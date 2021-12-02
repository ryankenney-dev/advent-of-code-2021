Advent of Code 2021
================

Create the local `.venv`:

    python3 -m venv .venv

Download dependencies:

    pipenv run pip install -r requirements.txt

Run type checking:

    pipenv run mypy ./

Run all unit tests:

    pipenv run python -m unittest discover -s test

Run a specific puzzle:

    pipenv run python main.py -p day1_part1
