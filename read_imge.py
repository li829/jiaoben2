from skimage import io
import numpy as np
import os
from PIL import Image
from matplotlib import pyplot as plt


save_dir = '/home/liyuewen/PycharmProjects/images/TDOM-1_Group0_resize'
img_path1 = '/home/liyuewen/data_zoom/5th/5th_resize_2_2_ppm/5th_Result_1_0_00_00.ppm'#'
img_path2 = '/home/liyuewen/data_zoom/VOCdevkit/VOC2012/JPEGImages/2008_000001.jpg'
#imgs = os.listdir(imgdir) #str img's name
#print(imgs)
#N = len(imgs)
#print("total images:", N)
image = Image.open(img_path2)
print(np.shape(image))
#image.show(image)
print(image.size)
plt.imshow(image)
plt.show()

