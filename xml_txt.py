import xml.etree.ElementTree as ET
import numpy as np
import os

def loadimagepath(img_dir, annatation_path):
    tree = ET.parse(annatation_path)
    image_name = tree.find('filename')
    img_path = image_name.text
    path = img_dir + "/" + img_path
    return path

def loadbbox(annatation_path, img_dir):
    ann = os.listdir(annatation_path)
    N = len(ann)
    dic = {'plane':'0', 'can':'1', 'bridge':'2', 'ground':'3', 'dock':'4', 'ship':'5'}
    for i in range(N):
        ann_path = annatation_path + "/" + ann[i]
        tree = ET.parse(ann_path)
        objs = tree.findall('object')
        num_objs = len(objs)

        boxes = np.zeros((num_objs, 4), dtype=np.uint16)


        for ix, obj in enumerate(objs):
            bbox = obj.find('bndbox')
            x1 = float(bbox.find('xmin').text) - 1
            y1 = float(bbox.find('ymin').text) - 1
            x2 = float(bbox.find('xmax').text) - 1
            y2 = float(bbox.find('ymax').text) - 1
            id = str(obj.find('name').text)
            boxes[ix, :] = [x1, y1, x2, y2]
        n, _ = np.shape(boxes)
        print(boxes.shape)
        bbox_str = ""
        for j in range(n):
            bbox_str += "{},{},{},{},{} ".format(boxes[j,0], boxes[j, 1], boxes[j,2], boxes[j,3], dic[id])
        image_path = loadimagepath(img_dir, ann_path)
        print(image_path,"\n", bbox_str)
        with open('train1.txt', 'r+') as f:
            content = f.read()
            f.seek(0,0)
            f.write(image_path + " " + bbox_str + "\n" + content)

annatation_path="/home/liyuewen/data_zoom/5th/5th_annotation"
img_dir="/home/liyuewen/data_zoom/5th/5th_resize_2_2_ppm"
loadbbox(annatation_path, img_dir)