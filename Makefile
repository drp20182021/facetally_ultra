install:
	@pip install -e .

train_model:
	@python face_tally/interface/main.py
