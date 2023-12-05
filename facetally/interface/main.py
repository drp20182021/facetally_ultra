from facetally.data.roboflow_load import load_data_from_roboflow
from facetally.mllogic.train import train_model
from facetally.params import *


def main():
    load_data_from_roboflow()
    train_model(epochs=NUM_EPOCHS)


if __name__ == "__main__":
    main()
