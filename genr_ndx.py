import MDAnalysis as mda
u = mda.Universe('step5_znm.pdb')

helixB1 = u.select_atoms('resid 9-37 and segid PROB') 
helixB2 = u.select_atoms('resid 38-66 and segid PROB')
helixB3 = u.select_atoms('resid 79-109 and segid PROB')
helixB4 = u.select_atoms('resid 115-142 and segid PROB')
helixB5 = u.select_atoms('resid 149-174 and segid PROB')
helixB6 = u.select_atoms('resid 178-208 and segid PROB')
helixB7 = u.select_atoms('resid 213-226 and segid PROB')
helixB8 = u.select_atoms('resid 258-227 and segid PROB')
sheetB1 = u.select_atoms('resid 232-241 and segid PROB')
sheetB2 = u.select_atoms('resid 244-252 and segid PROB')
sheetB3 = u.select_atoms('resid 280-287 and segid PROB')      

helixA1 = u.select_atoms('resid 9-37 and segid PROA') 
helixA2 = u.select_atoms('resid 38-66 and segid PROA')
helixA3 = u.select_atoms('resid 79-109 and segid PROA')
helixA4 = u.select_atoms('resid 115-142 and segid PROA')
helixA5 = u.select_atoms('resid 149-174 and segid PROA')
helixA6 = u.select_atoms('resid 178-208 and segid PROA')
helixA7 = u.select_atoms('resid 213-226 and segid PROA')
helixA8 = u.select_atoms('resid 258-227 and segid PROA')
sheetA1 = u.select_atoms('resid 232-241 and segid PROA')
sheetA2 = u.select_atoms('resid 244-252 and segid PROA')
sheetA3 = u.select_atoms('resid 280-287 and segid PROA') 

transmem = u.select_atoms('resid 7-208')
cytosolic = u.select_atoms('resid 209-288')
with mda.selections.gromacs.SelectionWriter('2nd_structure.ndx', mode='a') as ndx:
    ndx.write(helixB1, name='helixB1')
    ndx.write(helixB2, name='helixB2')
    ndx.write(helixB3, name='helixB3')
    ndx.write(helixB4, name='helixB4')
    ndx.write(helixB5, name='helixB5')
    ndx.write(helixB6, name='helixB6')
    ndx.write(helixB7, name='helixB7')
    ndx.write(helixB8, name='helixB8')
    ndx.write(sheetB1, name='sheetB1')
    ndx.write(sheetB2, name='sheetB2')
    ndx.write(sheetB2, name='sheetB3')
    ndx.write(helixA1, name='helixA1')
    ndx.write(helixA2, name='helixA2')
    ndx.write(helixA3, name='helixA3')
    ndx.write(helixA4, name='helixA4')
    ndx.write(helixA5, name='helixA5')
    ndx.write(helixA6, name='helixA6')
    ndx.write(helixA7, name='helixA7')
    ndx.write(helixA8, name='helixA8')
    ndx.write(sheetA1, name='sheetA1')
    ndx.write(sheetA2, name='sheetA2')
    ndx.write(sheetA3, name='sheetA3')

    ndx.write(transmem, name='transmem')
    ndx.write(cytosolic, name='cytosolic')
