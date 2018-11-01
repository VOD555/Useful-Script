import MDAnalysis as mda
import numpy as np
import matplotlib.pyplot as plt
import seaborn.apionly as sns

u = mda.Universe('step6.6.part0001.gro')
bins = np.loadtxt('bins.dat')
rdf = np.load('rdf.npy') 
cdf = np.load('cdf.npy')
indices = np.load('indices.npy')


for i in range(len(indices)):
# select a pair of atom groups
    for j in range(len(indices[i][0])):
    # select an atom in group1
        siteA = u.atoms[indices[i][0][j]]
        fig = plt.figure(figsize=(6,4))
        title = '{}{}'.format(siteA.name, siteA.resname, siteA.resid)
        ax = fig.add_subplot(1,1,1, title=title)
        for k in range(len(indices[i][1])):
        # select an atom in group2
            siteB = u.atoms[indices[i][1][k]]
            rdf_AB = rdf[i][j][k]
            cdf_AB = cdf[i][j][k]
            if cdf_AB[-1] != 0:
                label = '{} of {}{}'.format(siteB.name, siteB.resname, siteB.resid)
                ax.plot(bins, rdf_AB, label=label, linestyle = '--')
        ax.legend(loc='best')
        ax.set_ylabel('RDF')
        ax.set_xlabel(r"Distance ($\AA$)")
        sns.despine(offset=10, ax=ax)
        plt.tight_layout()
        fig.savefig("resid{}.png".format(siteA.resid))
        fig.clf()
