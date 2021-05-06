import json
import os
import xml.etree.cElementTree as ET
import pandas as pd

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
        if name.startswith('fun-'):
            with open(name +'/contrast_description.json') as jsonfile:
                file = json.load(jsonfile)
                jsondict["Type"].append("Functional")
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
                with open('atl-' + name +'/atlas_description.json') as jsonfile:
                    descr.append(json.load(jsonfile))
            if file['Type'][i]=='Functional':
                with open('atl-' + name +'/contrast_description.json') as jsonfile:
                    descr.append(json.load(jsonfile))
    return descr



def write_readme(descr): 
    with open('README.md','w') as out: 
        out.write("# Cerebellar Atlases\n")
        out.write("The cerebellar atlases are a collection of anatomical and functional atlases of the human cerebellum, both of parcellations and continuous maps.")
        out.write("The atlases are provided as NIFTI-volumes aligned to FNIRT MNI space (FNIRT) or SUIT, as well as gifti-files maps for viewing on the surface-based representation of the cerebellum (Diedrichsen & Zotow, 2015).\n")
        out.write("The atlases can also be viewed online using out cerebellar atlas tool for quick reference!\n\n")
        for d in descr:
            out.write("### " + d["ShortDesc"] + "\n")
            out.write(d["LongDesc"] + "\n")
            for i,f in enumerate(d["Files"]):
                out.write("* " + f + ":    " + d["FileDescr"][i] +"\n")
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


if __name__ == "__main__":
    # make_atlas_list()
    # descr = read_all_atlasdescrip()
    # write_readme(descr)
    # export_as_FSLatlas('Buckner','Buckner7')
    rgbtxt_to_lut('atl-Xue10Sub1_desc-color.txt')
    pass 