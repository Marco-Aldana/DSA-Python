# DSA-Python
"This is a repository to study and store data structure and algorithms in python"

to create virtual environment in linux or macOS
```bash
# init
python3 -m venv .venv

#activate
source .venv/bin/activate

#installing
pip install -r requirements.txt

#verify successful installation
pytest --version  

#deactivate
deactivate

#update requeriments document for new libs
pip freeze > Requirements.txt
```

To install just run pip install in your local environment

 ### To Execute tests just run pytest commands
```bash
#execute from project root folder and use prefix 
python -m pytest

# All tests
pytest

# Specific file
pytest test_ejemplo.py

# Specific function
pytest test_ejemplo.py::test_funcion

# Specific class
pytest test_ejemplo.py::TestClase

# With verbose
pytest -v

# Only last failed
pytest --lf

# Stop in first fail
pytest -x

# Stop after N fails
pytest --maxfail=3

# In parallel (require pytest-xdist)
pytest -n 4
```