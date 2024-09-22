from pathlib import Path
from httpx import stream


def get_material() -> None:
    URI = "https://danskogproever.dk/media/11242/laeremateriale-til-indfoedsretsproeve-2023.pdf"
    file = Path("data/indfoedsretsproeve2023.pdf")
    with stream("GET", URI) as r, file.open("wb") as f:
        for chuck in r.iter_raw():
            f.write(chuck)


if __name__ == "__main__":
    get_material()
