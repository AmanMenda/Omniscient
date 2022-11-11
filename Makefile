VENV := .env
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

.PHONY: run clean

# Run with the venv python instead of the system one
run:	$(VENV)/bin/activate
	${PYTHON} src/app.py

setup:	$(VENV)/bin/activate

# refresh your virtual environment and run your app with this virtual environment.
$(VENV)/bin/activate:	requirements.txt
	python3 -m venv ${VENV}
	${VENV}/bin/pip install -r requirements.txt

# run tests
tests_run:
	pytest

clean:
	rm -rf src/__pycache__
	rm -rf src/commands/__pycache__
	rm -rf tests/__pycache__
	rm -rf ${VENV}
