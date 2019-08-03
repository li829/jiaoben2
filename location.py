import math
import numpy as np

class conpute_location():
    def convert(self, dec1, dec2, NDec1, EDec1):
        dec1 = dec1 + NDec1
        dec2 = dec2 + EDec1
        degree1 = math.floor(dec1)
        m1 = math.floor((dec1 - degree1) * 60)
        s1 = round(((dec1 - degree1) * 60 - m1) * 60, 2)
        latitude = "{}:{}:{}".format(degree1, m1, s1)
        degree2 = math.floor(dec2)
        m2 = math.floor((dec2 - degree2) * 60)
        s2 = round(((dec2 - degree2) * 60 - m2) * 60, 2)
        longitude = "{}:{}:{}".format(degree2, m2, s2)
        return latitude, longitude

    def bbox_convert(self, x, y, bbox, dx, dy, NDec1, EDec1):
        "x：裁剪图片的横坐标 y：裁剪图片的纵坐标"
        x_point = round((bbox[2] + bbox[0]) / 2)
        y_point = round((bbox[3] + bbox[1]) / 2)
        x_min = 1000 * x + bbox[0] #real xmin
        y_min = 1000 * y + bbox[1] #real ymin
        x_max = 1000 * x + bbox[2] #real xmax
        y_max = 1000 * y + bbox[3] #real ymax

        x_c = 1000 * x + x_point
        y_c = 1000 * y + y_point
        x_c_la = x_c * dx
        y_c_lo = y_c * dy
        la, lo = self.convert(x_c_la, y_c_lo, NDec1, EDec1) #latitude, longtitude
        map1 = [x_min, y_min, x_max, y_max, la, lo]
        return map1

    def generator(self, anatation_line):
        bbox_lines = anatation_line.split(" ")
        coordinate = bbox_lines[0].split('_', 1)
        x = int(coordinate[1][:2])
        y = int(coordinate[1][3:5])
        print(bbox_lines)
        box = np.array([np.array(list(map(int, box.split(',')))) for box in bbox_lines[1:]])
        return box, x, y

    def location(self):
        NDeg1 = 36
        Nm1 = 18
        Ns1 = 32.82
        EDeg1 = 120
        Em1 = 34
        Es1 = 58.76

        NDeg2 = 36
        Nm2 = 17
        Ns2 = 35.74
        EDeg2 = 120
        Em2 = 37
        Es2 = 54.72

        NDec1 = round(NDeg1 + Nm1 / 60 + Ns1 / 3600, 5)
        EDec1 = round(EDeg1 + Em1 / 60 + Es1 / 3600, 5)

        NDec2 = round(NDeg2 + Nm2 / 60 + Ns2 / 3600, 5)
        EDec2 = round(EDeg2 + Em2 / 60 + Es2 / 3600, 5)

        dy = (NDec1 - NDec2) / 19166
        dx = (EDec2 - EDec1) / 44564
        bbox_path = "test.txt"  # your path
        with open(bbox_path) as f:
            lines = f.readlines()
        N = len(lines)
        localtions = []

        for i in range(N):
            bbox, x, y =self.generator(lines[i])
            n = len(bbox)
            for j in range(n):
                map1 = self.bbox_convert(x, y, bbox[j], dx, dy, NDec1, EDec1) #map[0] = x_min #map[1]=y_min #map[2]=x_max #map[3]=y_max #map[4]=latitude #map[5]=longtitude
            #print("real_location:")
            #print("latitude:", map1[4], "\t", "longtitude", map1[5])
                localtions.append(map1)
        return localtions

a = conpute_location()
location = a.location()
print(location)
