from river import compose
from river import preprocessing, stats
from river import naive_bayes


def build_model():
    island_transformation = compose.Select("island") | preprocessing.OneHotEncoder(
        drop_first=True,
    )

    sex_transformation = (
        compose.Select("sex")
        | preprocessing.StatImputer(("sex", stats.Mode()))
        | preprocessing.OneHotEncoder(drop_first=True)
    )

    numeric_transformation = (
        compose.Select(
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm",
            "body_mass_g",
        )
        | preprocessing.StatImputer(
            ("bill_length_mm", stats.Mean()),
            ("bill_depth_mm", stats.Mean()),
            ("flipper_length_mm", stats.Mean()),
            ("body_mass_g", stats.Mean()),
        )
    )

    model = (
        island_transformation
        + sex_transformation
        + numeric_transformation
        | naive_bayes.MultinomialNB(alpha=1)
    )

    return model


if __name__ == "__main__":
    from data.penguins import fetch_data
    from river import metrics

    data = fetch_data()
    model = build_model()

    y_true = []
    y_pred = []
    for d in data:
        y = d.pop("species")
        X = d

       
        y_hats = model.predict_one(X)
        model.learn_one(X, y)

        y_true.append(y)
        y_pred.append(y_hats)

        print(f"{y=} {y_hats}")

    print(f"ROC AUC: {metrics.roc_auc(y_true, y_pred) : .4f}")
