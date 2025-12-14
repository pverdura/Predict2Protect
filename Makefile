all: main

main: pyenv folders

pyenv:
	python3 -m venv .venv
	. .venv/bin/activate
	pip install -r requirements.txt


folders:
	mkdir data
	mkdir data/.model

