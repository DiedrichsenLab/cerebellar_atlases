### Atlas spaces 

SUIT: 
size: 141 x 95 x  87

MNI: tpl-MNI152NLin6AsymC
size: 153 x 103 x 84

MNISym: tpl-MNI152NLin2009cSymC
size: 153 x 100 x  79


### Data formats: 

|H | spm_type | nibabel | FSLeyes |
|--|-----------------|------------|-------------|
|2 |  uint8	 | unit8 | uint8|
|4 | int16  | <i2 | int16|
|8  | int32  | <i4 | int32|
|16| float32 | <f4 | Float32|
|64| float 64 | <f8 | Double64|
|256 | int8 | int8 |int8|
|512| uint16 |  <u2 | uint16 |
|762 | unit32 | <u4 |unit32|


### Making the deformations: 
Deformations are based on SUIT-normalization of the atlas template into suit space. 
The process is stored under: 

``Dropbox(Diedrichsenlab)/projects/AtlasTemplates/MNI152NLin2009cSymC`` and ``MNI152NLin6AsymC``. 

