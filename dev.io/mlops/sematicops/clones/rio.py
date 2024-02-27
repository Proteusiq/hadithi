from pathlib import Path
from typing import Tuple
from orjson import loads

import sematic
import pandas as pd

PENGUINS_DATA = Path(__file__).parent.parent / "data/penguins.json"
FEATURES = [
    "sex",
    "island",
    "bill_length_mm",
    "bill_depth_mm",
    "flipper_length_mm",
    "body_mass_g",
]
TARGET = "species"


def read_json(path: Path) -> list[dict]:
    return loads(path.read_text())


def penguins_data(
    path: Path = PENGUINS_DATA,
    as_frame=False,
    return_X_y=False,
    features: list[str] = FEATURES,
    target: str = TARGET,
):
    data = read_json(path)

    if as_frame or return_X_y:
        data = pd.DataFrame(data)

    if return_X_y:
        X, y = data[features], data[target]

        return X, y

    return data


@sematic.func
def load_data() -> Tuple[pd.DataFrame, pd.DataFrame]:
    X, y = penguins_data(as_frame=True, return_X_y=True)
    return X, y


if __name__ == "__main__":
    print(penguins_data(path=PENGUINS_DATA))
