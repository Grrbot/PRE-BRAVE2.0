
import torch
import os
from IPython.display import Image, clear_output  # to display images

print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")



# Model
model = torch.hub.load('ultralytics/yolov5', 'custom', path='run4.pt')  # or yolov5n - yolov5x6, custom

# Images
img = 'plane.png'  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

#Print relusts
print(results.pandas().xyxy[0])

# Results
results.show()  # or .show(), .save(), .crop(), .pandas(), etc.
