
from roboflow import Roboflow
rf = Roboflow(api_key="gYUC0WWrG5HYqEXoJpIq")
project = rf.workspace("seaplane").project("seaplanes")
dataset = project.version(1).download("yolov5")