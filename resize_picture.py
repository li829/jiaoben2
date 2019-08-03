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
flag = 0

for i in range(0, N):

    img = imgs[i]
    name = imgs[i][:8]
    print(name)
    img = plt.imread(imgdir+"/"+imgs[i])
    img = np.rot90(img)
    h, w, _= np.shape(img)
    resize_img = np.empty((24, 1000, 1000, 3), np.uint8)
    print(i)
    s = 0
    a = 0
    flag = 0
    if h == 6000:
        for j in range(0, 24):
            if flag:
                a = a + 1
                flag = 0
            if s >= 6:
                s = 0
            resize_img[j, :, :, :] = img[s*1000:s*1000+1000, a*1000:a*1000+1000, :]
            if j < 9:
                path = save_dir + "/" + name + '0{}.JPG'.format(j+1)
            else:
                path = save_dir + "/" + name + '{}.JPG'.format(j+1)
            print(path)
            io.imsave(path, resize_img[j])
            s = s + 1
            if s == 6:
                flag = 1

