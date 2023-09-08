from pathlib import Path
from orjson import loads

PENGUINS_DATA = "data/penguins.json"


def read_json(path: str) -> list[dict]:
    return loads(Path(path).read_text())


def fetch_data(path: str = PENGUINS_DATA):
    return read_json(path)


if __name__ == "__main__":
    print(fetch_data(path=PENGUINS_DATA))
