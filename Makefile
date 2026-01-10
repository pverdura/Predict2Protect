all: help

help:
	@echo "make options:"
	@echo "  help   - Shows this list"
	@echo "  config - Configures the working environment"
	@echo "  train  - Trains the model"

config:
	@python3 src/config.py

train:
	@python3 src/train.py

