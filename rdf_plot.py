import matplotlib
import matplotlib.pyplot as plt
import MDAnalysis as mda
import numpy as np

u = mda.Universe('Nw_Center.gro')
for i in range(289,297):
    name = 'ZNM'+str(i)
    bins = np.loadtxt('bins.dat')
    indices = np.loadtxt(name+'indices.dat')
    rdf = np.loadtxt(name+'_rdf.dat')
    cdf = np.loadtxt(name+'_cdf.dat')

    fig = plt.figure(figsize=(14,5))
    ax = fig.add_subplot(121)
    bx = fig.add_subplot(122)
    colors = ['b', 'g', 'r', 'c', 'y', 'm']

    for n in range(len(indices)):
        atom = u.atoms[int(indices[n])]
        index = atom.resname+str(atom.resid)+atom.name
        ax.plot(bins, rdf[n,:], linestyle = '-', color = colors[n], label = index)
        bx.plot(bins, cdf[n,:], linestyle = '-', color = colors[n], label = index)
    ax.legend(loc='best')
    ax.set_xlabel(r"Distance ($\AA$)")
    ax.set_ylabel(r"RDF")
    ax.set_title('RDF')
    bx.legend(loc='best')
    bx.set_xlabel(r"Distance ($\AA$)")
    bx.set_ylabel(r"CDF")
    bx.set_title('CDF')
    fig.savefig(str(i)+"RDF&CDF.png")
    fig.clf()
