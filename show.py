import numpy as np
from skimage.measure import find_contours
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines
from matplotlib.patches import Polygon
import IPython.display
import cv2
import os
import location
imgdir = '/home/liyuewen/PycharmProjects/images/001'
imgs = os.listdir(imgdir) #str img's name
N = len(imgs)
print("total images:", N)
image = plt.imread(imgdir+"/"+imgs[0])
image = image[:13000, :24000, :3]
image = image.astype(np.uint8)
#io.imshow(image)
#plt.show()
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
caption = "111"
caption1 = "111"
cv2.rectangle(image, (100, 100), (5000, 5000), color, thickness=4)
#cv2.putText(image, caption + caption1, (90, 90),  cv2.FONT_HERSHEY_COMPLEX, 1, color=(0, 255,), thickness=2, )
plt.imshow(image)
plt.show()
"""
