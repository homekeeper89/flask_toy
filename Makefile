lint:
	pylint src/

hint:
	mypy src/

no_merge_dev:
	git branch --no-merged develop