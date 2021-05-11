import json
import os
import xml.etree.cElementTree as ET
import pandas as pd
import nibabel as nb
import numpy as np

def make_atlas_list():
    """
        Makes the package list as json file
    """
    jsondict = {}
    jsondict['Atlas'] = []
    jsondict['Maps'] = []
    jsondict['Type'] = []
    
    directories =  os.listdir()

    for name in directories:
        if name.startswith('atl-'):
            with open(name +'/atlas_description.json') as jsonfile:
                file = json.load(jsonfile)
                jsondict["Type"].append("Atlas")
                jsondict["Atlas"].append(name)
                jsondict["Maps"].append(file["Maps"])
        if name.startswith('con-'):
            with open(name +'/contrast_description.json') as jsonfile:
                file = json.load(jsonfile)
                jsondict["Type"].append("Contrast")
                jsondict["Atlas"].append(name)
                jsondict["Maps"].append(file["Maps"])
    with open('package_description.json','w') as outfile:
        json.dump(jsondict,outfile)

def rgbtxt_to_lut(filename):
    D=pd.read_csv(filename,header=None,delimiter=' ')
    L=pd.DataFrame({
            "key":D[0],
            "R":D[2]/255,
            "G":D[3]/255,
            "B":D[4]/255,
            "Name":D[1]})
    L.to_csv(filename+'.lut',header=None,delimiter=' ')

def read_all_atlasdescrip():
    """
        Reads all atlas descriptors for later parsing into website or README
        INPUT:
        OUTPUT:

    """
    descr = []
    with open('package_description.json') as jsonfile:
        file = json.load(jsonfile)
        for i,name in enumerate(file['Atlas']):
            if file['Type'][i]=='Atlas':
                with open(name +'/atlas_description.json') as jsonfile:
                    descr.append(json.load(jsonfile))
            if file['Type'][i]=='Contrast':
                with open(name +'/contrast_description.json') as jsonfile:
                    descr.append(json.load(jsonfile))
    return descr



def write_readme(descr): 
    with open('README.md','w') as out: 
        out.write("# Cerebellar Atlases\n")
        out.write("The cerebellar atlases are a collection of anatomical and functional atlases of the human cerebellum, both of parcellations and continuous maps.")
        out.write("For every maps, we provide some the following files\n" + 
        "* ..._sp-MNI.nii: volume file aligned to FNIRT MNI space\n" +
        "* ..._sp-SUIT.nii: volume file aligned to SUIT space\n" +
        "* ..._lut: Color and label lookup table for parcellations\n" + 
        "* ....gii: Data projected to surface-based representation of the cerebellum (Diedrichsen & Zotow, 2015).\n")
        out.write("The atlases can also be viewed online using out cerebellar atlas tool for quick reference!\n\n")
        for d in descr:
            out.write("### " + d["ShortDesc"] + "\n")
            out.write(d["LongDesc"] + "\n")
            for i,f in enumerate(d["Maps"]):
                out.write("* " + f + ":    " + d["MapDesc"][i] +"\n")
            out.write("\nReferences and Links:\n")
            for ref in d["ReferencesAndLinks"]: 
                out.write("* " + ref + "\n")
            out.write("\n\n")
        out.write("## Reference and Licence\n")
        out.write("The atlas collection was curated by the Jörn Diedrichsen and his lab. ")

def export_as_FSLatlas(name = None, atlas = None):
    root = ET.Element("root")
    doc = ET.SubElement(root, "doc")
    ET.SubElement(doc, "field1", name="blah").text = "some value1"
    ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

    tree = ET.ElementTree(root)
    tree.write("filename.xml")

def make_MDTB_contrasts(): 
    """
        Generates the MDTB contrasts from the atlas package with correct naming
    """
    D = pd.read_csv('../MDTB_maps/contrast_list.csv')
    for at in ['SUIT']: 
        for c in range(50):
            images = D[D.ConNo == c+1]
            num_img = images.Contrast.shape[0]
            nii = []
            dir = os.path.join('..', 'MDTB_maps', at + '_group_contrasts')
            X = []
            for i, file in enumerate(images.Filename):
                nii = nb.load(os.path.join(dir,file + '.nii'))
                X.append(nii.get_fdata())
            pass
            if num_img==2: 
                Y = (X[0]+X[1])/2
            else:
                Y = X[0]
            img = nb.Nifti1Image(Y, nii.affine)
            filename = os.path.join('con-MDTB',f'con-MDTB{images.ConNo.iloc[0]:02}{images.Contrast.iloc[0]}_sp-{at}.nii')
            img.set_data_dtype('int16')
            nb.save(img, filename)
    pass

def make_MDTB_json(): 
    """
        Generates the MDTB json file from the csv
    """
    D = pd.read_csv('con-MDTB/contrast_description.csv')
    with open('atl-MDTB/atlas_description.json') as jsonfile:
        condict = json.load(jsonfile)
        condict['Maps']=D['Contrast'].tolist()
        condict['MapDesc']=D['Description'].tolist()
        with open('con-MDTB/contrast_description_new.json','w') as outfile:
            json.dump(condict,outfile)

if __name__ == "__main__":
    # make_atlas_list()
    descr = read_all_atlasdescrip()
    write_readme(descr)
    # export_as_FSLatlas('Buckner','Buckner7')
    # rgbtxt_to_lut('atl-Xue10Sub1_desc-color.txt')
    # make_MDTB_json()
    pass 