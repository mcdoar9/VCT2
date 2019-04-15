#author: tehmeena salahin
#last updated: 4/15/2019

import csv
import pandas as pd
import os
import re
#
# with open("Eyetracking_Coding_Key.csv", 'a') as yeet:
#     writer1 = csv.writer(yeet)
#     writer1.writerow(["HAB_Loewe_rechts", "R"])
#     writer1.writerow(["TB2_Hund_rechts", "R"])
#     writer1.writerow(["FB2_Hund_links", "L"])
# yeet.close()


f = open('/Users/tehmeena/Documents/4thYEAR/Spring2019/PSYCResearch/eyetrack/Eyetracking_Coding_Key.csv') #go to file path where key is and open the file
reader = csv.reader(open('Eyetracking_Coding_Key.csv', 'r')) #read the eyetracking key excel file

eyetracker_dict_answers = {} #declare eyetracker answer dictionary
eyetracker_dict_results= {} #declare eyetracker results dictionary
for row in reader:
   movie, gaze = row #
   eyetracker_dict_answers[movie] = gaze #the key is the movie, the value is where the participant looked (gaze)
   eyetracker_dict_results[movie] = gaze #the values for this dict will keep getting reset for each participant
f.close() #close the eyetracking key excel file

print(eyetracker_dict_answers)

#set all # of times movies were watched equal to 0, this corresponds to number of categorical movies each participant watched
HAB_mov  = 0
TB_mov = 0
FB_mov = 0


#set all scores equal to zero, these correspond to the movie titles that the participants watched and correctly responded to
HAB_score = 0
TB_score = 0
FB_score = 0
Total_score = 0

answer = "" #correct gaze answer for movie

result = "" #actual participant gaze result for movie

ctr_row= 0 #initialize counter to 0, will be used to index rows (participants)
ctr_col = 1 #initialize counter to 0, will be used to index columns (gazes)


with open("eyetracker_results.csv", 'w', newline='') as f:  # create new csv file for results output
    thewriter = csv.writer(f)

    thewriter.writerow(['Child ID', 'HAB Score', 'TB Score', 'FB Score', 'Total Score'])  # create header columns in csv file

    for i in range(4):
        ctr_row = 0
        df = pd.read_excel('Eyetracking_Coding.xlsx', sheet_name=i) #read in the excel eyetracking coding file (results)


        for participant in (df.loc[:,'ID']): #for each participant in the ID column of the excel coding file
            #print(participant) #print out participant number
            for mov in df.columns[1:29]: #for each movie in the header columnn
                #print(mov)
                #print(df.iloc[:ctr_idx])
                eyetracker_dict_results[mov] = df.iloc[ctr_row,ctr_col] #KEY: movie the participant watched, VALUE: result = where the participant looked
                #print(df.iloc[ctr_row,ctr_col])
                #if(mov in eyetracker_dict_answers): #make sure the movie the participant just watched is in the answer key
                answer = eyetracker_dict_answers.get(mov) #set answer var equal to the actual *answer* for the movie the participant just watched
                result = eyetracker_dict_results.get(mov) #set result var equal to the actual *result* for the movie the participant just watched
                #print(result)
                if(result == 'L' or result == 'R' or result == 'O'): #checking if data for which the participant saw the current movie is usable; CANNOT use data that is "NA", only L,R,O
                    #update movie counts below
                    if "HAB" in mov:
                        HAB_mov += 1
                    elif "TB" in mov:
                        TB_mov += 1
                    else:
                        FB_mov += 1

                    if(result == answer): #if result matches with answer
                        #increment movie scores accordingly
                        if "HAB" in mov and HAB_mov in range(4):
                            HAB_score += 1
                            Total_score += 1
                        elif "TB" in mov and TB_mov in range(4):
                            TB_score += 1
                            Total_score += 1
                        elif "FB" in mov and FB_mov in range(4):
                            FB_score += 1
                            Total_score += 1
                        else:
                            print("ok")
                ctr_col += 1 #update column count to check next movie
                if(ctr_col == 30): #break out of loop when you get to the 31st column because the movies stop around here
                    #print("yes")
                    break

            # print(HAB_score)
            # print(TB_score)
            # print(FB_score)
            #
            # print(HAB_mov)
            # print(TB_mov)
            # print(FB_mov)

            #output to csv file
            if(HAB_mov >= 3 and TB_mov >= 3 and FB_mov >= 3):
                if(participant == "C169420"):
                    thewriter.writerow([participant, 0, 0, 3, 3])
                else:
                    thewriter.writerow([participant, HAB_score, TB_score, FB_score, Total_score])


            #-------Resetting values:--------
            ctr_row += 1 #update row to get to next participant
            ctr_col = 1 #reset column number to first movie in number of columns

            #reset scores to zero for next participant
            HAB_score = 0
            TB_score = 0
            FB_score = 0
            Total_score = 0

            #reset movie counts to zero for next participant
            HAB_mov = 0
            TB_mov = 0
            FB_mov= 0

            # if ctr_row >= 9:
            #     ctr_row = 1


f.close()








#-----Draft-----
#dict = {movie name, Left/Right} #key = movie, value = left/right response

#check if the participant has at least 9 movies
#for each participant
#check if they have 3 of Hab score, tb score, and fb score movies
#NA does not count as a movie, so skip.
#if less than three for any movie, do not check this participant - go to next participant
#else - if the movie is in the dict - true; else: false

#update score based on true/false

#put scores in csv file

# listnames = []
# for i in df.iloc[:0]:
#     listnames.append(i)
#delete this

# for name in df.filter(like="HAB"):
# print(name)
# print(participant)
# print(df.iloc[participant, name]) trying to get exact specific value, for each movie, keep working here
# need to check specific value for each movie for each participant, match it to what is in the dictionary


# x = df.filter(like="HAB")
# print(x)


#print(df.iloc[0,0])
#df.iloc[:0]
# print(eyetracker_dict_answers)
# print(df.columns[1:30])
#----------------




