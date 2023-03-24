#!/bin/bash
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}"; )" &> /dev/null && pwd 2> /dev/null; )";
SRC_DIR="$SCRIPT_DIR/.."

cd $SRC_DIR

# python manage.py migrate
python manage.py runserver 0.0.0.0:8000
