test:
	pytest agro/tests -v --cov

install:
	pip install -r requirements.txt

clean:
	rm -rf htmlcov
	rm -rf agro/testing.db