#display inference on ALL test images

import glob
from IPython.display import Image, display

for imageName in glob.glob('runs/detect/exp/*.png'): #assuming JPG
    display(Image(filename=imageName))
    print("\n")
