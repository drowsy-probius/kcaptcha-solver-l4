#!/bin/bash
VENV_DIR="venv"
SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}"; )" &> /dev/null && pwd 2> /dev/null; )";
SRC_DIR="$SCRIPT_DIR/.."
VENV_ACTIVATE="$SRC_DIR/$VENV_DIR/bin/activate"
PYTHON_PATH="$SRC_DIR/$VENV_DIR/bin/python3"

echo "script dir: $SCRIPT_DIR"

cd $SRC_DIR

if [ ! -d "$VENV_DIR" ]; then
  echo "    python virtual environment is not created. Creating it at '$VENV_DIR' directory"
  python3 -m virtualenv "$VENV_DIR" --python=python3.9
fi

echo "    Activate python venv"
source $VENV_ACTIVATE

echo "    Install requirements"
python3 -m pip install -r requirements.txt
python3 manage.py migrate

echo "    Run server"
python3 manage.py runserver 0.0.0.0:8000