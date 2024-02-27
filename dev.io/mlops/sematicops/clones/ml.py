from river import compose
from river import preprocessing, stats
from river import forest


# ml_predictor = naive_bayes.MultinomialNB(alpha=1)
ml_predictor = forest.AMFClassifier(
    n_estimators=10,
    use_aggregation=True,
    dirichlet=0.5,
    seed=1
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
