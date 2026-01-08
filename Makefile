all: main

main: configure #folders

configure:
	@python3 config.py

aux:
	python3 -m venv .venv
	. .venv/bin/activate
	pip install -r requirements.txt

