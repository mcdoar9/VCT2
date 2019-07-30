import pandas as pd
import numpy as np 
import os 
cwd = os.getcwd()
os.chdir("/Volumes/MorrisServerFolder/Child_Psych/Qualtrics")
os.getcwd()
qualtrics = pd.read_csv('Qualtrics_Pilot.csv',encoding = 'unicode_escape')
qualtrics1 = qualtrics.iloc[1:]
qualtrics2 = qualtrics1.drop(qualtrics1.iloc[:, 0:63], axis=1)  # df.columns is zero-based pd.Index 
qualtrics3 = qualtrics2.iloc[:, 0:125]
qualtrics3.columns = ["SSIS_1","SSIS_2", "SSIS_3","SSIS_4","SSIS_HI_1", "SSIS_HI_2", "SSIS_HI_3","SSIS_HI_4",
                                 "SSIS_5","SSIS_6","SSIS_7","SSIS_8","SSIS_HI_5","SSIS_HI_6","SSIS_HI_7","SSIS_HI_8",
                                 "SSIS_9","SSIS_10","SSIS_11","SSIS_12","SSIS_HI_9","SSIS_HI_10","SSIS_HI_11","SSIS_HI_12",
                                 "SSIS_13","SSIS_14","SSIS_15","SSIS_16","SSIS_HI_13","SSIS_HI_14","SSIS_HI_15","SSIS_HI_16",
                                 "SSIS_17","SSIS_18","SSIS_19","SSIS_20","SSIS_HI_17","SSIS_HI_18","SSIS_HI_19","SSIS_HI_20",
                                 'SSIS_21','SSIS_22','SSIS_23','SSIS_24','SSIS_HI_21','SSIS_HI_22','SSIS_HI_23','SSIS_HI_24',
                                 'SSIS_25','SSIS_26','SSIS_27','SSIS_28','SSIS_HI_25','SSIS_HI_26','SSIS_HI_27','SSIS_HI_28',
                                 'SSIS_29','SSIS_30','SSIS_31','SSIS_32','SSIS_HI_29','SSIS_HI_30','SSIS_HI_31','SSIS_HI_32',
                                 'SSIS_33','SSIS_34','SSIS_35','SSIS_36','SSIS_HI_33','SSIS_HI_34','SSIS_HI_35','SSIS_HI_36',
                                 'SSIS_37','SSIS_38','SSIS_39','SSIS_40','SSIS_HI_37','SSIS_HI_38','SSIS_HI_39','SSIS_HI_40',
                                 'SSIS-_41','SSIS_42','SSIS_43','SSIS_44','SSIS_HI_41','SSIS_HI_42','SSIS_HI_43','SSIS_HI_44',
                                 'SSIS_45','SSIS_46','SSIS_HI_45','SSIS_HI_46','SSIS_47','SSIS_48','SSIS_49','SSIS_50','SSIS_51',
                                 'SSIS_52','SSIS_53','SSIS_54','SSIS_55','SSIS_56','SSIS_57','SSIS_58','SSIS_59','SSIS_60','SSIS_61',
                                 'SSIS_62','SSIS_63','SSIS_64','SSIS_65','SSIS_66','SSIS_67','SSIS_68','SSIS_69','SSIS_70','SSIS_71',
                                 'SSIS_72','SSIS_73','SSIS_74','SSIS_75','SSIS_76','SSIS_77','SSIS_78','SSIS_79',]
qualtrics3 = qualtrics3.drop(qualtrics3.index[[61,62,63]])
qualtrics3=qualtrics3.dropna(axis=0).reset_index(drop=True)
qualtrics4 = qualtrics3.iloc[1:]
qualtrics4 = qualtrics4.iloc[:-1]
qualtrics4[qualtrics4 == "A"] = 3
qualtrics4[qualtrics4 == "O"] = 2
qualtrics4[qualtrics4 == "S"] = 1
qualtrics4[qualtrics4 == "N"] = 0
qualtrics5 = qualtrics4[qualtrics4.columns.drop(list(qualtrics4.filter(regex='HI')))]

col_names =  ['Communication', 'Cooperation', 'Assertion',"Responsibility","Empathy","Engagement","Self-Control","Externalizing","Internalizing",
              "Social_Skill_AS","Problem_Behavior_AS","Bullying","Hyperactivity_inattention","Social_Skill_Sum","Problem_Behavior_Sum"]
scoring  = pd.DataFrame(columns = col_names)
scoring['Communication']=qualtrics5.iloc[:,[3,9,13,19,23,29,39]].sum(axis=1)
scoring["Cooperation"] = qualtrics5.iloc[:,[1,6,11,16,26,36]].sum(axis=1)
scoring["Assertion"]=qualtrics5.iloc[:,[0,4,10,14,24,34,44]].sum(axis=1)
scoring["Responsibility"]=qualtrics5.iloc[:,[5,15,21,25,31,41]].sum(axis=1)
scoring["Empathy"]=qualtrics5.iloc[:,[2,7,12,17,27,37]].sum(axis=1)
scoring["Engagement"]=qualtrics5.iloc[:,[8,18,22,28,32,38,42]].sum(axis=1)
scoring["Self-Control"]=qualtrics5.iloc[:,[20,30,33,35,40,43,45]].sum(axis=1)
scoring["Externalizing"]=qualtrics5.iloc[:,[46,48,50,53,55,57,62,64,69,71,75,77]].sum(axis=1)
scoring["Internalizing"]=qualtrics5.iloc[:,[56,60,63,65,67,70,72,73,76,78]].sum(axis=1)
scoring["Social_Skill_AS"]=qualtrics5.iloc[:,[9,18,19,28,29,37,38,39]].sum(axis=1)
scoring["Problem_Behavior_AS"]=qualtrics5.iloc[:,[47,49,54,56,61,68,74]].sum(axis=1)
scoring["Bullying"]=qualtrics5.iloc[:,[48,51,55,58,62]].sum(axis=1)
scoring["Hyperactivity_inattention"]=qualtrics5.iloc[:,[46,50,52,53,57,59,66]].sum(axis=1)
scoring["Social_Skill_Sum"]=scoring.iloc[:,0:6].sum(axis=1)
scoring["Problem_Behavior_Sum"]=scoring.iloc[:,[7,8]].sum(axis=1)

SSIS_pilot = scoring.to_csv("/Volumes/MorrisServerFolder/Child_Psych/Qualtrics/SSIS_pilot.csv")
