import MDAnalysis as mda
from MDAnalysis.analysis.rdf import InterRDF_s
import numpy as np

u = mda.Universe('step6.6.part0001.gro','step7_1000ns_dt_500_center.xtc')

Zn1 = u.select_atoms('name ZND and resid 24905')
Zn2 = u.select_atoms('name ZND and resid 24900')
Zn3 = u.select_atoms('name ZND')

Bsites1 = u.select_atoms('((name O* and resname ASP) or (name N* and resname HSD)) and around 4.0 (name ZND and resid 24905)')
Bsites2 = u.select_atoms('((name O* and resname ASP) or (name N* and resname HSD)) and around 4.0 (name ZND and resid 24900)')

ags = [[Zn1 ,Bsites1], [Zn2 ,Bsites2]]

rdf = InterRDF_s(u, ags, nbins = 200, range=(1.0, 4.0), density=False)
rdf.run()
rdf.get_cdf()

np.savetxt('bins.dat', rdf.bins)
np.save('rdf', rdf.rdf)
np.save('indices', rdf.indices)
np.save('cdf', rdf.cdf)

