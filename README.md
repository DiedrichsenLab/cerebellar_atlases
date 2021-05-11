# Cerebellar Atlases
The cerebellar atlases are a collection of anatomical and functional atlases of the human cerebellum, both of parcellations and continuous maps.For every maps, we provide some the following files
* ..._sp-MNI.nii: volume file aligned to FNIRT MNI space
* ..._sp-SUIT.nii: volume file aligned to SUIT space
* ..._lut: Color and label lookup table for parcellations
* ....gii: Data projected to surface-based representation of the cerebellum (Diedrichsen & Zotow, 2015).
The atlases can also be viewed online using out cerebellar atlas tool for quick reference!

### Probabilistic atlas for cerebellar lobules and nuclei: Diedrichsen (2009)
The anatomical definitions are based on the fMRI atlas of an individual cerebellum by Schmahmann et al. (2000). We manually identified the main lobules on MRI scans of 20 healthy young participants (ROIs 1-28). Using a different set of 23 participants, we also identified the deep cerebellar nuclei (ROIs 29-34).
* Anatom:    Number of most probable compartment, Lobules and Nuclei
* Anatom_desc-confid:    Probability of most probable department

References and Links:
* Diedrichsen, J., Balsters, J. H., Flavell, J., Cussans, E., & Ramnani, N. (2009). A probabilistic atlas of the human cerebellum. Neuroimage.
* Diedrichsen, J., Maderwald, S., Kuper, M., Thurling, M., Rabe, K., Gizewski, E. R., et al. (2011). Imaging the deep cerebellar nuclei: A probabilistic atlas and normalization procedure. Neuroimage.
* http://www.diedrichsenlab.org/imaging/propatlas.htm


### Resting state network partcellation: Buckner et al. (2011)
Buckner et al. (2011) presented the first comprehensive functional atlas of the human cerebellum, based on the correlation of each cerebellar voxel and with the 7 or 17 cortical resting state networks, described in Yeo et al. Parcellation is based on the data from 1000 subjects. 
* Buckner7:    Assignment of cerebellar voxels to the 7 network parcellation
* Buckner17:    Assignment of cerebellar voxels to the 17 network parcellation

References and Links:
* Buckner, R. L., Krienen, F. M., Castellanos, A., Diaz, J. C. & Yeo, B. T. (2011). The organization of the human cerebellum estimated by intrinsic functional connectivity. J Neurophysiol 106, 2322–2345.


### Individual resting state parcellation: Xue et al. (2020)
Xue et al. (2020) provided two individual parcellations based on resting state data from 31 sessions for each. 10 Cortical networks were estimated using a hierarchical Bayesian model (Kong et al. 2019) and the cerebellum labeled based on the highest correlation with these networks.
* Xue10Sub1:    Individual parcellation for subject 1
* Xue10Sub2:    Individual parcellation for subject 2

References and Links:
* Xue, A., Kong, R., Yang, Q., Eldaief, M. C., Angeli, P. A., Dinicola, L. M., … Yeo, B. T. T. (2021). The detailed organization of the human cerebellum estimated by intrinsic functional connectivity within the individual. https://doi.org/10.1152/jn.00561.2020


### Subcortical restingstate parcellation: Ji et al. (2019)
Ji et al. (2019) presented a parcellation of subcortical structures based on correlation with 10 cortical networks, based on the HCP resting state data.
* Ji10:    Subcortical resting state parcellation in 10 networks

References and Links:
* Buckner, R. L., Krienen, F. M., Castellanos, A., Diaz, J. C. & Yeo, B. T. (2011). The organization of the human cerebellum estimated by intrinsic functional connectivity. J Neurophysiol 106, 2322–2345.


### Multi-domain task battery (MDTB) parcellation: King et al. (2019)
King et al. (2019) provided an extensive characterization of the functional organization of the cerebellum, by collecting data from 47 task conditions in 24 healthy, young participants. Based on the the task data, a parcellation of the cerebellum in 7, 10, or 17 regions was supplied.
* MDTB10:    MDTB 10 region parcellation

References and Links:
* King, M., Hernandez-Castillo, C.R., Poldrack, R.R., Ivry, R., and Diedrichsen, J. (2019). Functional Boundaries in the Human Cerebellum revealed by a Multi-Domain Task Battery. Nat. Neurosci.


### Multi-domain task battery (MDTB) contrast maps: King et al. (2019)
King et al. (2019) provided an extensive characterization of the functional organization of the cerebellum of 24 healthy, young participants. The contast are for for 47 task conditions, accounted for the activity caused by left hand, right hand, and eye movements. All maps are relative to the mean activitiy across all tasks.
* LeftHandMovement:    Activity across tasks accounted for by left hand movements
* RightHandMovement:    Activity across tasks accounted for by right hand movements
* Saccades:    Activity across tasks accounted for by saccadic eye movements
* NoGo:    Go-Nogo task with words: No-go
* Go:    Go-Nogo task with words: go
* TheoryOfMind:    2 AFC task to indicate if a short story contains true or false belief
* ActionObservation:    Passive viewing of knots being tied
* VideoKnots:    Passive viewing of static knots
* UnpleasantScenes:    IAPS affective pictures: Unpleasant scenes
* PleasantScenes:    IAPS affective pictures: Pleasant scenes
* Math:    Simple multiplication equations: Judge true or false
* DigitJudgement:    Control task for Math: detect 1 within 4 digits
* ObjectViewing:    Passive viewing of objects or checkerboard patterns
* SadFaces:    IAPS affective pictures: Sad facial expressions
* HappyFaces:    IAPS affective pictures: Happy facial expressions
* IntervalTiming:    Auditory temporal judgement task between short (100ms) and long (175ms) 
* MotorImagery:    Imagine playing a game of tennis
* FingerSimple:    Series of six simple key presses of same finger
* FingerSequence:    Bimanual sequence of six key press
* Verbal2Back-:    Working memory 2-back task with words: no target 
* Verbal2Back+:    Working memory 2-back task with words: target 
* Object2Back-:    Working memory 2-back task with pictures: no target 
* Object2Back+:    Working memory 2-back task with pictures: target 
* SpatialImagery:    Imagine to walk from kitchen to bathroom in your childhood home
* StroopIncongruent:    Stroop task: Incongruent trials
* StroopCongruent:    Stroop task: Congruent trials
* VerbGeneration:    Generate a verb for a displayed noun (dog->bark)
* WordReading:    Read the displayed noun: control for verb generation
* VisualSearchSmall:    Find a target ('T') amoung distractors ('L'): 4 items
* VisualSearchMedium:    Find a target ('T') amoung distractors ('L'): 8 items
* VisualSearchLarge:    Find a target ('T') amoung distractors ('L'): 12 items
* Rest:    Passive viewing of fixation cross 
* CPRO:    Concrete Permuted Rules Operations: Apply set of rules to 2 stimuli
* PredictionTrue:    Predicting the end of a sequentially presented sentence: fulfilled prediction
* PredictionViolated:    Predicting the end of a sequentially presented sentence: violated prediction
* PredictionScrambles:    Predicting the end of a sequentially presented sentence: scrambled sentence
* SpatialMapEasy:    Memorize a spatial map of numbers for subsequent recall: 1 item
* SpatialMapMedium:    Memorize a spatial map of numbers for subsequent recall: 4 items
* SpatialMapHard:    Memorize a spatial map of numbers for subsequent recall: 7 items
* NatureMovie:    Passive viewing of "Planet Earth II: Islands" movie: Animal movements
* AnimatedMovie:    Passive viewing of "Up" pixar movie: Social interactions
* LandscapeMovie:    Passive viewing of movie: Landscape scenes
* MentalRotationEasy:    Mental rotation task between two objects: 0 degrees
* MentalRotationMedium:    Mental rotation task between two objects: 50 degrees
* MentalRotationHard:    Mental rotation task between two objects: 150 degrees
* BiologicalMotion:    Point light walker: Judge whether gait is happy or sad
* ScrambledMotion:    Point light walker: Judge whether scrambled control stimulus moves fast or slow
* ResponseAlternativesEasy:    Execute fast keypress to imparative signal: 1 cued position
* ResponseAlternativesMedium:    Execute fast keypress to imparative signal: 2 cued positions
* ResponseAlternativesHard:    Execute fast keypress to imparative signal: 4 cued position

References and Links:
* King, M., Hernandez-Castillo, C.R., Poldrack, R.R., Ivry, R., and Diedrichsen, J. (2019). Functional Boundaries in the Human Cerebellum revealed by a Multi-Domain Task Battery. Nat. Neurosci.


## Reference and Licence
The atlas collection was curated by the Jörn Diedrichsen and his lab. 