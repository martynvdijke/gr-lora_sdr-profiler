.DEFAULT_GOAL := help
.PHONY: coverage deps help lint publish push test tox requirements venv

venv: ## Makes new virtual venv and loads all dependencies
	python -m venv env
	. env/bin/activate
	$(MAKE) deps

coverage:  ## Run tests with coverage
	python -m coverage erase
	python -m coverage run --include=gr_lora_sdr_profiler/* -m pytest -ra
	python -m coverage report -m

deps:  ## Install dependencies
	python -m pip install --upgrade pip
	python -m pip install black coverage flake8 flit mccabe mypy pylint pytest tox tox-gh-actions pandas matplotlib wandb
	python -m pip freeze > requirements.txt

lint:  ## Lint and static-check
	python -m flake8 gr_lora_sdr_profiler
	python -m pylint gr_lora_sdr_profiler
	python -m mypy gr_lora_sdr_profiler

publish:  ## Publish to PyPi
	python -m flit publish

push:  ## Push code with tags
	git push && git push --tags

test:  ## Run tests
	python -m pytest -ra

requirements:	## Update requirements.txt
	python -m pip freeze > requirements.txt

tox:   ## Run tox
	python -m tox

help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [task]"; \
	printf "%-20s %s\n" "task" "help" ; \
	printf "%-20s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-20s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done
