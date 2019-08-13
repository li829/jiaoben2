import numpy as np
from skimage.measure import find_contours
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines
from matplotlib.patches import Polygon
import os
from skimage import io
import math
#imgdir = '/home/liyuewen/PycharmProjects/images/001'
#imgs = os.listdir(imgdir) #str img's name
imgs = '/home/liyuewen/PycharmProjects/jiaoben/test_9th_194.ppm'
#N = len(imgs)
#print("total images:", N)
image = plt.imread(imgs)
print(image.shape)
#io.imshow(image)
#plt.show()
image = image[:, :]
image = image.astype(np.uint8)
#io.imshow(image)
#plt.show()

path = '/home/liyuewen/PycharmProjects/jiaoben/194.txt'
with open(path) as f:
    lines = f.readlines()
print(len(lines))
N = len(lines)
color = (0, 0, 255)#bgr
image = image.copy()
figsize=(16, 16)
_, ax = plt.subplots(1, figsize=figsize)
height, width = image.shape[:2]
ax.set_ylim(height + 10, -10)
ax.set_xlim(-10, width + 10)
ax.axis('off')
dic = {'飞机': 'plane', '储蓄罐':'can', '桥梁':'bridge', '操场':'ground', '船只':'ship', '码头':'dock'}
for i in range(N):
    line = lines[i].split(' ', 4)
    print(line)
    a = line[3].split(',', 1)
    x_min = a[0][1:]
    S = len(a[1])
    y_min = a[1][:S-1]

    b = line[4].split(',', 1)
    x_max = b[0][1:]
    s = len(b[1])
    y_max = b[1][: s-2]
    print(x_min, y_min, x_max, y_max)

    x1 = round(float(x_min))
    y1 = 4096 - round(float(y_max))
    x2 = round(float(x_max))
    y2 = 4096 - round(float(y_min))

    p = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=1,
                          alpha=0.7, linestyle="-",
                          edgecolor=(0, 1, 0), facecolor='none')
    ax.add_patch(p)
    print(line[1])
    x = np.random.randint(x1, (x1 + x2) // 2)
    caption = "{}".format(dic[line[1]])
    ax.text(x1, y1 + 8, caption,
            color='w', size=12, backgroundcolor="none")
ax.imshow(image)
plt.show()
"""
lo = location.conpute_location()
location = lo.location()
print(location)
n, _ =np.shape(location)
color = (0, 0, 255)#bgr
image = image.copy()
figsize=(16, 16)
_, ax = plt.subplots(1, figsize=figsize)
height, width = image.shape[:2]
ax.set_ylim(height + 10, -10)
ax.set_xlim(-10, width + 10)
ax.axis('off')
for i in range(n):
    x1, y1, x2, y2 = location[i][:4]
    p = patches.Rectangle((x1, y1), x2 - x1, y2 - y1, linewidth=1,
                          alpha=0.7, linestyle="-",
                          edgecolor=(0, 1, 0), facecolor='none')
    ax.add_patch(p)

    # x = random.randint(x1, (x1 + x2) // 2)
    caption = "{} {}".format(location[i][4], location[i][5])
    ax.text(x1, y1 + 8, caption,
            color='w', size=11, backgroundcolor="none")
ax.imshow(image)
plt.show()
"""
