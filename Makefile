install:
	@pip install -e .

train_model:
	@python facetally/interface/main.py
