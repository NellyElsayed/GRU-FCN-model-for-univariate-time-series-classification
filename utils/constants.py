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
TRAIN_FILES = ['../data\\Adiac_TRAIN', #0
               '../data\\ArrowHead_TRAIN',  #1
			   '../data\\Beef_TRAIN',  #2
			   '../data\\BeetleFly_TRAIN', #3
			   '../data\\BirdChicken_TRAIN', #4
			   '../data\\Car_TRAIN', #5 
			   '../data\\CBF_TRAIN', #6
			   '../data\\ChlorineConcentration_TRAIN', #7
			   '../data\\CinC_ECG_torso_TRAIN', #8
			   '../data\\Coffee_TRAIN', #9
			   '../data\\Computers_TRAIN', #10
			   '../data\\Cricket_X_TRAIN',  #11
               '../data\\Cricket_Y_TRAIN',  #12
               '../data\\Cricket_Z_TRAIN',  #13
			   '../data\\DiatomSizeReduction_TRAIN', #14 
			   '../data\\DistalPhalanxOutlineAgeGroup_TRAIN', #15
			   '../data\\DistalPhalanxOutlineCorrect_TRAIN',  #16
               '../data\\DistalPhalanxTW_TRAIN', #17
			   '../data\\Earthquakes_TRAIN', #18
			   '../data\\ECG200_TRAIN', #19
               '../data\\ECG5000_TRAIN', #20 
			   '../data\\ECGFiveDays_TRAIN', #21
			   '../data\\ElectricDevices_TRAIN', #22 
			   '../data\\FaceAll_TRAIN',  # 23
               '../data\\FaceFour_TRAIN',  # 24
               '../data\\FacesUCR_TRAIN',  # 25
			   '../data\\50words_TRAIN', # 26
               '../data\\Fish_TRAIN',  # 27
               '../data\\FordA_TRAIN',  # 28
               '../data\\FordB_TRAIN',  # 29
               '../data\\Gun_Point_TRAIN',  # 30
               '../data\\Ham_TRAIN',  # 31
               '../data\\HandOutlines_TRAIN',  # 32 
               '../data\\Haptics_TRAIN', # 33
               '../data\\Herring_TRAIN', # 34
               '../data\\InlineSkate_TRAIN', #35
			   '../data\\InsectWingbeatSound_TRAIN', #36
			   '../data\\ItalyPowerDemand_TRAIN', #37
			   '../data\\LargeKitchenAppliances_TRAIN', #38
			   '../data\\Lighting2_TRAIN', #39
			   '../data\\Lighting7_TRAIN', #40
			   '../data\\MALLAT_TRAIN', # 41
               '../data\\Meat_TRAIN', #42
			   '../data\\MedicalImages_TRAIN', #43
			   '../data\\MiddlePhalanxOutlineAgeGroup_TRAIN', #44
			   '../data\\MiddlePhalanxOutlineCorrect_TRAIN', #45
			   '../data\\MiddlePhalanxTW_TRAIN', #46
			   '../data\\MoteStrain_TRAIN', #47
               '../data\\NonInvasiveFatalECG_Thorax1_TRAIN', # 48
               '../data\\NonInvasiveFatalECG_Thorax2_TRAIN',#49
			   '../data\\OliveOil_TRAIN',#50
			   '../data\\OSULeaf_TRAIN', # 51
               '../data\\PhalangesOutlinesCorrect_TRAIN', #52
			   '../data\\Phoneme_TRAIN',  # 53
               '../data\\plane_TRAIN', #54
               '../data\\ProximalPhalanxOutlineAgeGroup_TRAIN', # 55
               '../data\\ProximalPhalanxOutlineCorrect_TRAIN', # 56
               '../data\\ProximalPhalanxTW_TRAIN', #57
			   '../data\\RefrigerationDevices_TRAIN', # 58
			   '../data\\ScreenType_TRAIN',  # 59
               '../data\\ShapeletSim_TRAIN',  # 60
               '../data\\ShapesAll_TRAIN',  # 61
               '../data\\SmallKitchenAppliances_TRAIN', #62
			   '../data\\SonyAIBORobotSurface_TRAIN', # 63
               '../data\\SonyAIBORobotSurfaceII_TRAIN', #64
			   '../data\\StarlightCurves_TRAIN', #65
			   '../data\\Strawberry_TEST', #66
			   '../data\\SwedishLeaf_TRAIN', #67
			   '../data\\Symbols_TRAIN', #68
			   '../data\\synthetic_control_TRAIN', #69
			   '../data\\ToeSegmentation1_TRAIN', #70
			   '../data\\ToeSegmentation2_TRAIN', #71
			   '../data\\Trace_TRAIN', #72
			   '../data\\TwoLeadECG_TRAIN', #73
			   '../data\\Two_Patterns_TRAIN', #74
			   '../data\\UWaveGestureLibraryAll_TRAIN',#75
			   '../data\\uWaveGestureLibrary_X_TRAIN',  # 76
               '../data\\uWaveGestureLibrary_Y_TRAIN',  # 77
               '../data\\uWaveGestureLibrary_Z_TRAIN', #78
			   '../data\\wafer_TRAIN', #79
			   '../data\\Wine_TRAIN', #80
               '../data\\WordsSynonyms_TRAIN',  # 81
               '../data\\Worms_TRAIN',  # 82
               '../data\\WormsTwoClass_TRAIN',  # 83
               '../data\\yoga_TRAIN',  # 84   
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

TEST_FILES = ['../data\\Adiac_TEST', #0
               '../data\\ArrowHead_TEST',  #1
			   '../data\\Beef_TEST',  #2
			   '../data\\BeetleFly_TEST', #3
			   '../data\\BirdChicken_TEST', #4
			   '../data\\Car_TEST', #5 
			   '../data\\CBF_TEST', #6
			   '../data\\ChlorineConcentration_TEST', #7
			   '../data\\CinC_ECG_torso_TEST', #8
			   '../data\\Coffee_TEST', #9
			   '../data\\Computers_TEST', #10
			   '../data\\Cricket_X_TEST',  #11
               '../data\\Cricket_Y_TEST',  #12
               '../data\\Cricket_Z_TEST',  #13
			   '../data\\DiatomSizeReduction_TEST', #14 
			   '../data\\DistalPhalanxOutlineAgeGroup_TEST', #15
			   '../data\\DistalPhalanxOutlineCorrect_TEST',  #16
               '../data\\DistalPhalanxTW_TEST', #17
			   '../data\\Earthquakes_TEST', #18
			   '../data\\ECG200_TEST', #19
               '../data\\ECG5000_TEST', #20 
			   '../data\\ECGFiveDays_TEST', #21
			   '../data\\ElectricDevices_TEST', #22 
			   '../data\\FaceAll_TEST',  # 23
               '../data\\FaceFour_TEST',  # 24
               '../data\\FacesUCR_TEST',  # 25
			   '../data\\50words_TEST', # 26
               '../data\\Fish_TEST',  # 27
               '../data\\FordA_TEST',  # 28
               '../data\\FordB_TEST',  # 29
               '../data\\Gun_Point_TEST',  # 30
               '../data\\Ham_TEST',  # 31
               '../data\\HandOutlines_TEST',  # 32 
               '../data\\Haptics_TEST', # 33
               '../data\\Herring_TEST', # 34
               '../data\\InlineSkate_TEST', #35
			   '../data\\InsectWingbeatSound_TEST', #36
			   '../data\\ItalyPowerDemand_TEST', #37
			   '../data\\LargeKitchenAppliances_TEST', #38
			   '../data\\Lighting2_TEST', #39
			   '../data\\Lighting7_TEST', #40
			   '../data\\MALLAT_TEST', # 41
               '../data\\Meat_TEST', #42
			   '../data\\MedicalImages_TEST', #43
			   '../data\\MiddlePhalanxOutlineAgeGroup_TEST', #44
			   '../data\\MiddlePhalanxOutlineCorrect_TEST', #45
			   '../data\\MiddlePhalanxTW_TEST', #46
			   '../data\\MoteSTEST_TEST', #47
               '../data\\NonInvasiveFatalECG_Thorax1_TEST', # 48
               '../data\\NonInvasiveFatalECG_Thorax2_TEST',#49
			   '../data\\OliveOil_TEST',#50
			   '../data\\OSULeaf_TEST', # 51
               '../data\\PhalangesOutlinesCorrect_TEST', #52
			   '../data\\Phoneme_TEST',  # 53
               '../data\\plane_TEST', #54
               '../data\\ProximalPhalanxOutlineAgeGroup_TEST', # 55
               '../data\\ProximalPhalanxOutlineCorrect_TEST', # 56
               '../data\\ProximalPhalanxTW_TEST', #57
			   '../data\\RefrigerationDevices_TEST', # 58
			   '../data\\ScreenType_TEST',  # 59
               '../data\\ShapeletSim_TEST',  # 60
               '../data\\ShapesAll_TEST',  # 61
               '../data\\SmallKitchenAppliances_TEST', #62
			   '../data\\SonyAIBORobotSurface_TEST', # 63
               '../data\\SonyAIBORobotSurfaceII_TEST', #64
			   '../data\\StarlightCurves_TEST', #65
			   '../data\\Strawberry_TEST', #66
			   '../data\\SwedishLeaf_TEST', #67
			   '../data\\Symbols_TEST', #68
			   '../data\\synthetic_control_TEST', #69
			   '../data\\ToeSegmentation1_TEST', #70
			   '../data\\ToeSegmentation2_TEST', #71
			   '../data\\Trace_TEST', #72
			   '../data\\TwoLeadECG_TEST', #73
			   '../data\\Two_Patterns_TEST', #74
			   '../data\\UWaveGestureLibraryAll_TEST',#75
			   '../data\\uWaveGestureLibrary_X_TEST',  # 76
               '../data\\uWaveGestureLibrary_Y_TEST',  # 77
               '../data\\uWaveGestureLibrary_Z_TEST', #78
			   '../data\\wafer_TEST', #79
			   '../data\\Wine_TEST', #80
               '../data\\WordsSynonyms_TEST',  # 81
               '../data\\Worms_TEST',  # 82
               '../data\\WormsTwoClass_TEST',  # 83
               '../data\\yoga_TEST',  # 84   
               '../data\\ACSF1_TEST.csv', #85
               '../data\\AllGestureWiimoteX_TEST.csv', # 86
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
               '../data\\FreezerRegularTEST_TEST.csv',#98
               '../data\\FreezerSmallTEST_TEST.csv',#99
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
               '../data\\InsectEPGRegularTEST_TEST.csv',#110
               '../data\\InsectEPGSmallTEST_TEST.csv',#111
               '../data\\MelbournePedestrian_TEST.csv',#112
               '../data\\MixedShapesRegularTEST_TEST.csv',#113
               '../data\\MixedShapesSmallTEST_TEST.csv',#114
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

MAX_SEQUENCE_LENGTH_LIST = [ # time_series_length
                            176, #0
							251, #1
							470, #2
							512,#3
							512,#4
							577,#5
							128,#6
							166,#7
							1639,#8
							286,#9
							720,#10
							300,#11
							300,#12
							300,#13
							345,#14
							80,#15
							80,#16
							80,#17
							512,#18
							96,#19
							140,#20
							136,#21
							96,#22
							131,#23
							350,#24
							131,#25
							270,#26
							463,#27
							500,#28
							500,#29
							150,#30
							431,#31
							2709,#32
							1092,#33
							512,#34
							1882,#35
							256,#36
							24,#37
							720,#38
							637,#39
							319,#40
							1024,#41
							448,#42
							99,#43
							80,#44
							80,#45
							80,#46
							84,#47
							750,#48
							750,#49
							570,#50
							427,#51
							80,#52
							1024,#53
							144,#54
							80,#55
							80,#56
							80,#57
							720,#58
							720,#59
							500,#60
							512,#61
							720,#62
							70,#63
							65,#64
							1024,#65
							235,#66
							128,#67
							398,#68
							60,#69
							277,#70
							343,#71
							275,#72
							82,#73
							128,#74
							945,#75
							315,#76
							315,#77
							315,#78
							152,#79
							234,#80
							270,#81
							900,#82
							900,#83
							426,#84
							1460,#85
							100,# 86 Vary
							100,# 87 VaryVary
							100,# 88 VaryVary
							128,# 89
							24,#90
							46,#91
							288,#92
							288,#93
							288,#94
							1250,#95
							1250,#96
							1751,#97
							301,#98
							301,#99
							201,#100
							100,#101 Vary
							100,#102 Vary
							100,#103 Vary
							100,# 104 Vary
							100,#105 Vary
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

NB_CLASSES_LIST = [# number of classes
                   37, #0
					3,#1
					5,#2
					2,#3
					2,#4
					4,#5
					3,#6
					3,#7
					4,#8
					2,#9
					2,#10
					12,#11
					12,#12
					12,#13
					4,#14
					3,#15
					2,#16
					6,#17
					2,#18
					2,#19
					5,#20
					2,#21
					7,#22
					14,#23
					4,#24
					14,#25
					50,#26
					7,#27
					2,#28
					2,#29
					2,#30
					2,#31
					2,#32
					5,#33
					2,#34
					7,#35
					11,#36
					2,#37
					3,#38
					2,#39
					7,#40
					8,#41
					3,#42
					10,#43
					3,#44
					2,#45
					6,#46
					2,#47
					42,#48
					42,#49
					4,#50
					6,#51
					2,#52
					39,#53
					7,#54
					3,#55
					2,#56
					6,#57
					3,#58
					3,#59
					2,#60
					60,#61
					3,#62
					2,#63
					2,#64
					3,#65
					2,#66
					15,#67
					6,#68
					6,#69
					2,#70
					2,#71
					4,#72
					2,#73
					4,#74
					8,#75
					8,#76
					8,#77
					8,#78
					2,#79
					2,#80
					25,#81
					5,#82
					2,#83
					2,#84
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