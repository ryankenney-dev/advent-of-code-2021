Advent of Code 2021
================

Create the local `.venv`:

    python3.8 -m venv .venv

Download dependencies:

    pipenv run pip install -r requirements.txt

Run type checking:

    pipenv run mypy ./

Run all unit tests:

    pipenv run python -m unittest discover -s test

Run a specific puzzle:

    pipenv run python main.py -p d1p1
