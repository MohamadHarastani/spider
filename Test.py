# Use for Python 2:
#from spider_files import *
# Works with Python 3:
from spider_files3 import *
import numpy as np
from PIL import Image

f = open_volume("volume.vol")
print(np.shape(f))
save_volume(f,"saved.vol")

show_header("volume.vol")

# Two ways to open a spider image and a numpy array:
I1 = Image.open("image.spi")
I1 = np.array(Image.open("image.spi"))
I2 = open_image("image.spi")

print("Mean difference between the two images",np.mean(I1-I2))

# In either ways, we can use the function from pillow to convert a Numpy to spider
I3 = Image.fromarray(I1)
I3.save("saved_image.spi", format='SPIDER')


