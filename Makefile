VENV := .env
PYTHON := $(VENV)/bin/python3.9
PIP := $(VENV)/bin/pip

.PHONY: run clean
# Run with the venv python instead of the system one
run:	$(VENV)/bin/activate
	${PYTHON} src/main.py

setup:	$(VENV)/bin/activate

# refresh your virtual environment and run your app with this virtual environment.
$(VENV)/bin/activate:	requirements.txt
	python3.9 -m venv ${VENV}
	${VENV}/bin/pip install -r requirements.txt

clean:
	rm -rf src/__pycache__
	rm -rf ${VENV}
