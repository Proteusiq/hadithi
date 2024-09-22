"""
This module provides functionality to download a PDF file from a specified URL
and save it to a local directory.
"""

from pathlib import Path
from httpx import stream


def get_material() -> None:
    """
    Downloads a PDF file from a predefined URL and saves it to the local 'data' directory.

    The function streams the content of the file to avoid loading the entire file into memory.
    """
    URI = "https://danskogproever.dk/media/11242/laeremateriale-til-indfoedsretsproeve-2023.pdf"
    file = Path("data/indfoedsretsproeve2023.pdf")
    with stream("GET", URI) as r, file.open("wb") as f:
        for chuck in r.iter_raw():
            f.write(chuck)


if __name__ == "__main__":
    get_material()
