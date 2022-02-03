help:					##@starter Show this help.
	@perl -e '$(HELP_FUNC)' $(MAKEFILE_LIST)

setup:					##@starter Initial env setup.
	curl -sSL https://install.python-poetry.org | python3 -
	poetry config virtualenvs.in-project true
	poetry install

tests:					##@common Run tests.
	poetry run pytest -vv

coverage: _generate_coverage_local _check_coverage_ci	##@common Generate local HTML coverage report and open it.

_generate_coverage_local:		# Generate HTML coverage report
	poetry run pytest -vv --cov=draft --cov-report=html
	@open htmlcov/index.html

_generate_coverage_ci:			# Generate XLM coverage report
	poetry run pytest -vv --cov=draft --cov-report=xml

_check_coverage_ci:				# Check coverage percentage
	poetry run coverage report --fail-under=70

lint: lint_python   ##@common Runs all linters, when possible the linter will automatically reformat the file for you.

CI_CMDS := _generate_coverage_ci
CI_CMDS += _check_coverage_ci
CI_CMDS += _lint_python_ci
ci:	$(CI_CMDS)			##@common Runs everything CI typically does. Can/should run this prior to pushing new commits.

lint_python:			# Lint python, fix errors
	@echo "\n> Linting Python"
	poetry run black . --line-length 120

_lint_python_ci:		# Lint python, raise errors
	poetry run black . --line-length 120 --check --diff


# ----------------------------------------
# https://gist.github.com/prwhite/8168133#gistcomment-1712123
# ----------------------------------------
RED := $(shell tput -Txterm setaf 1)
GREEN := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
BLUE := $(shell tput -Txterm setaf 4)
PINK := $(shell tput -Txterm setaf 5)
TEAL := $(shell tput -Txterm setaf 6)
GREY := $(shell tput -Txterm setaf 7)
BLACK := $(shell tput -Txterm setaf 8)
RESET := $(shell tput -Txterm sgr0)
HELP_FUNC = \
	%help; \
	while(<>) { \
		if(/^([a-z0-9_-]+):.*\#\#(?:@(\w+))?\s(.*)$$/) { \
			push(@{$$help{$$2}}, [$$1, $$3]); \
		} \
	}; \
	print "usage: make ${BLUE}[command]${RESET}\n\n"; \
	for ( sort keys %help ) { \
		print "$$_:\n"; \
		printf("  ${BLUE}%-20s${RESET} %s\n", $$_->[0], $$_->[1]) for @{$$help{$$_}}; \
		print "\n"; \
	}