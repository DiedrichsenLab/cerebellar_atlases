% Instructional script of how to use the deformation to move the 
% cerebellar atlasses between different atlas spaces using matlab. 
% requirements: SPM12 
% - SUIT (github.com/jdiedrichsen/suit) 
% - spmdefs (github.com/DiedrichsenLab/spmdefs) 
%% Test 1: Deform MNISym into SUIT 
[Def,mat]=spmdefs_get_def('../tpl-SUIT/tpl-SUIT_from-MNI152NLin2009cSymC_mode-image_xfm.nii');
fname = '../tpl-MNI152NLin2009cSymC/tpl-MNI152NLin2009cSymC_T1w.nii';
ofname = '../tpl-SUIT/MNISym_into-SUIT.nii';
spmdefs_apply_def(Def,mat,fname,1,ofname);

%% Test_2: Deform SUIT into MNISym 
[Def,mat]=spmdefs_get_def('../tpl-MNI152NLin2009cSymC/tpl-MNI152NLin2009cSymC_from-SUIT_mode-image_xfm.nii');
fname = '../tpl-SUIT/tpl-SUIT_res-1_T1w.nii';
ofname = '../tpl-MNI152NLin2009cSymC/SUIT_into-MNISym.nii';
spmdefs_apply_def(Def,mat,fname,1,ofname);

%% Example 1: Deform a discrete segmentation file using nearest neighbor interpolation
[Def,mat]=spmdefs_get_def('../tpl-MNI152NLin2009cSymC/tpl-MNI152NLin2009cSymC_from-SUIT_mode-image_xfm.nii');
fname = '../atl-Diedrichsen2009/tpl-SUIT_res-1_T1w.nii';
ofname = '../atl-Diedrichsen2009/SUIT_into-MNISym.nii';
spmdefs_apply_def(Def,mat,fname,1,ofname);
