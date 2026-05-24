.PHONY: install validate test build-index export-backend export-client term-matrix clean help

PYTHON := python3
SCRIPTS := scripts

help:
	@echo "Defend-A-Pedia · Makefile targets"
	@echo "  install         install dependencies"
	@echo "  validate        run all validators (terms · jsonl · schemas)"
	@echo "  test            run pytest test suite"
	@echo "  build-index     regenerate docs/vocabulary/index.md"
	@echo "  export-backend  emit backend field map (data/backend_field_map.jsonl)"
	@echo "  export-client   emit client dictionary (data/client_language_map.jsonl)"
	@echo "  term-matrix     generate cross-category term matrix"
	@echo "  clean           remove build artifacts"

install:
	$(PYTHON) -m pip install -r requirements.txt

validate:
	$(PYTHON) $(SCRIPTS)/validate_terms.py
	$(PYTHON) $(SCRIPTS)/validate_jsonl.py
	$(PYTHON) $(SCRIPTS)/validate_schemas.py

test:
	$(PYTHON) -m pytest tests/ -v

build-index:
	$(PYTHON) $(SCRIPTS)/build_index.py

export-backend:
	$(PYTHON) $(SCRIPTS)/export_backend_map.py

export-client:
	$(PYTHON) $(SCRIPTS)/export_client_dictionary.py

term-matrix:
	$(PYTHON) $(SCRIPTS)/generate_term_matrix.py

clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
