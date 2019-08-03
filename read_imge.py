from skimage import io
import numpy as np
import os

from matplotlib import pyplot as plt


save_dir = '/home/liyuewen/PycharmProjects/images/TDOM-1_Group0_resize'
imgdir = '/home/liyuewen/PycharmProjects/images/TDOM-1_Group0'
imgs = os.listdir(imgdir) #str img's name
print(imgs)
N = len(imgs)
print("total images:", N)
image = plt.imread(imgdir+"/"+imgs[0])
io.imshow(image)

