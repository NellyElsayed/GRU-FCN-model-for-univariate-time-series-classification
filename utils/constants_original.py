# this file is originall created by the 
#@misc{Karim_Majumdar2017,
#Author = {Fazle Karim and Somshubra Majumdar and Houshang Darabi and Shun Chen},
#Title = {LSTM Fully Convolutional Networks for Time Series Classification},
##Year = {2017},
#Eprint = {arXiv:1709.05206},
#}
# and modified by: Nelly Elsayed for GRU-FCN model
# We also added the new Datasets in the UCR benchmark to to handeled by our model.
#our paper is:
#@article{elsayed2018deep,
#  title={Deep Gated Recurrent and Convolutional Network Hybrid Model for Univariate Time Series Classification},
#  author={Elsayed, Nelly and Maida, Anthony S and Bayoumi, Magdy},
#  journal={arXiv preprint arXiv:1812.07683},
#  year={2018}
#}
TRAIN_FILES = ['../data\\Adiac_TRAIN.csv', # 0
               '../data\\ArrowHead_TRAIN.csv',  # 1
               '../data\\ChlorineConcentration_TRAIN.csv',  # 2
               '../data\\InsectWingbeatSound_TRAIN.csv',  # 3
               '../data\\Lighting7_TRAIN.csv',  # 4
               '../data\\Wine_TRAIN.csv',  # 5
               '../data\\WordsSynonyms_TRAIN.csv',  # 6
               '../data\\50words_TRAIN.csv',  # 7
               '../data\\Beef_TRAIN.csv',  # 8
               '../data\\DistalPhalanxOutlineAgeGroup_TRAIN.csv',  # 9 (inverted dataset)
               '../data\\DistalPhalanxOutlineCorrect_TRAIN.csv',  # 10 (not inverted dataset)
               '../data\\DistalPhalanxTW_TRAIN.csv',  # 11 (inverted dataset)
               '../data\\ECG200_TRAIN.csv',  # 12
               '../data\\ECGFiveDays_TRAIN.csv',  # 13
               '../data\\BeetleFly_TRAIN.csv',  # 14
               '../data\\BirdChicken_TRAIN.csv',  # 15
               '../data\\ItalyPowerDemand_TRAIN.csv', # 16
               '../data\\SonyAIBORobotSurface_TRAIN.csv', # 17
               '../data\\SonyAIBORobotSurfaceII_TRAIN.csv', # 18
               '../data\\MiddlePhalanxOutlineAgeGroup_TRAIN.csv', # 19
               '../data\\MiddlePhalanxOutlineCorrect_TRAIN.csv', # 20
               '../data\\MiddlePhalanxTW_TRAIN.csv', # 21
               '../data\\ProximalPhalanxOutlineAgeGroup_TRAIN.csv', # 22
               '../data\\ProximalPhalanxOutlineCorrect_TRAIN.csv', # 23
               '../data\\ProximalPhalanxTW_TRAIN.csv', # 24 (inverted dataset)
               '../data\\MoteStrain_TRAIN.csv', # 25
               '../data\\MedicalImages_TRAIN.csv', # 26
               '../data\\Strawberry_TEST.csv',  # 27 (inverted dataset)
               '../data\\ToeSegmentation1_TRAIN.csv',  # 28
               '../data\\Coffee_TRAIN.csv',  # 29
               '../data\\Cricket_X_TRAIN.csv',  # 30
               '../data\\Cricket_Y_TRAIN.csv',  # 31
               '../data\\Cricket_Z_TRAIN.csv',  # 32
               '../data\\uWaveGestureLibrary_X_TRAIN.csv',  # 33
               '../data\\uWaveGestureLibrary_Y_TRAIN.csv',  # 34
               '../data\\uWaveGestureLibrary_Z_TRAIN.csv',  # 35
               '../data\\ToeSegmentation2_TRAIN.csv',  # 36
               '../data\\DiatomSizeReduction_TRAIN.csv',  # 37
               '../data\\car_TRAIN.csv',  # 38
               '../data\\CBF_TRAIN.csv',  # 39
               '../data\\CinC_ECG_torso_TRAIN.csv',  # 40
               '../data\\Computers_TRAIN.csv',  # 41
               '../data\\Earthquakes_TRAIN.csv',  # 42 (not inverted dataset)
               '../data\\ECG5000_TRAIN.csv',  # 43
               '../data\\ElectricDevices_TRAIN.csv',  # 44
               '../data\\FaceAll_TRAIN.csv',  # 45
               '../data\\FaceFour_TRAIN.csv',  # 46
               '../data\\FacesUCR_TRAIN.csv',  # 47
               '../data\\Fish_TRAIN.csv',  # 48
               '../data\\FordA_TRAIN.csv',  # 49 (not inverted dataset)
               '../data\\FordB_TRAIN.csv',  # 50 (not inverted dataset)
               '../data\\Gun_Point_TRAIN.csv',  # 51
               '../data\\Ham_TRAIN.csv',  # 52
               '../data\\HandOutlines_TRAIN.csv',  # 53 (not inverted dataset)
               '../data\\Haptics_TRAIN.csv', # 54
               '../data\\Herring_TRAIN.csv', # 55
               '../data\\InlineSkate_TRAIN.csv', # 56
               '../data\\LargeKitchenAppliances_TRAIN.csv', # 57
               '../data\\Lighting2_TRAIN.csv', # 58
               '../data\\MALLAT_TRAIN.csv', # 59
               '../data\\Meat_TRAIN.csv', # 60
               '../data\\NonInvasiveFatalECG_Thorax1_TRAIN.csv', # 61
               '../data\\NonInvasiveFatalECG_Thorax2_TRAIN.csv', # 62
               '../data\\OliveOil_TRAIN.csv', # 63
               '../data\\OSULeaf_TRAIN.csv', # 64
               '../data\\PhalangesOutlinesCorrect_TRAIN.csv',  # 65
               '../data\\Phoneme_TRAIN.csv',  # 66
               '../data\\plane_TRAIN.csv',  # 67
               '../data\\RefrigerationDevices_TRAIN.csv',  # 68
               '../data\\ScreenType_TRAIN.csv',  # 69
               '../data\\ShapeletSim_TRAIN.csv',  # 70
               '../data\\ShapesAll_TRAIN.csv',  # 71
               '../data\\SmallKitchenAppliances_TRAIN.csv',  # 72
               '../data\\StarlightCurves_TRAIN.csv',  # 73
               '../data\\SwedishLeaf_TRAIN.csv',  # 74
               '../data\\Symbols_TRAIN.csv',  # 75
               '../data\\synthetic_control_TRAIN.csv',  # 76
               '../data\\Trace_TRAIN.csv',  # 77
               '../data\\Two_Patterns_TRAIN.csv',  # 78
               '../data\\TwoLeadECG_TRAIN.csv',  # 79
               '../data\\UWaveGestureLibraryAll_TRAIN.csv',  # 80
               '../data\\wafer_TRAIN.csv',  # 81
               '../data\\Worms_TRAIN.csv',  # 82
               '../data\\WormsTwoClass_TRAIN.csv',  # 83
               '../data\\yoga_TRAIN.csv',  # 84
               '../data\\ACSF1_TRAIN.csv', #85
               '../data\\AllGestureWiimoteX_TRAIN.csv', # 86
               '../data\\AllGestureWiimoteY_TRAIN.csv',#87
               '../data\\AllGestureWiimoteZ_TRAIN.csv',#88
               '../data\\BME_TRAIN.csv',#89
               '../data\\Chinatown_TRAIN.csv',#90
               '../data\\Crop_TRAIN.csv',#91
               '../data\\DodgerLoopDay_TRAIN.csv',#92
               '../data\\DodgerLoopGame_TRAIN.csv',#93
               '../data\\DodgerLoopWeekend_TRAIN.csv',#94
               '../data\\EOGHorizontalSignal_TRAIN.csv',#95
               '../data\\EOGVerticalSignal_TRAIN.csv',#96
               '../data\\EthanolLevel_TRAIN.csv',#97
               '../data\\FreezerRegularTrain_TRAIN.csv',#98
               '../data\\FreezerSmallTrain_TRAIN.csv',#99
               '../data\\Fungi_TRAIN.csv',#100
               '../data\\GestureMidAirD1_TRAIN.csv',#101
               '../data\\GestureMidAirD2_TRAIN.csv',#102
               '../data\\GestureMidAirD3_TRAIN.csv',#103
               '../data\\GesturePebbleZ1_TRAIN.csv',#104
               '../data\\GesturePebbleZ2_TRAIN.csv',#105
               '../data\\GunPointAgeSpan_TRAIN.csv',#106
               '../data\\GunPointMaleVersusFemale_TRAIN.csv',#107
               '../data\\GunPointOldVersusYoung_TRAIN.csv',#108
               '../data\\HouseTwenty_TRAIN.csv',#109
               '../data\\InsectEPGRegularTrain_TRAIN.csv',#110
               '../data\\InsectEPGSmallTrain_TRAIN.csv',#111
               '../data\\MelbournePedestrian_TRAIN.csv',#112
               '../data\\MixedShapesRegularTrain_TRAIN.csv',#113
               '../data\\MixedShapesSmallTrain_TRAIN.csv',#114
               '../data\\PickupGestureWiimoteZ_TRAIN.csv',#115
               '../data\\PigAirwayPressure_TRAIN.csv',#116
               '../data\\PigArtPressure_TRAIN.csv',#117
               '../data\\PigCVP_TRAIN.csv',#118
               '../data\\PLAID_TRAIN.csv',#119
               '../data\\PowerCons_TRAIN.csv',#120
               '../data\\Rock_TRAIN.csv',#121
               '../data\\SemgHandGenderCh2_TRAIN.csv',#122
               '../data\\SemgHandMovementCh2_TRAIN.csv',#123
               '../data\\SemgHandSubjectCh2_TRAIN.csv',#124
               '../data\\ShakeGestureWiimoteZ_TRAIN.csv',#125
               '../data\\SmoothSubspace_TRAIN.csv',#126
               '../data\\UMD_TRAIN.csv',#127

               ]

TEST_FILES = ['../data\\Adiac_TEST.csv', # 0
              '../data\\ArrowHead_TEST.csv', # 1
              '../data\\ChlorineConcentration_TEST.csv', # 2
              '../data\\InsectWingbeatSound_TEST.csv', # 3
              '../data\\Lighting7_TEST.csv', # 4
              '../data\\Wine_TEST.csv', # 5
              '../data\\WordsSynonyms_TEST.csv', # 6
              '../data\\50words_TEST.csv', # 7
              '../data\\Beef_TEST.csv', # 8
              '../data\\DistalPhalanxOutlineAgeGroup_TEST.csv', # 9 (not inverted dataset)
              '../data\\DistalPhalanxOutlineCorrect_TEST.csv', # 10 (not inverted dataset)
              '../data\\DistalPhalanxTW_TEST.csv', # 11 (not inverted dataset)
              '../data\\ECG200_TEST.csv', # 12
              '../data\\ECGFiveDays_TEST.csv', # 13
              '../data\\BeetleFly_TEST.csv', # 14
              '../data\\BirdChicken_TEST.csv', # 15
              '../data\\ItalyPowerDemand_TEST.csv', # 16
              '../data\\SonyAIBORobotSurface_TEST.csv', # 17
              '../data\\SonyAIBORobotSurfaceII_TEST.csv', # 18
              '../data\\MiddlePhalanxOutlineAgeGroup_TEST.csv', # 19 (inverted dataset)
              '../data\\MiddlePhalanxOutlineCorrect_TEST.csv', # 20 (inverted dataset)
              '../data\\MiddlePhalanxTW_TEST.csv', # 21 (inverted dataset)
              '../data\\ProximalPhalanxOutlineAgeGroup_TEST.csv', # 22
              '../data\\ProximalPhalanxOutlineCorrect_TEST.csv', # 23
              '../data\\ProximalPhalanxTW_TEST.csv', # 24 (inverted dataset)
              '../data\\MoteStrain_TEST.csv', # 25
              '../data\\MedicalImages_TEST.csv', # 26
              '../data\\Strawberry_TRAIN.csv',  # 27
              '../data\\ToeSegmentation1_TEST.csv',  # 28
              '../data\\Coffee_TEST.csv',  # 29
              '../data\\Cricket_X_TEST.csv',  # 30
              '../data\\Cricket_Y_TEST.csv',  # 31
              '../data\\Cricket_Z_TEST.csv',  # 32
              '../data\\uWaveGestureLibrary_X_TEST.csv',  # 33
              '../data\\uWaveGestureLibrary_Y_TEST.csv',  # 34
              '../data\\uWaveGestureLibrary_Z_TEST.csv',  # 35
              '../data\\ToeSegmentation2_TEST.csv',  # 36
              '../data\\DiatomSizeReduction_TEST.csv',  # 37
              '../data\\car_TEST.csv',  # 38
              '../data\\CBF_TEST.csv',  # 39
              '../data\\CinC_ECG_torso_TEST.csv',  # 40
              '../data\\Computers_TEST.csv',  # 41
              '../data\\Earthquakes_TEST.csv',  # 42 (not inverted dataset)
              '../data\\ECG5000_TEST.csv',  # 43
              '../data\\ElectricDevices_TEST.csv',  # 44
              '../data\\FaceAll_TEST.csv',  # 45
              '../data\\FaceFour_TEST.csv',  # 46
              '../data\\FacesUCR_TEST.csv',  # 47
              '../data\\Fish_TEST.csv',  # 48
              '../data\\FordA_TEST.csv',  # 49 (not inverted dataset)
              '../data\\FordB_TEST.csv',  # 50 (not inverted dataset)
              '../data\\Gun_Point_TEST.csv',  # 51
              '../data\\Ham_TEST.csv',  # 52
              '../data\\HandOutlines_TEST.csv',  # 53 (not inverted dataset)
              '../data\\Haptics_TEST.csv',  # 54
              '../data\\Herring_TEST.csv',  # 55
              '../data\\InlineSkate_TEST.csv',  # 56
              '../data\\LargeKitchenAppliances_TEST.csv',  # 57
              '../data\\Lighting2_TEST.csv',  # 58
              '../data\\MALLAT_TEST.csv',  # 59
              '../data\\Meat_TEST.csv',  # 60
              '../data\\NonInvasiveFatalECG_Thorax1_TEST.csv',  # 61
              '../data\\NonInvasiveFatalECG_Thorax2_TEST.csv',  # 62
              '../data\\OliveOil_TEST.csv',  # 63
              '../data\\OSULeaf_TEST.csv',  # 64
              '../data\\PhalangesOutlinesCorrect_TEST.csv',  # 65
              '../data\\Phoneme_TEST.csv',  # 66
              '../data\\plane_TEST.csv',  # 67
              '../data\\RefrigerationDevices_TEST.csv',  # 68
              '../data\\ScreenType_TEST.csv',  # 69
              '../data\\ShapeletSim_TEST.csv',  # 70
              '../data\\ShapesAll_TEST.csv',  # 71
              '../data\\SmallKitchenAppliances_TEST.csv',  # 72
              '../data\\StarlightCurves_TEST.csv',  # 73
              '../data\\SwedishLeaf_TEST.csv',  # 74
              '../data\\Symbols_TEST.csv',  # 75
              '../data\\synthetic_control_TEST.csv',  # 76
              '../data\\Trace_TEST.csv',  # 77
              '../data\\Two_Patterns_TEST',  # 78
              '../data\\TwoLeadECG_TEST.csv',  # 79
              '../data\\UWaveGestureLibraryAll_TEST.csv',  # 80
              '../data\\wafer_TEST.csv',  # 81
              '../data\\Worms_TEST.csv',  # 82
              '../data\\WormsTwoClass_TEST.csv',  # 83
              '../data\\yoga_TEST.csv',  # 84
              '../data\\ACSF1_TEST.csv',#85
              '../data\\AllGestureWiimoteX_TEST.csv',#86
              '../data\\AllGestureWiimoteY_TEST.csv',#87
              '../data\\AllGestureWiimoteZ_TEST.csv',#88
              '../data\\BME_TEST.csv',#89
              '../data\\Chinatown_TEST.csv',#90
              '../data\\Crop_TEST.csv',#91
              '../data\\DodgerLoopDay_TEST.csv',#92
              '../data\\DodgerLoopGame_TEST.csv',#93
              '../data\\DodgerLoopWeekend_TEST.csv',#94
              '../data\\EOGHorizontalSignal_TEST.csv',#95
              '../data\\EOGVerticalSignal_TEST.csv',#96
              '../data\\EthanolLevel_TEST.csv',#97
              '../data\\FreezerRegularTrain_TEST.csv',#98
              '../data\\FreezerSmallTrain_TEST.csv',#99
              '../data\\Fungi_TEST.csv',#100
              '../data\\GestureMidAirD1_TEST.csv',#101
              '../data\\GestureMidAirD2_TEST.csv',#102
              '../data\\GestureMidAirD3_TEST.csv',#103
              '../data\\GesturePebbleZ1_TEST.csv',#104
              '../data\\GesturePebbleZ2_TEST.csv',#105
              '../data\\GunPointAgeSpan_TEST.csv',#106
              '../data\\GunPointMaleVersusFemale_TEST.csv',#107
              '../data\\GunPointOldVersusYoung_TEST.csv',#108
              '../data\\HouseTwenty_TEST.csv',#109
              '../data\\InsectEPGRegularTrain_TEST.csv',#110
              '../data\\InsectEPGSmallTrain_TEST.csv',#111
              '../data\\MelbournePedestrian_TEST.csv',#112
              '../data\\MixedShapesRegularTrain_TEST.csv',#113
              '../data\\MixedShapesSmallTrain_TEST.csv',#114
              '../data\\PickupGestureWiimoteZ_TEST.csv',#115
              '../data\\PigAirwayPressure_TEST.csv',#116
              '../data\\PigArtPressure_TEST.csv',#117
              '../data\\PigCVP_TEST.csv',#118
              '../data\\PLAID_TEST.csv',#119
              '../data\\PowerCons_TEST.csv',#120
              '../data\\Rock_TEST.csv',#121
              '../data\\SemgHandGenderCh2_TEST.csv',#122
              '../data\\SemgHandMovementCh2_TEST.csv',#123
              '../data\\SemgHandSubjectCh2_TEST.csv',#124
              '../data\\ShakeGestureWiimoteZ_TEST.csv',#125
              '../data\\SmoothSubspace_TEST.csv',#126
              '../data\\UMD_TEST.csv',#127

              ]

MAX_SEQUENCE_LENGTH_LIST = [176, # 0 # time_series_length
                            251, # 1
                            166, # 2
                            256, # 3
                            319, # 4
                            234, # 5
                            270, # 6
                            270, # 7
                            470, # 8
                            80,  # 9
                            80,  # 10
                            80,  # 11
                            96, # 12
                            136, # 13
                            512, # 14
                            512, # 15
                            24, # 16
                            70, # 17
                            65, # 18
                            80, # 19
                            80, # 20
                            80, # 21
                            80, # 22
                            80, # 23
                            80, # 24
                            84, # 25
                            99, # 26
                            235, # 27
                            277, # 28
                            286, # 29
                            300, # 30
                            300, # 31
                            300, # 32
                            315, # 33
                            315, # 34
                            315, # 35
                            343, # 36
                            345, # 37
                            577, # 38
                            128, # 39
                            1639, # 40
                            720, # 41
                            512, # 42
                            140, # 43
                            96, # 44
                            131, # 45
                            350, # 46
                            131, # 47
                            463, # 48
                            500, # 49
                            500, # 50
                            150, # 51
                            431, # 52
                            2709, # 53
                            1092, # 54
                            512, # 55
                            1882, # 56
                            720, # 57
                            637, # 58
                            1024, # 59
                            448, # 60
                            750, # 61
                            750, # 62
                            570, # 63
                            427, # 64
                            80, # 65
                            1024, # 66
                            144, # 67
                            720, # 68
                            720, # 69
                            500, # 70
                            512, # 71
                            720, # 72
                            1024, # 73
                            128, # 74
                            398, # 75
                            60, # 76
                            275, # 77
                            128, # 78
                            82, # 79
                            945, # 80
                            152, # 81
                            900, # 82
                            900, # 83
                            426, # 84
                            1460, # 85
                            100, # 86 vary
                            100, # 87 vary
                            100, # 88 vary
                            128, #89
                            24,  #90
                            46,  #91
                            288,  #92
                            288, #93
                            288, #94
                            1250,#95
                            1250,#96
                            1751,#97
                            301,#98
                            301,#99
                            201,#100
                            100,#101 Vary
                            100, #102 Vary
                            100,#103 Vary
                            100,#104 Vary
                            100,#105Vary
                            150,#106
                            150,#107
                            150,#108
                            2000,#109
                            601,#110
                            601,#111
                            24,#112
                            1024,#113
                            1024,#114
                            100,#115 Vary
                            2000,#116
                            2000,#117
                            2000,#118
                            100,#119 Vary
                            144,#120
                            2844,#121
                            1500,#122
                            1500,#123
                            1500,#124
                            100,#125 Vary
                            15,#126
                            150,#127
                            ]

NB_CLASSES_LIST = [37, # 0  # number of classes
                   3, # 1 
                   3, # 2
                   11, # 3
                   7, # 4
                   2, # 5
                   25, # 6
                   50, # 7
                   5, # 8
                   3, # 9
                   2, # 10
                   6, # 11
                   2, # 12
                   2, # 13
                   2, # 14
                   2, # 15
                   2, # 16
                   2, # 17
                   2, # 18
                   3, # 19
                   2, # 20
                   6, # 21
                   3, # 22
                   2, # 23
                   6, # 24
                   2, # 25
                   10, # 26
                   2, # 27
                   2, # 28
                   2, # 29
                   12, # 30
                   12, # 31
                   12, # 32
                   8, # 33
                   8, # 34
                   8, # 35
                   2, # 36
                   4, # 37
                   4, # 38
                   3, # 39
                   4, # 40
                   2, # 41
                   2, # 42
                   5, # 43
                   7, # 44
                   14, # 45
                   4, # 46
                   14, # 47
                   7, # 48
                   2, # 49
                   2, # 50
                   2, # 51
                   2, # 52
                   2, # 53
                   5, # 54
                   2, # 55
                   7, # 56
                   3, # 57
                   2, # 58
                   8, # 59
                   3, # 60
                   42, # 61
                   42, # 62
                   4, # 63
                   6, # 64
                   2, # 65
                   39, # 66
                   7, # 67
                   3, # 68
                   3, # 69
                   2, # 70
                   60, # 71
                   3, # 72
                   3, # 73
                   15, # 74
                   6, # 75
                   6, # 76
                   4, # 77
                   4, # 78
                   2, # 79
                   8, # 80
                   2, # 81
                   5, # 82
                   2, # 83
                   2, # 84
                   10,# 85
                   10,# 86
                   10,#87
                   10,#88
                   3,#89
                   2,#90
                   24,#91
                   7,#92
                   2,#93
                   2,#94
                   12,#95
                   12,#96
                   4,#97
                   2,#98
                   2,#99
                   18,#100
                   26,#101
                   26,#102
                   26,#103
                   6,#104
                   6,#105
                   2,#106
                   2,#107
                   2,#108
                   2,#109
                   3,#110
                   3,#111
                   10,#112
                   5,#113
                   5,#114
                   10,#115
                   52,#116
                   52,#117
                   52,#118
                   11,#119
                   2,#120
                   4,#121
                   2,#122
                   6,#123
                   5,#123
                   10,#125
                   3,#126
                   3,#127
                   ]