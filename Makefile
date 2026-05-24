.PHONY: install validate test build-index export-backend export-client term-matrix \
        mint manifest issue indexes snapshot verify upload deed-all clean help

PYTHON := python3
SCRIPTS := scripts

help:
	@echo "Defend-A-Pedia · Makefile targets"
	@echo ""
	@echo "  Core (v0.2.x · vocabulary infrastructure):"
	@echo "    install         install dependencies"
	@echo "    validate        run all validators (terms · jsonl · schemas)"
	@echo "    test            run pytest test suite"
	@echo "    build-index     regenerate docs/vocabulary/index.md"
	@echo "    export-backend  emit data/backend_field_map.jsonl"
	@echo "    export-client   emit data/client_language_map.jsonl"
	@echo "    term-matrix     generate cross-category term matrix"
	@echo ""
	@echo "  Deed pipeline (v0.3.0 · vocabulary as books-and-records):"
	@echo "    mint            markdown → JSON + receipt + DDEED-VOCAB per term"
	@echo "    issue           run 6-check validator chain · promote drafts"
	@echo "    manifest        emit SHA256SUMS + vocabulary_manifest_v*.json"
	@echo "    indexes         build 5 cross-reference indexes"
	@echo "    snapshot        capture daily snapshot to streetledger.eth namespace"
	@echo "    verify          re-hash + compare against manifest · integrity check"
	@echo "    upload          dry-run rsync to NAS (use --confirm to actually push)"
	@echo ""
	@echo "  Combined:"
	@echo "    deed-all        mint → issue → manifest → indexes → snapshot → verify"
	@echo "    clean           remove build artifacts"

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

mint:
	$(PYTHON) $(SCRIPTS)/mint_vocabulary_object.py

issue:
	$(PYTHON) $(SCRIPTS)/issue_vocabulary_deed.py

manifest:
	$(PYTHON) $(SCRIPTS)/generate_sha256_manifest.py

indexes:
	$(PYTHON) $(SCRIPTS)/build_cross_reference_index.py

snapshot:
	$(PYTHON) $(SCRIPTS)/snapshot_vocabulary_state.py --cadence daily

verify:
	$(PYTHON) $(SCRIPTS)/verify_deed_integrity.py

upload:
	$(PYTHON) $(SCRIPTS)/upload_to_object_storage.py --target nas

deed-all:
	$(PYTHON) $(SCRIPTS)/mint_vocabulary_object.py
	$(PYTHON) $(SCRIPTS)/issue_vocabulary_deed.py
	$(PYTHON) $(SCRIPTS)/generate_sha256_manifest.py
	$(PYTHON) $(SCRIPTS)/build_cross_reference_index.py
	$(PYTHON) $(SCRIPTS)/snapshot_vocabulary_state.py --cadence daily
	$(PYTHON) $(SCRIPTS)/verify_deed_integrity.py

clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
