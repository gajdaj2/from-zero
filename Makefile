install:
	pip install --upgrade pip && pip install -r requirements.txt

format:
	black *.py nlplogic

lint:
	pylint *.py nlplogic

test:
	python -m pytest -vv --cov=check_wiki  test_corenlp.py