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

%% Test_3: Deform MNISym into MNI
[Def,mat]=spmdefs_get_def('../tpl-MNI152NLin6AsymC/tpl-MNI152NLin6AsymC_from-MNI152NLin2009cSymC_mode-image_xfm.nii');
fname = '../tpl-MNI152NLin2009cSymC/tpl-MNI152NLin2009cSymC_T1w.nii';
ofname = '../tpl-MNI152NLin6AsymC/MNISym_into-MNI.nii';
spmdefs_apply_def(Def,mat,fname,1,ofname);

%% Example 1: Deform a discrete segmentation file using nearest neighbor interpolation
[Def,mat]=spmdefs_get_def('../tpl-MNI152NLin2009cSymC/tpl-MNI152NLin2009cSymC_from-SUIT_mode-image_xfm.nii');
fname = '../Diedrichsen_2009/atl-Anatom_space-SUIT_dseg.nii';
ofname = '../Diedrichsen_2009/atl-Anatom_space-MNISym_dir_dseg.nii';
spmdefs_apply_def(Def,mat,fname,0,ofname);

%% Example 2: Deform a probabilistic segementation using trilinear interpolation
% then do winner-take-all assignment
[Def,mat]=spmdefs_get_def('../tpl-MNI152NLin2009cSymC/tpl-MNI152NLin2009cSymC_from-SUIT_mode-image_xfm.nii');
fname = '../Diedrichsen_2009/atl-Anatom_space-SUIT_pseg.nii';
ofname = '../Diedrichsen_2009/atl-Anatom_space-MNISym_pseg.nii';
dfname = '../Diedrichsen_2009/atl-Anatom_space-MNISym_dseg.nii';

spmdefs_apply_def(Def,mat,fname,1,ofname);
V=spm_vol(ofname);
X=spm_read_vols(V);
% X=(X + flipdim(X,1))/2; 
for i=1:length(V)
    spm_write_vol(V(i),X(:,:,:,i));
end; 
[x,win] = max(X,[],4);
xs = sum(X,4);
win(xs<0.3)=0; 
Vo = struct('fname',dfname,...
                'dim',[size(Def{1},1) size(Def{1},2) size(Def{1},3)],...
                'dt',[2 0],...
                'pinfo',[1 0 0]',...
                'mat',V(1).mat,...
                'n',[1 1],...
                'descrip','label');
spm_write_vol(Vo,win);