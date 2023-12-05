from roboflow import Roboflow
from facetally.params import *


def load_data_from_roboflow():
    rf = Roboflow(api_key="NtHDWWC0JhDMlxNNhpDb")
    project = rf.workspace("le-wagon-borrz").project("facetally-tiowv")
    dataset = project.version(1).download("yolov8", location=LOCAL_DATA_PATH)


if __name__ == "__main__":
    load_data_from_roboflow()
