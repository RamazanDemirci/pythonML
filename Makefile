.PHONY:unittest

clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

test_main:
	python ./src/main.py test $(ARG) --parallel

test:
	python -m unittest 

run:
	python ./src/main.py