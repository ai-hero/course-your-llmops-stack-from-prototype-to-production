#!/bin/bash
python3.9 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
pre-commit install
pre-commit autoupdate
