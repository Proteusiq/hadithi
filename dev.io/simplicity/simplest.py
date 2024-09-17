
# No function is simpler than function (in this case) 

from pathlib import Path


def main() -> None:
    file_path = Path("README.md")
    data: str = file_path.read_text()
    print(data)


if __name__ == "__main__":
    main()
