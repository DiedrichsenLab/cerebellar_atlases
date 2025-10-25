# Cerebellar Atlases
The cerebellar atlases are a collection of anatomical and functional atlases of the human cerebellum, both of parcellations and continuous maps. The collection is maintained as a [Github repository](https://github.com/diedrichsenlab/cerebellar_atlases).

## Template spaces
We are providing the atlas and data maps in three template spaces. All three templates are provided in the `tpl-` directory in a cerebellar-only version.
* MNI152NLin6AsymC: The non-linear asymmetric MNI template used for example in FSL (short MNI)
* MNI152NLin2009cSymC: The 2000c symmetric MNI template (short MNISym)
* SUIT: The original cerebellar-only template (Diedrichsen, 2005)

For every template space, we provide the following files:
* .._T1w: T1-weighted template image
* .._desc-pcereb.nii: Probabilistic mask
* .._desc-cereb_mask.nii: hard mask
* .._xfm.nii: Transform files between different atlas spaces
* ..label-GMc_probseg.nii: Gray matter probability
* ..label-WMc_probseg.nii: White matter probability

## Atlases
For every maps, we provide some the following files:
* ..._space-MNI.nii: volume file aligned to MNI152NLin6AsymC
* ..._space-MNISym.nii: volume file aligned to MNI152NLin2009cSymC
* ..._space-SUIT.nii: volume file aligned to SUIT space
* ...tsv: Color and label lookup table for parcellation
* ...lut: Color and label lookup table for FSLeyes
* ....gii: Data projected to surface-based representation of the cerebellum (Diedrichsen & Zotow, 2015).

The atlases are organized by the first author / year of the main paper

The maps can also be viewed online using our [cerebellar atlas viewer](https://www.diedrichsenlab.org/imaging/AtlasViewer).

