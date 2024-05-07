#!/bin/bash

cd ./app

alembic upgrade head

python3 main.py