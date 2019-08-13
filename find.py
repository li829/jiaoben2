import xml.etree.ElementTree as ET
import numpy as np
import os
annotation_path = "/home/liyuewen/data_zoom/5th/5th_annotation/5th_Result_2_0_00_00.xml"
tree = ET.parse(annotation_path)
image_name = tree.find('object')
for i in image_name:
    img_path = image_name.find('name')
    print(img_path.text)