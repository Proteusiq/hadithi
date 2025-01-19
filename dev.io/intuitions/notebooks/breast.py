import marimo

__generated_with = "0.10.13"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    mo.md(
        """
        # Human Intuition is All You Need
        ## 🔎 A Sherlock Holmes' Path to Breast Cancer's Classification
        """
    )
    return (mo,)


@app.cell(hide_code=True)
def _():
    class Image(object):
        def __init__(self, url: str) -> None:
            self.url = url

        def _mime_(self) -> tuple[str, str]:
            return ("image/png", self.url)


    Image(
        "https://miro.medium.com/v2/resize:fit:1400/format:webp/1*DVtYTGpEVxtsOWcu560rLw.jpeg"
    )
    return (Image,)


@app.cell
def _(breasts):
    # 569 rows

    _breasts = breasts.sample(fraction=1.0, seed=42, shuffle=True)
    train_data = _breasts.head(569 - 150)
    test_data = _breasts.tail(150)
    _breasts
    return test_data, train_data


@app.cell(hide_code=True)
def _(mo):
    mo.md("""## Test Inuitions""")
    return


@app.cell
def _(mo, test_data):
    mo.ui.table(test_data.sample(3, seed=42).to_dicts())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
        # 🦔 Intuition Estimator
        **Steps:**

        - [x] Use categorical features for filtering
        - [x] Use numerical features absolute difference for ranking
        - [ ] Use text features similiarities for ranking
        - [x] Select top_k [classification  →  mode | regression  → mean] = complete :tada:
        """
    )
    return


@app.cell
def _(pl):
    from typing import Annotated, Self


    class Intuition:
        def __init__(self, n: Annotated[int, "nearest neighbors"]) -> Self:
            self.n = n
            self.is_fitted = False

        def fit(self, X: pl.DataFrame, y: pl.Series) -> Self:
            self.lookup = X.insert_column(0, y)
            self.is_fitted = True

            return self

        def predict(self, X: pl.DataFrame) -> list[str]:
            predictions = [
                self.lookup
                # Similarity => Distance
                .with_columns(
                    pl.col("area_mean").sub(row["area_mean"]).abs(),
                    pl.col("concavity_mean").sub(row["concavity_mean"]).abs(),
                )
                .with_columns(
                    pl.col("area_mean")
                    .add(pl.col("concavity_mean"))
                    .mul(-1)
                    .alias("combined_diff")
                )
                # Nearest Neighbor
                .top_k(5, by="combined_diff")
                .select(pl.col("diagnosis").mode())
                .item(0, "diagnosis")
                for row in X.iter_rows(named=True)
            ]

            return predictions
    return Annotated, Intuition, Self


@app.cell(hide_code=True)
def _(mo):
    mo.md("""##🧪  Train & Test Data""")
    return


@app.cell
def _(Intuition, pl, test_data, train_data):
    X_train, y_train = (
        train_data.select(pl.exclude("diagnosis")),
        train_data.get_column("diagnosis"),
    )
    X_test, y_test = (
        test_data.select(pl.exclude("diagnosis")),
        test_data.get_column("diagnosis"),
    )
    estimator = Intuition(n=5).fit(X=X_train, y=y_train)
    return X_test, X_train, estimator, y_test, y_train


@app.cell(hide_code=True)
def _(mo):
    mo.md("""##🔬 Prediction and Results""")
    return


@app.cell
def _(X_test, estimator, y_test):
    predictions = estimator.predict(X=X_test)
    predictions == y_test
    return (predictions,)


@app.cell
def _(pl):
    HEADERS = [
        "id",
        "diagnosis",
        "radius_mean",
        "texture_mean",
        "perimeter_mean",
        "area_mean",
        "smoothness_mean",
        "compactness_mean",
        "concavity_mean",
        "concave_points_mean",
        "symmetry_mean",
        "fractal_dimension_mean",
        "radius_se",
        "texture_se",
        "perimeter_se",
        "area_se",
        "smoothness_se",
        "compactness_se",
        "concavity_se",
        "concave_points_se",
        "symmetry_se",
        "fractal_dimension_se",
        "radius_worst",
        "texture_worst",
        "perimeter_worst",
        "area_worst",
        "smoothness_worst",
        "compactness_worst",
        "concavity_worst",
        "concave points_worst",
        "symmetry_worst",
        "fractal_dimension_worst",
    ]
    URI = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"
    breasts = pl.read_csv(URI, has_header=False, new_columns=HEADERS)
    breasts
    return HEADERS, URI, breasts


@app.cell
def _():
    import polars as pl
    import altair as alt
    return alt, pl


if __name__ == "__main__":
    app.run()
