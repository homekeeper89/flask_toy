lint:
	pylint src/

hint:
	mypy src/

no_merge_dev:
	git brandc --no-merged develop