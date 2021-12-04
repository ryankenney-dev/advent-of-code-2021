#!/bin/bash

set -ex

# Create python environment
python3.8 -m venv .venv

# Install dependencies
pipenv run pip install -r requirements

# Run static type checker
pipenv run mypy ./

# Run unit tests
pipenv run python -m unittest discover -s test

# Run main for all puzzles
pipenv run python main.py --puzzle all
#pipenv run python main.py --puzzle d1p1

