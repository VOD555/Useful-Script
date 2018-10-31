import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn.apionly as sns

APO_cytobb = np.loadtxt('APO/cytobb.xvg')
APO_cytoca = np.loadtxt('APO/cytoca.xvg')
APO_transbb = np.loadtxt('APO/transbb.xvg')
APO_transca = np.loadtxt('APO/transca.xvg')

HOLO_cytobb = np.loadtxt('HOLO/cytobb.xvg')
HOLO_cytoca = np.loadtxt('HOLO/cytoca.xvg')
HOLO_transbb = np.loadtxt('HOLO/transbb.xvg')
HOLO_transca = np.loadtxt('HOLO/transca.xvg')

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(1, 1, 1)
ax.plot(APO_cytobb[:,0]/1000, APO_cytobb[:,1] ,linestyle='-', color = 'blue',label='APO beckbone')
ax.plot(APO_transbb[:,0]/1000, APO_transbb[:,1] ,linestyle='-', color = 'blue',label='APO beckbone')

ax.plot(HOLO_cytobb[:,0]/1000, HOLO_cytoca[:,1] ,linestyle='-', color = 'red',label='HOLO beckbone')
ax.plot(HOLO_transbb[:,0]/1000, HOLO_transbb[:,1] ,linestyle='-', color = 'red',label='HOLO beckbone')

sns.despine(offset=10, ax=ax)

ax.set_xlabel(r"time  $t$ (ns)")
ax.legend(loc='best')

ax.set_ylabel(r"RMSD (nm)")
ax.set_title('Transmembrane domain')

plt.tight_layout()

fig.savefig('transbb.png')
