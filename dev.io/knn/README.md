# kNN in 🦀 for 🐍

Using PyO3, and `maturin` to generate Rust bindings for Python. The goal of this repository is to show how we can implement kNN writen in Rust, into Python.

## Installation
```bash
# clone the repo, install rust and pixi and run pixi install
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
curl -fsSL https://pixi.sh/install.sh | bash
pixi install

# develop or build
pixi run maturin build
pixi run python -m use.ml
```