all: help

help:
	@echo "make options:"
	@echo "  help - Shows this list"
	@echo "  config - Configures the working environment"
	@echo "  help - Trains the model"

config:
	@python3 config.py

train:
	@python3 src/train.py

