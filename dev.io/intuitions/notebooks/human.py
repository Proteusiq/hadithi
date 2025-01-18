import marimo

__generated_with = "0.10.13"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    mo.md(
        """
        # Human Intuition is All You Need
        ## 🔎 A Sherlock Holmes' Path to Penguin's Classification
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
        "https://allisonhorst.github.io/palmerpenguins/reference/figures/culmen_depth.png"
    )
    return (Image,)


@app.cell(hide_code=True)
def _(alt, penguins):
    x, y = "bill_depth_mm", "bill_length_mm"

    base = alt.Chart(penguins).encode(
        x="bill_depth_mm:Q", y="bill_length_mm:Q", color="species:N"
    )

    points = base.mark_circle(size=60, opacity=0.5).encode(
        x=alt.X(x, scale=alt.Scale(domain=[0, 25])),
        y=alt.Y(y, scale=alt.Scale(domain=[0, 65])),
        color="species",
        tooltip=["species", "island", "body_mass_g"],
    )

    density_x = (
        base.transform_density(
            density="bill_depth_mm",
            groupby=["species"],
            as_=["bill_depth_mm", "density"],
        )
        .mark_area(orient="vertical", opacity=0.5)
        .encode(
            y="density:Q",
        )
        .properties(
            height=100,
            title={
                "text": [
                    "Hello, Penguins!",
                ],
                "subtitle": [
                    f"What is the relationship between {x!r} and {y!r}?",
                ],
                "color": "blue",
                "subtitleColor": "grey",
                "anchor": "start",
                "fontSize": 20,
            },
        )
    )

    density_y = (
        base.transform_density(
            density="bill_length_mm",
            groupby=["species"],
            as_=["bill_length_mm", "density"],
        )
        .mark_area(orient="horizontal", opacity=0.5)
        .encode(
            x="density:Q",
        )
        .properties(width=100)
    )

    (density_x & (points | density_y))
    return base, density_x, density_y, points, x, y


@app.cell(hide_code=True)
def _(chart, mo):
    mo.vstack([chart, mo.ui.table(chart.value)])
    return


@app.cell(hide_code=True)
def _(mo, points, x, y):
    chart = points.properties(
        title={
            "text": [
                "Filter, Penguins!",
            ],
            "subtitle": [
                f"What is the relationship between {x!r} and {y!r}?",
            ],
            "color": "blue",
            "subtitleColor": "grey",
            "anchor": "start",
            "fontSize": 20,
        }
    )

    chart = mo.ui.altair_chart(chart)
    return (chart,)


@app.cell
def _(penguins, pl):
    # 333 rows

    _penguins = penguins.filter(
        pl.col("sex").is_not_null(), pl.col("island").is_not_null()
    ).sample(fraction=1.0, seed=42, shuffle=True)
    train_data = _penguins.head(333 - 70)
    test_data = _penguins.tail(70)
    _penguins
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
def _(bill_depth, bill_length, island, pl, sex, train_data):
    (
        train_data.filter(
            # Filters => Tree
            pl.col("island").eq(island.value),  # ↓ 97 rows
            pl.col("sex").eq(sex.value),  # ↓ 49 rows
        )  .with_columns(
            pl.col("bill_depth_mm")
            .sub(bill_depth.value)
            .abs()
            .alias("diff_bill_depth"),
            pl.col("bill_length_mm")
            .sub(bill_length.value)
            .abs()
            .alias("diff_bill_length"),
        )
        .with_columns(
            pl.col("diff_bill_depth")
            .add(pl.col("diff_bill_length"))
            .mul(-1)
            .alias("combined_diff")
        )
        .top_k(5, by="combined_diff")  # ↓ 5 rows → Mode
        .select(
            "species",
            "combined_diff",
        )
        .select(pl.col("species").mode())  # ↓ 1 rows
      
    )
    return


@app.cell(hide_code=True)
def _(mo, train_data):
    island = mo.ui.dropdown(
        options=train_data["island"].unique().to_numpy(),
        value="Dream",
        label=f"{'Island':.<12}",
    )
    sex = mo.ui.dropdown(
        options=["male", "female"], value="male", label=f"{'Gender':.<11}"
    )
    bill_depth = mo.ui.number(value=19.5, label=f"{'Bill depth':.<11}")
    bill_length = mo.ui.number(value=51.9, label="Bill length")
    mo.vstack([island, sex, bill_depth, bill_length])
    return bill_depth, bill_length, island, sex


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """# 🦔 Intuition Estimator
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
                self.lookup.filter(
                    # Filters => Tree
                    pl.col("island").eq(row["island"]),
                    pl.col("sex").eq(row["sex"]),
                )
                # Similarity => Distance
                .with_columns(
                    pl.col("bill_depth_mm").sub(row["bill_depth_mm"]).abs(),
                    pl.col("bill_length_mm").sub(row["bill_length_mm"]).abs(),
                )
                .with_columns(
                    pl.col("bill_depth_mm")
                    .add(pl.col("bill_length_mm"))
                    .mul(-1)
                    .alias("combined_diff")
                )
                # Nearest Neighbor
                .top_k(5, by="combined_diff")
                .select(pl.col("species").mode())
                .item(0, "species")
                for row in X.iter_rows(named=True)
            ]

            return predictions
    return Annotated, Intuition, Self


@app.cell(hide_code=True)
def _(mo):
    mo.md("##🧪  Train & Test Data")
    return


@app.cell
def _(Intuition, pl, test_data, train_data):
    X_train, y_train = (
        train_data.select(pl.exclude("species")),
        train_data.get_column("species"),
    )
    X_test, y_test = (
        test_data.select(pl.exclude("species")),
        test_data.get_column("species"),
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
    URI = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/penguins.csv"
    penguins = pl.read_csv(URI).with_columns(pl.col("sex").str.to_lowercase())
    penguins
    return URI, penguins


@app.cell
def _():
    import polars as pl
    import duckdb
    import altair as alt
    return alt, duckdb, pl


if __name__ == "__main__":
    app.run()
