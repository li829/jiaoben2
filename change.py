import numpy as np
path = '/home/liyuewen/data_zoom/test.txt'
save_path = '/home/liyuewen/data_zoom/res9.txt'
with open(path) as f:
    lines = f.readlines()
print(len(lines))

#print(dic['飞机'])
N = len(lines)
store = []

for i in range(N):
    line = lines[i].split(' ', 2)
    print(line)
    a = len(line)
    if a <= 2:
        with open(save_path, "a") as f:
            f.writelines(lines[i])
            f.close()
    else:
        store.append(int(line[1]))
        ind = np.argsort(store)
#print(store)
#print(ind)
        N1 = len(ind)

        for j in range(N1):
            #print(lines[ind[j]+1])
            store_line = lines[ind[j]+1].split(' ', 2)
            with open(save_path, "a") as f:
                f.writelines(str(j) + ' ' + store_line[2])
                f.close()

