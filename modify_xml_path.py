import os
import re

# 设置为自己Annotations保存路径
_dir = "/home/liyuewen/PycharmProjects/tf-faster-rcnn-master/data/VOCdevkit2007/VOC2007/Annotations/"
xmlList = os.listdir(_dir)
n = 1
a = 0
for xml in xmlList:
    try:
    # f = open(_dir + xml, "r")
        f = open(_dir + xml, "r", encoding='utf-8')
        xmldata = f.read()
    # 设置为希望修改的path即可

        xmldata = re.sub('\<path>(.*?)\</path>',
                         '<path>/home/liyuewen/PycharmProjects/tf-faster-rcnn-master/data/VOC2012/JPEGImages/' + xml.split('.')[0] + '.ppm</path>', xmldata)
        f.close()
        f = open(_dir + xml, "w")
        f.write(xmldata)
        f.close()
        n += 1
        print(str(n).zfill(6))
    except:
        a = a+1
print(a)