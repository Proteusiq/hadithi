from river import compose
from river import preprocessing, stats
from river import naive_bayes


def penguins_model():
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
        | naive_bayes.MultinomialNB(alpha=1)
    )

    return model


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
