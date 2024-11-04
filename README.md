# action-python-template

A template repository for GitHub Actions implemented in Python.

## Content

* `pytest` for tests: `make test`
* `ruff` for linting/formatting: `make lint` (replaces both `black` and `isort`)
* `.github` with actions ready to be used
    * ...
* `action.yml` and `entrypoint.py` to serve as placeholders with a valid dummy action
* Template README.md below

## New project checklist

* [ ] Replace `action.yml` with your action details
* [ ] Replace `entrypoint.py` with your code
* [ ] Replace `LICENSE` if MIT does not apply
* [ ] Search the project for `# TODO` to find the (minimum list of) places that need to be changed

---
---
---


[![Build and Test](https://github.com/actions/checkout/actions/workflows/test.yml/badge.svg)](https://github.com/actions/checkout/actions/workflows/test.yml)

# action-python-template

This action takes 2 integers as input and returns the sum of those in the output variable `sum`.

It also adds a joke to output `joke` to brighten your day.

# What's new

Please refer to the [release page](https://github.com/actions/checkout/releases/latest) for the latest release notes.

# Usage

<!-- start usage -->
```yaml
name: auto update

on:
  schedule:
    - cron: "0 12 * * *"
  workflow_dispatch:

jobs:
  autoupdate:
    runs-on: ubuntu-latest
    steps:
      - name: scan target with template
        id: autoupdate
        uses: fopina/action-python-template@dev
      - name: test sum2
        run: |
          cat <<'EOF'
          ${{ steps.autoupdate.outputs.sum }}
          EOF
      - name: scan target with template
        id: another
        uses: fopina/action-python-template@dev
        with:
          number-one: 2
          number-two: 3
      - name: test sum2
        run: |
          echo ${{ steps.another.outputs.sum }}
- uses: fopina/action-python-template@v1
  with:
    # first number to sum
    number-one: ''

    # second number to sum
    number-two: ''

    # imaginary input that would have a default for documentation purposes
    # Default: ${{ github.token }}
    # token: ''
```
<!-- end usage -->

# Scenarios

- [Sum two numbers](#sum-two-numbers)
- [Easter egg](#easter-egg)

## Sum two numbers

```yaml
- uses: actions/checkout@v4
  with:
    sparse-checkout: .
```

## Easter egg

```yaml
- uses: actions/checkout@v4
  with:
    sparse-checkout: |
      .github
      src
```
