all: test

test: lint
	bash test.sh

install_test:
	pip install -r tests/requirements.txt

git-diff-check:
	git diff --exit-code

lint:
	bash lint.sh

format:
	isort -y $(find httpfs -name "*.py"|xargs echo) $(find tests -name "*.py"|xargs echo)
	black -l 79 httpfs
	black -l 79 tests

git-diff-check:
	git diff --exit-code
