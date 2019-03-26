import numpy as np
import matplotlib.pyplot as plt
import seaborn.apionly as sns

a = np.loadtxt('benchmark.dat')

total = a[:,1]
universe = a[:,2]
prepare = a[:,3]
IO = np.loadtxt('io.dat')
compute = np.loadtxt('compute.dat')
conclude = a[:,6]

ind = np.arange(len(total))+1
width = 0.35
n = 0
Dom_com = np.zeros(16)
Dom_IO = np.zeros(16)
stop = len(IO[1,:])-1
for i in range(16):
    n_frames = len(IO[1,:])
    n_blocks = i+1
    bsize = int(np.ceil(n_frames / float(n_blocks)))
    print(bsize)
    ith_IO = np.zeros(i+1)
    ith_com = np.zeros(i+1)
    for j in range(i+1):
        jth_IO = IO[i, (bsize*j):min(stop, (j+1)*bsize)]
        jth_com = compute[i,(bsize*j):min(stop, (j+1)*bsize)]
        ith_IO[j] = np.sum(jth_IO)
        ith_com[j] = np.sum(jth_com)

    ith_Dom = ith_IO+ith_com
    n = np.argmax(ith_Dom)
    Dom_com[i] = ith_com[n]
    Dom_IO[i] = ith_IO[n]

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(1,1,1)
sns.despine(offset=10, ax=ax)
rects1 = ax.bar(ind - width/2, total, width, color='SkyBlue', label='total')
rects2 = ax.bar(ind + width/2, universe, width, color='m', label='universe')
rects3 = ax.bar(ind + width/2, prepare, width, color='g', bottom=universe, label='prepare')
rects4 = ax.bar(ind + width/2, Dom_IO, width, color='navy', bottom=universe+prepare, label='IO')
rects5 = ax.bar(ind + width/2, Dom_com, width, color='r', bottom=universe+prepare+Dom_IO, label='compute')
rects6 = ax.bar(ind + width/2, conclude, width, color='darkorange', bottom=universe+prepare+Dom_IO+Dom_com, label='conclude')
ax.legend(bbox_to_anchor=(0.5, 1.05), loc='upper center', ncol=3, edgecolor=None)
plt.xlabel('Number of processors')
plt.ylabel('Time(s)')

plt.tight_layout()
plt.savefig('bcmk.png')
