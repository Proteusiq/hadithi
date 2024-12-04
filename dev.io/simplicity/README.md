 ____  _                 _ _      _ _         
/ ___|(_)_ __ ___  _ __ | (_) ___(_) |_ _   _ 
\___ \| | '_ ` _ \| '_ \| | |/ __| | __| | | |
 ___) | | | | | | | |_) | | | (__| | |_| |_| |
|____/|_|_| |_| |_| .__/|_|_|\___|_|\__|\__, |
                  |_|                   |___/ 


“You know you’ve achieved perfection in design, not when you have nothing more to add, but when you have nothing more to take away.”
— Anotine de Saint-Exupery

In his amazing youtube channel [ArjanCodes](https://youtu.be/yFLY0SVutgM?si=a8MauvOyRLSbI6_C), Arjan, a software developer and educator, shared seven common mistakes new Python Object Oriented Programmers ought to avoid.
In this article, I will go a step deeper using two of his examples and one of my own.

```python
from pathlib import Path

class DataLoader:
  def __init__(self, file_path:Path) -> None:
    self.file_path = file_path

  def load(self) -> str:
    with open(self.file_path, "r") as file:
      return file.read()


def main() -> None:
  file_path = Path("README.md")
  loader = DataLoader(file_path)
  data = loader.load()
  print(data)

if __name__ == "__main__":
  main()

```
Function > Class = Functions is simplier than a class

```python
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

```
No Function > Function =  No function is simplier than a function
> pathlib has in built context manager for opening and read the file contents
```python
from pathlib import Path


def main() -> None:
  file_path = Path("README.md")
  data: str = file_path.read_text()
  print(data)

if __name__ == "__main__":
  main()

```

“Anything simple always interests me.”
— David Hockney


“Simplicity is prerequisite for reliability."
— Edsger Dijkstraui

# Bank
