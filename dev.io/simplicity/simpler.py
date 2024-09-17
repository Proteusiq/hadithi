
# Function is simpler than  class

from pathlib import Path

def load(file_path: Path) -> str:
  with open(file_path, "r") as file:
    return file.read()

 
def main() -> None:
  file_path = Path("README.md")
  data = load(file_path)
  print(data)

if __name__ == "__main__":
  main()
