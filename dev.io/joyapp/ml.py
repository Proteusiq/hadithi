import pickle
from pathlib import Path
from typing import Literal

from river import compose
from river import preprocessing, stats
from river import forest

# from river import naive_bayes
from tenacity import (
    retry,
    retry_if_exception_type,
    retry_if_result,
    wait_random_exponential,
)


# ml_predictor = naive_bayes.MultinomialNB(alpha=1)
ml_predictor = forest.AMFClassifier(
    n_estimators=10, use_aggregation=True, dirichlet=0.5, seed=1
)


def penguins_model(ml_predictor=ml_predictor) -> compose.Pipeline:
    island_transformation = compose.Select("island") | preprocessing.OneHotEncoder(
        drop_first=True
    )

    sex_transformation = (
        compose.Select("sex")
        | preprocessing.StatImputer(("sex", stats.Mode()))
        | preprocessing.OneHotEncoder(drop_first=True)
    )

    numeric_transformation = compose.Select(
        "bill_length_mm",
        "bill_depth_mm",
        "flipper_length_mm",
        "body_mass_g",
    ) | preprocessing.StatImputer(
        ("bill_length_mm", stats.Mean()),
        ("bill_depth_mm", stats.Mean()),
        ("flipper_length_mm", stats.Mean()),
        ("body_mass_g", stats.Mean()),
    )

    model = (
        island_transformation + sex_transformation + numeric_transformation
        | ml_predictor
    )

    return model


@retry(
    retry=retry_if_exception_type(EOFError) | retry_if_result(lambda d: d is None),
    wait=wait_random_exponential(multiplier=1, max=6),
)
def ml_io(
    model_file: Path,
    mode: Literal["wb", "rb"] = "rb",
    ml_object: compose.Pipeline | None = None,
):
    if mode == "rb" and not model_file.exists():
        ml = penguins_model()
        ml.meta = {
            "predicted": 0,
            "learned": 0,
        }
        # save the first local copy (god like ...)
        model_file.write_bytes(pickle.dumps(ml_object))

        return ml

    elif mode == "rb" and model_file.exists():
        ml = pickle.loads(model_file.read_bytes())
        return ml

    elif mode == "wb":
        return model_file.write_bytes(pickle.dumps(ml_object))
    else:
        NotImplemented(f"mode can only be `wb` or `rb`")


if __name__ == "__main__":
    from collections import defaultdict
    from data.penguins import fetch_data
    from river import metrics as m
    from sklearn.metrics import classification_report

    data = fetch_data()
    model = penguins_model()

    traces = defaultdict(list)

    report = m.ClassificationReport()

    for d in data:
        y_true = d.pop("species")
        X = d

        y_pred = model.predict_one(X)
        model.learn_one(X, y_true)

        if y_pred:
            report = report.update(y_true=y_true, y_pred=y_pred)
            traces["y_true"].append(y_true)
            traces["y_pred"].append(y_pred)

            model.meta = classification_report(
                traces["y_true"],
                traces["y_pred"],
                output_dict=True,
            )

    print(report)
