.PHONY: help check

help:
	@echo "Available targets: check"

check:
	python -m compileall -q scripts src
