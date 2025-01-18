# intuitions

[![Release](https://img.shields.io/github/v/release/proteusiq/intuitions)](https://img.shields.io/github/v/release/proteusiq/intuitions)
[![Build status](https://img.shields.io/github/actions/workflow/status/proteusiq/intuitions/main.yml?branch=main)](https://github.com/proteusiq/intuitions/actions/workflows/main.yml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/proteusiq/intuitions/branch/main/graph/badge.svg)](https://codecov.io/gh/proteusiq/intuitions)
[![Commit activity](https://img.shields.io/github/commit-activity/m/proteusiq/intuitions)](https://img.shields.io/github/commit-activity/m/proteusiq/intuitions)
[![License](https://img.shields.io/github/license/proteusiq/intuitions)](https://img.shields.io/github/license/proteusiq/intuitions)

Using Human intuitions to solve problems

- **Github repository**: <https://github.com/proteusiq/intuitions/>
- **Documentation** <https://proteusiq.github.io/intuitions/>

## Getting started with your project

### 1. Create a New Repository

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:proteusiq/intuitions.git
git push -u origin main
```

### 2. Set Up Your Development Environment

Then, install the environment and the pre-commit hooks with

```bash
make install
```

This will also generate your `uv.lock` file

### 3. Run the pre-commit hooks

Initially, the CI/CD pipeline might be failing due to formatting issues. To resolve those run:

```bash
uv run pre-commit run -a
```

### 4. Commit the changes

Lastly, commit the changes made by the two steps above to your repository.

```bash
git add .
git commit -m 'Fix formatting issues'
git push origin main
```

You are now ready to start development on your project!
The CI/CD pipeline will be triggered when you open a pull request, merge to main, or when you create a new release.

To finalize the set-up for publishing to PyPI, see [here](https://proteusiq.github.io/pyproject/features/publishing/#set-up-for-pypi).
For activating the automatic documentation with MkDocs, see [here](https://proteusiq.github.io/pyproject/features/mkdocs/#enabling-the-documentation-on-github).
To enable the code coverage reports, see [here](https://proteusiq.github.io/pyproject/features/codecov/).

## Releasing a new version



---

Repository initiated with [proteusiq/pyproject](https://github.com/proteusiq/pyproject).
