# Agents

```
# uv flow
uv init packagename
cd packagename
mkdir -p src/packagename tests/
uv python pin 3.11

echo -e '\n[tool.pytest.ini_options]\npythonpath = ["src"]' >> pyproject.toml
echo -e '\n[tool.ruff.lint]\nselect = [\n\t  "A", # warn about shadowing built-ins\n\t  "E", # style stuff, whitespaces\n\t  "F", # important pyflakes lints\n\t  "I", # import sorting\n\t  "N", # naming\n\t]' >> pyproject.toml


uv add --dev ruff pytest
~~
```
```~~ 
```
