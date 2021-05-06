# Cerebellar Atlases
The cerebellar atlases are a collection of anatomical and functional atlases of the human cerebellum, both of parcellations and continuous maps.The atlases are provided as NIFTI-volumes aligned to FNIRT MNI space (FNIRT) or SUIT, as well as gifti-files maps for viewing on the surface-based representation of the cerebellum (Diedrichsen & Zotow, 2015).
The atlases can also be viewed online using out cerebellar atlas tool for quick reference!

### Probabilistic atlas for cerebellar lobules and nuclei: Diedrichsen (2009)
The anatomical definitions are based on the fMRI atlas of an individual cerebellum by Schmahmann et al. (2000). We manually identified the main lobules on MRI scans of 20 healthy young participants (ROIs 1-28). Using a different set of 23 participants, we also identified the deep cerebellar nuclei (ROIs 29-34).
* atl-Anatom_sp-SUIT.nii:    Number of most probable compartment
* atl-Anatom.nii.lut:    Assignment of compartment numbers to lobules
* atl-Anatom_sp-SUIT_desc-prob.nii:    Full probability maps for each of the compartments
* atl-Anatom_sp-SUIT_desc-maxprob.nii:    Probability of the compartment with the highest probability

References and Links:
* Diedrichsen, J., Balsters, J. H., Flavell, J., Cussans, E., & Ramnani, N. (2009). A probabilistic atlas of the human cerebellum. Neuroimage.
* Diedrichsen, J., Maderwald, S., Kuper, M., Thurling, M., Rabe, K., Gizewski, E. R., et al. (2011). Imaging the deep cerebellar nuclei: A probabilistic atlas and normalization procedure. Neuroimage.
* http://www.diedrichsenlab.org/imaging/propatlas.htm


### Resting state network partcellation: Buckner et al. (2011)
Buckner et al. (2011) presented the first comprehensive functional atlas of the human cerebellum, based on the correlation of each cerebellar voxel and with the 7 ot 15 cortical resting state networks, described in Yeo et al. Parcellation is based on the data from 1000 subjects. 
* atl-Buckner7_sp-SUIT.nii:    Assignment of cerebellar voxels to the 7 network parcellation in SUIT space
* atl-Buckner7_sp-SUIT_desc-confid.nii:    Confidence of the assignment to the 7 networks in SUIT space [0-1]
* atl-Buckner17_sp-SUIT.nii:    Assignment of cerebellar voxels to the 7 network parcellation in SUIT space
* atl-Buckner17_sp-SUIT_desc-confid.nii:    Confidence of the assignment to the 7 networks in SUIT space [0-1]

References and Links:
* Buckner, R. L., Krienen, F. M., Castellanos, A., Diaz, J. C. & Yeo, B. T. (2011). The organization of the human cerebellum estimated by intrinsic functional connectivity. J Neurophysiol 106, 2322–2345.


### Individual resting state parcellation: Xue et al. (2020)
Xue et al. (2020) provided two individual parcellations based on resting state data from 31 sessions.  daya  of the functional organization of the cerebellum, by collecting data from 47 task conditions in 24 healthy, young participants. Based on the the task data, a parcellation of the cerebellum in 7, 10, or 17 regions was supplied.
* atl-MDTB10_sp-SUIT.nii:    MDTB 10 region parcellation in SUIT space
* atl-MDTB10_desc-color.txt:    Color and region name information

References and Links:
* Xue, A., Kong, R., Yang, Q., Eldaief, M. C., Angeli, P. A., Dinicola, L. M., … Yeo, B. T. T. (2021). The detailed organization of the human cerebellum estimated by intrinsic functional connectivity within the individual. https://doi.org/10.1152/jn.00561.2020


### Subcortical restingstate parcellation: Ji et al. (2019)
Ji et al. (2019) presented a parcellation of subcortical structures based on correlation with 10 cortical networks, based on the HCP resting state data.
* atl-Ji10_sp-SUIT.nii:    Assignment of cerebellar voxels to the 7 network parcellation in SUIT space
* atl-Ji10_sp-SUIT_desc-confid.nii:    Confidence of the assignment to the 7 networks in SUIT space [0-1]

References and Links:
* Buckner, R. L., Krienen, F. M., Castellanos, A., Diaz, J. C. & Yeo, B. T. (2011). The organization of the human cerebellum estimated by intrinsic functional connectivity. J Neurophysiol 106, 2322–2345.


### Multi-domain task battery (MDTB) parcellation: King et al. (2019)
King et al. (2019) provided an extensive characterization of the functional organization of the cerebellum, by collecting data from 47 task conditions in 24 healthy, young participants. Based on the the task data, a parcellation of the cerebellum in 7, 10, or 17 regions was supplied.
* atl-MDTB10_sp-SUIT.nii:    MDTB 10 region parcellation in SUIT space
* atl-MDTB10_desc-color.txt:    Color and region name information

References and Links:
* King, M., Hernandez-Castillo, C.R., Poldrack, R.R., Ivry, R., and Diedrichsen, J. (2019). Functional Boundaries in the Human Cerebellum revealed by a Multi-Domain Task Battery. Nat. Neurosci.


## Reference and Licence
The atlas collection was curated by the Jörn Diedrichsen and his lab. 