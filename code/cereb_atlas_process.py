import json
import os
import xml.etree.cElementTree as ET
import pandas as pd
import nibabel as nb
import numpy as np
import SUITPy as suit
import nilearn.image as nli

def make_atlas_list(directories=['Diedrichsen_2009','Buckner_2011',
                                 'Xue_2021','Ji_2019','King_2019']):
    """
        Makes the package list as json file
    """
    jsondict = {}
    # jsondict['Atlas'] = []
    # jsondict['ShortDesc'] = []
    # jsondict['Maps'] = []
    # jsondict['MapDesc'] = []
    # jsondict['Type'] = []
    # jsondict["LongDesc"]=[]
    # jsondict["ReferencesAndLinks"]=[]
    atlases = {}
    for name in directories:
        atlas_dict = {}
        with open(f'../{name}' +'/atlas_description.json') as jsonfile:
            file = json.load(jsonfile)
            # jsondict["Atlas"].append(name)
            # jsondict["ShortDesc"].append(file["ShortDesc"])
            # jsondict["Maps"].append(file["Maps"])
            # jsondict["Type"].append(file["Type"])
            # jsondict["MapDesc"].append(file["MapDesc"])
            # jsondict["LongDesc"].append(file["LongDesc"])
            # jsondict["ReferencesAndLinks"].append(file["ReferencesAndLinks"])
            atlas_dict["ShortDesc"] = file["ShortDesc"]
            atlas_dict["Maps"] = file["Maps"]
            atlas_dict["Type"] = file["Type"]
            atlas_dict["MapDesc"] = file["MapDesc"]
            atlas_dict["ReferencesAndLinks"] = file["ReferencesAndLinks"]
        atlases[name] = atlas_dict
        jsondict["atlases"] = atlases
    with open('../package_description.json','w') as outfile:
        json.dump(jsondict,outfile,indent = 5)

def rgbtxt_to_lut(filename):
    D=pd.read_csv(filename,header=None,delimiter=' ')
    L=pd.DataFrame({
            "key":D[0],
            "R":D[2]/255,
            "G":D[3]/255,
            "B":D[4]/255,
            "Name":D[1]})
    L.to_csv(filename+'.lut',header=None,sep=' ')

def lut_to_tsv(filename):
    D=pd.read_csv(filename + '.lut',header=None,delimiter=' ')
    hexcolor = []
    for i in range(D.shape[0]):
        hexcolor.append(f"#{int(D.iloc[i,1]*255):02x}{int(D.iloc[i,2]*255):02x}{int(D.iloc[i,3]*255):02x}")
    L=pd.DataFrame({
            "index":D[0],
            "name":D[4],
            "color":hexcolor})
    L.to_csv(filename+'.tsv',index = False, sep='\t')


def write_readme():
    with open('README.md','w') as out:
        out.write("# Cerebellar Atlases\n")
        out.write("The cerebellar atlases are a collection of anatomical and functional atlases of the human cerebellum, both of parcellations and continuous maps.")
        out.write("The collection is maintained as a [Github repository](https://github.com/diedrichsenlab/cerebellar_atlases).")
        out.write("For every maps, we provide some the following files:\n" +
        "* ..._space-MNI.nii: volume file aligned to FNIRT MNI space\n" +
        "* ..._space-SUIT.nii: volume file aligned to SUIT space\n" +
        "* ....tsv: Color and label lookup table for parcellations\n" +
        "* ....gii: Data projected to surface-based representation of the cerebellum (Diedrichsen & Zotow, 2015).\n\n")
        out.write("The atlases are organized by the first author / year of the main paper\n\n")

        out.write("The maps can also be viewed online using our [cerebellar atlas viewer](https://www.diedrichsenlab.org/imaging/AtlasViewer).\n\n")
        with open('package_description.json') as jsonfile:
            file = json.load(jsonfile)
            for i,name in enumerate(file['Atlas']):
                out.write("### " + file["ShortDesc"][i] + "\n")
                out.write(file["LongDesc"][i] + "\n")
                for j,f in enumerate(file["Maps"][i]):
                    out.write("* " + f + ":    " + file["MapDesc"][i][j] +"\n")
                out.write("\nReferences and Links:\n")
                for ref in file["ReferencesAndLinks"][i]:
                    out.write("* " + ref + "\n")
                out.write("\n\n")
        out.write("## Reference and Licence\n")
        out.write("The atlas collection was curated by the Jörn Diedrichsen and his lab and distributed . ")

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
    for at in ['MNI']:
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
            filename = os.path.join('MDTB_2019',f'con-MDTB{images.ConNo.iloc[0]:02}{images.Contrast.iloc[0]}_space-{at}.nii')
            img.set_data_dtype('int16')
            nb.save(img, filename)
    pass

def preprocess_nifti(fname,isLabel=True):
    """
        Preprocesses (cleans) the nifti file by setting data type and intent
    """
    nii = nb.load(fname + '.nii')
    X = nii.get_fdata()
    img = nb.Nifti1Image(X.round(0), nii.affine)
    if isLabel:
        img.set_data_dtype('int8')
        img.header.set_intent(1002,(),"")
        img.header.set_slope_inter(1.0,0.0)
    else:
        img.set_data_dtype('int16')
    print(img.shape)
    nb.save(img, fname + '.nii')

def preprocess_all():
    preprocess_nifti('Buckner_2011/atl-Buckner7_space-MNI')
    preprocess_nifti('Buckner_2011/atl-Buckner7_space-SUIT')
    preprocess_nifti('Buckner_2011/atl-Buckner17_space-MNI')
    preprocess_nifti('Buckner_2011/atl-Buckner17_space-SUIT')
    preprocess_nifti('Ji_2019/atl-Ji10_space-MNI')
    preprocess_nifti('Ji_2019/atl-Ji10_space-SUIT')
    preprocess_nifti('Anatom/atl-Anatom_space-MNI')
    preprocess_nifti('Anatom/atl-Anatom_space-SUIT')
    preprocess_nifti('MDTB_2019/atl-MDTB10_space-MNI')
    preprocess_nifti('MDTB_2019/atl-MDTB10_space-SUIT')

def map_to_surf(fname,isLabel=True):
    """
        Maps a specific label file to the SUIT flatmap
    """
    nii_name = fname + '_space-SUIT'
    if isLabel:
        gii_name = fname + '_dseg.label.gii'
        labeldata = suit.flatmap.vol_to_surf([nii_name + '_dseg.nii'],stats = 'mode')
        lut_name = fname + '.lut'
        D=pd.read_csv(lut_name,header=None,delimiter=' ')
        RGBA = np.c_[D[1],D[2],D[3],np.ones((D.shape[0],))]
        RGBA = np.vstack([np.zeros((1,4)),RGBA])
        labels = ['None']
        labels = labels + D[4].tolist()
        L = suit.flatmap.make_label_gifti(labeldata,
            label_names=labels,column_names=['label'],label_RGBA=RGBA)
        L.darrays[0].datatype=2
    else:
        gii_name = fname + '.func.gii'
        condata = suit.flatmap.vol_to_surf([nii_name + '.nii'],stats = 'nanmean')
        L = suit.flatmap.make_func_gifti(condata)
    nb.save(L,gii_name)

def all_maps_to_surf():
    with open('package_description.json') as jsonfile:
        file = json.load(jsonfile)
        for i,atlname in enumerate(file['Atlas']):
            typ = file['Type'][i]
            for x,map in enumerate(file['Maps'][i]):
                    print(f"mapping {map}\n")
                    if typ[x]=='dseg':
                        map_to_surf(os.path.join(atlname,map),True)
                    elif typ[x]=='func':
                        pass
                        # map_to_surf(os.path.join(atlname,map),False)
    pass


def make_MDTB_json():
    """
        Generates the MDTB json file from the csv
    """
    D = pd.read_csv('MDTB_2019/atlas_description.csv')
    with open('MDTB_2019/atlas_description.json') as jsonfile:
        condict = json.load(jsonfile)
        condict['ShortDesc'] = "Multi-domain task battery (MDTB) contrast maps: King et al. (2019)"
        condict['LongDesc'] = "King et al. (2019) provided an extensive characterization of the functional organization of the cerebellum of 24 healthy, young participants. The contast are for for 47 task conditions, accounted for the activity caused by left hand, right hand, and eye movements. All maps are relative to the mean activitiy across all tasks."
        condict['MapDesc']=D['Description'].tolist()
        condict['Maps'] = []
        for i,d in D.iterrows():
            condict['Maps'].append(f'MDTB{d.ConNo:02}{d.Contrast}')
        with open('MDTB_2019/atlas_description.json','w') as outfile:
            json.dump(condict,outfile,indent = 4)

def crop_to_MNI(filesource,filenew,interp = 'continuous'):
    target = nb.load('Buckner_2011/atl-Buckner7_space-MNI.nii')
    source = nb.load(filesource)
    new_img = nli.resample_to_img(source,target,interpolation = interp)
    nb.save(new_img,filenew)
    pass

if __name__ == "__main__":
    # preprocess_all()
   # make_atlas_list()
    write_readme()
    # export_as_FSLatlas('Buckner','Buckner7')
    # rgbtxt_to_lut('atl-Xue10Sub1_desc-color.txt')
    # make_MDTB_json()
    # lut_to_tsv('Buckner_2011/atl-Buckner7')
    # lut_to_tsv('Buckner_2011/atl-Buckner17')
    # lut_to_tsv('Xue_2021/atl-Xue10Sub2')
    # lut_to_tsv('Xue_2021/atl-Xue10Sub1')
    # lut_to_tsv('Anatom/atl-Anatom')
    # lut_to_tsv('MDTB_2019/atl-MDTB10')
    # lut_to_tsv('Ji_2010/atl-Ji10')

    # all_maps_to_surf()
    # make_MDTB_contrasts()
    # map_to_surf('MDTB_2019/atl-MDTB10',isLabel = True)
    # crop_to_MNI('Xue_2021/atl-Xue10Sub1.nii','atl-Xue/atl-Xue10Sub1_space-MNI.nii',interp='nearest')
    # crop_to_MNI('Xue_2021/atl-Xue10Sub2.nii','atl-Xue/atl-Xue10Sub2_space-MNI.nii',interp='nearest')
    # preprocess_nifti('Xue_2021/atl-Xue10Sub1_space-MNI')
    # preprocess_nifti('Xue_2021/atl-Xue10Sub2_space-MNI')
    pass