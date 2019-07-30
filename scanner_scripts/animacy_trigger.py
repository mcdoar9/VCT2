#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on Wed Apr 25 12:30:46 2018
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import random # to randomize viewing order

LUMINA = 1
LUMINA_TRIGGER = 3

## initialize communication with the lumina
'''
if LUMINA == 1:
    import pyxid # to interact with the Lumina box
    import sys

    ## initialize communication with the lumina
    devices=pyxid.get_xid_devices()

    if devices:
        lumina_dev=devices[0]
    else:
        print "Could not find Lumina device"
        sys.exit(1)

    print lumina_dev
    if lumina_dev.is_response_device():
        lumina_dev.reset_base_timer()
        lumina_dev.reset_rt_timer()
    else:
        print "Error: Lumina device is not a response device??"
        log.write("Error: Lumina device is not a response device??")
        sys.exit(1)
'''
        
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'animacy'  # from the Builder filename that created this script
expInfo = {'participant':'', 'randomization (1 = control, 2 = social)':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text_instruct = visual.TextStim(win=win, name='text_instruct',
    text=u'\nIn this task you will be viewing a series of videos. \nPlease watch the videos and remain still.',
    font=u'Arial',
    pos=(0, 0), height=0.18, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "sv01"
sv01Clock = core.Clock()

# Initialize components for Routine "sv02"
sv02Clock = core.Clock()

# Initialize components for Routine "sv03"
sv03Clock = core.Clock()

# Initialize components for Routine "sv04"
sv04Clock = core.Clock()

# Initialize components for Routine "sv05"
sv05Clock = core.Clock()

# Initialize components for Routine "sv06"
sv06Clock = core.Clock()

# Initialize components for Routine "sv07"
sv07Clock = core.Clock()

# Initialize components for Routine "sv08"
sv08Clock = core.Clock()

# Initialize components for Routine "cv01"
cv01Clock = core.Clock()

# Initialize components for Routine "cv02"
cv02Clock = core.Clock()

# Initialize components for Routine "cv03"
cv03Clock = core.Clock()

# Initialize components for Routine "cv04"
cv04Clock = core.Clock()

# Initialize components for Routine "cv05"
cv05Clock = core.Clock()

# Initialize components for Routine "cv06"
cv06Clock = core.Clock()

# Initialize components for Routine "cv07"
cv07Clock = core.Clock()

# Initialize components for Routine "cv08"
cv08Clock = core.Clock()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruction"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(text_instruct)
instructionsComponents.append(key_resp_2)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instruction"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instruct* updates
    if t >= 0.0 and text_instruct.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instruct.tStart = t  # underestimates by a little under one frame
        text_instruct.frameNStart = frameN  # exact frame index
        text_instruct.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clock.reset()  # now t=0
        event.clearEvents()
        theseKeys=[]
        if LUMINA==1:
            break; #sarah added this 
            #lumina_dev.clear_response_queue()
    if key_resp_2.status == STARTED:
        # check for a LUMINA_TRIGGER from the Lumina box
        if LUMINA == 1:
            theseKeys=[]
            lumina_dev.poll_for_response()
            while lumina_dev.response_queue_size() > 0:
                response = lumina_dev.get_next_response() 
                if response["pressed"]:
                    print "Lumina received: %s, %d"%(response["key"],response["key"])
                    if response["key"] == 3: 
                        theseKeys.append(str(response["key"]))
        else:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
        
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruction"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Randomization 1 (control first)
if (expInfo['randomization (1 = control, 2 = social)'] == '1'):
    # Set up lists shuffling 
    svList = ['sv01', 'sv02', 'sv03', 'sv04', 'sv05', 'sv06', 'sv07', 'sv08']
    cvList = ['cv01', 'cv02', 'cv03', 'cv04', 'cv05', 'cv06', 'cv07', 'cv08']
    
    random.shuffle(cvList)
    random.shuffle(svList)
    combinedList = [cvList[0], svList[0], cvList[1], svList[1], cvList[2], svList[2], cvList[3], svList[3], cvList[4], svList[4], cvList[5], svList[5], cvList[6], svList[6], cvList[7], svList[7]]
    
    # write a .txt file to record participant's viewing order
    file = open("Participant" + expInfo['participant'] +"VideoList.txt", "w+")
    file.write("Randomization 1: begin with Control video" + '\n')
    file.close()
    
    # make the file for c videos
    file = open("Participant" + expInfo['participant'] +"c_videos.txt", "w+")
    file.close()
    
    # make the file for the s videos
    file = open("Participant" + expInfo['participant'] +"s_videos.txt", "w+")
    file.close()
    """
    added by sarah
    """
    videoClock = core.Clock()  # to get times for txt files, will time all videos and get their stop/start times
    videoClock.reset()
    # begin playing videos in combinedList
    for video in combinedList:
        if (video == 'cv01'): 
            # ------Prepare to start Routine "cv01"-------
            t = 0
            cv01Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie = visual.MovieStim3(
                win=win, name='movie',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv01.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv01Components = [movie]
            for thisComponent in cv01Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv01"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv01Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie* updates
                if t >= 0.0 and movie.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie.tStart = t
                    movie.frameNStart = frameN  # exact frame index
                    movie.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie.status == STARTED and t >= frameRemains:
                    movie.setAutoDraw(False)
                if movie.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv01Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv01"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            for thisComponent in cv01Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv02'): 
            # ------Prepare to start Routine "cv02"-------
            t = 0
            cv02Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_2 = visual.MovieStim3(
                win=win, name='movie_2',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/Stimuli/cv02.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv02Components = [movie_2]
            for thisComponent in cv02Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv02"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close()
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv02Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_2* updates
                if t >= 0.0 and movie_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_2.tStart = t
                    movie_2.frameNStart = frameN  # exact frame index
                    movie_2.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_2.status == STARTED and t >= frameRemains:
                    movie_2.setAutoDraw(False)
                if movie_2.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv02Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv02"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            for thisComponent in cv02Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv03'):
            # ------Prepare to start Routine "cv03"-------
            t = 0
            cv03Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_3 = visual.MovieStim3(
                win=win, name='movie_3',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/Stimuli/cv03.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv03Components = [movie_3]
            for thisComponent in cv03Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv03"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv03Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_3* updates
                if t >= 0.0 and movie_3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_3.tStart = t
                    movie_3.frameNStart = frameN  # exact frame index
                    movie_3.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_3.status == STARTED and t >= frameRemains:
                    movie_3.setAutoDraw(False)
                if movie_3.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv03Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv03"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            for thisComponent in cv03Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv04'): 
            # ------Prepare to start Routine "cv04"-------
            t = 0
            cv04Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_4 = visual.MovieStim3(
                win=win, name='movie_4',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv04.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv04Components = [movie_4]
            for thisComponent in cv04Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv04"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv04Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_4* updates
                if t >= 0.0 and movie_4.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_4.tStart = t
                    movie_4.frameNStart = frameN  # exact frame index
                    movie_4.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_4.status == STARTED and t >= frameRemains:
                    movie_4.setAutoDraw(False)
                if movie_4.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv04Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv04"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            for thisComponent in cv04Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv05'): 
            # ------Prepare to start Routine "cv05"-------
            t = 0
            cv05Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_5 = visual.MovieStim3(
                win=win, name='movie_5',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv05.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv05Components = [movie_5]
            for thisComponent in cv05Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv05"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv05Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_5* updates
                if t >= 0.0 and movie_5.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_5.tStart = t
                    movie_5.frameNStart = frameN  # exact frame index
                    movie_5.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_5.status == STARTED and t >= frameRemains:
                    movie_5.setAutoDraw(False)
                if movie_5.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv05Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv05"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            for thisComponent in cv05Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv06'): 
            # ------Prepare to start Routine "cv06"-------
            t = 0
            cv06Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_6 = visual.MovieStim3(
                win=win, name='movie_6',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv06.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv06Components = [movie_6]
            for thisComponent in cv06Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv06"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv06Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_6* updates
                if t >= 0.0 and movie_6.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_6.tStart = t
                    movie_6.frameNStart = frameN  # exact frame index
                    movie_6.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_6.status == STARTED and t >= frameRemains:
                    movie_6.setAutoDraw(False)
                if movie_6.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv06Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv06"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in cv06Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv07'):
            # ------Prepare to start Routine "cv07"-------
            t = 0
            cv07Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_7 = visual.MovieStim3(
                win=win, name='movie_7',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv07.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv07Components = [movie_7]
            for thisComponent in cv07Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv07"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv07Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_7* updates
                if t >= 0.0 and movie_7.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_7.tStart = t
                    movie_7.frameNStart = frameN  # exact frame index
                    movie_7.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_7.status == STARTED and t >= frameRemains:
                    movie_7.setAutoDraw(False)
                if movie_7.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv07Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv07"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in cv07Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv08'): 
            # ------Prepare to start Routine "cv08"-------
            t = 0
            cv08Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_8 = visual.MovieStim3(
                win=win, name='movie_8',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv08.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv08Components = [movie_8]
            for thisComponent in cv08Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv08"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv08Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_8* updates
                if t >= 0.0 and movie_8.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_8.tStart = t
                    movie_8.frameNStart = frameN  # exact frame index
                    movie_8.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_8.status == STARTED and t >= frameRemains:
                    movie_8.setAutoDraw(False)
                if movie_8.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv08Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv08"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in cv08Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
        
        elif (video == 'sv01'): 
            # ------Prepare to start Routine "sv01"-------
            t = 0
            sv01Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(15.000000)
            # update component parameters for each repeat
            movie_9 = visual.MovieStim3(
                win=win, name='movie_9',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv01.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv01Components = [movie_9]
            for thisComponent in sv01Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv01"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv01Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_9* updates
                if t >= 0.0 and movie_9.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_9.tStart = t
                    movie_9.frameNStart = frameN  # exact frame index
                    movie_9.setAutoDraw(True)
                frameRemains = 0.0 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_9.status == STARTED and t >= frameRemains:
                    movie_9.setAutoDraw(False)
                if movie_9.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv01Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv01"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv01Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'sv02'): 
            # ------Prepare to start Routine "sv02"-------
            t = 0
            sv02Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_10 = visual.MovieStim3(
                win=win, name='movie_10',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv02.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv02Components = [movie_10]
            for thisComponent in sv02Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv02"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv02Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_10* updates
                if t >= 0.0 and movie_10.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_10.tStart = t
                    movie_10.frameNStart = frameN  # exact frame index
                    movie_10.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_10.status == STARTED and t >= frameRemains:
                    movie_10.setAutoDraw(False)
                if movie_10.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv02Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv02"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv02Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'sv03'): 
            # ------Prepare to start Routine "sv03"-------
            t = 0
            sv03Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_11 = visual.MovieStim3(
                win=win, name='movie_11',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv03.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv03Components = [movie_11]
            for thisComponent in sv03Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv03"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv03Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_11* updates
                if t >= 0.0 and movie_11.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_11.tStart = t
                    movie_11.frameNStart = frameN  # exact frame index
                    movie_11.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_11.status == STARTED and t >= frameRemains:
                    movie_11.setAutoDraw(False)
                if movie_11.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv03Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv03"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv03Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

        elif (video == 'sv04'): 
            # ------Prepare to start Routine "sv04"-------
            t = 0
            sv04Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_12 = visual.MovieStim3(
                win=win, name='movie_12',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv04.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv04Components = [movie_12]
            for thisComponent in sv04Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv04"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv04Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_12* updates
                if t >= 0.0 and movie_12.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_12.tStart = t
                    movie_12.frameNStart = frameN  # exact frame index
                    movie_12.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_12.status == STARTED and t >= frameRemains:
                    movie_12.setAutoDraw(False)
                if movie_12.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv04Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv04"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv04Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

        elif (video == 'sv05'): 
            # ------Prepare to start Routine "sv05"-------
            t = 0
            sv05Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(15.000000)
            # update component parameters for each repeat
            movie_13 = visual.MovieStim3(
                win=win, name='movie_13',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv05.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv05Components = [movie_13]
            for thisComponent in sv05Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv05"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv05Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_13* updates
                if t >= 0.0 and movie_13.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_13.tStart = t
                    movie_13.frameNStart = frameN  # exact frame index
                    movie_13.setAutoDraw(True)
                frameRemains = 0.0 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_13.status == STARTED and t >= frameRemains:
                    movie_13.setAutoDraw(False)
                if movie_13.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv05Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv05"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv05Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

        elif (video == 'sv06'): 
            # ------Prepare to start Routine "sv06"-------
            t = 0
            sv06Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_14 = visual.MovieStim3(
                win=win, name='movie_14',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv06.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv06Components = [movie_14]
            for thisComponent in sv06Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv06"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv06Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_14* updates
                if t >= 0.0 and movie_14.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_14.tStart = t
                    movie_14.frameNStart = frameN  # exact frame index
                    movie_14.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_14.status == STARTED and t >= frameRemains:
                    movie_14.setAutoDraw(False)
                if movie_14.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv06Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv06"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv06Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

        elif (video == 'sv07'): 
            # ------Prepare to start Routine "sv07"-------
            t = 0
            sv07Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_15 = visual.MovieStim3(
                win=win, name='movie_15',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv07.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv07Components = [movie_15]
            for thisComponent in sv07Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv07"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv07Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_15* updates
                if t >= 0.0 and movie_15.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_15.tStart = t
                    movie_15.frameNStart = frameN  # exact frame index
                    movie_15.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_15.status == STARTED and t >= frameRemains:
                    movie_15.setAutoDraw(False)
                if movie_15.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv07Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv07"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv07Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

        elif (video == 'sv08'): 
            # ------Prepare to start Routine "sv08"-------
            t = 0
            sv08Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_16 = visual.MovieStim3(
                win=win, name='movie_16',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv08.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv08Components = [movie_16]
            for thisComponent in sv08Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv08"-------
            """
            added by sarah
            """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv08Clock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_16* updates
                if t >= 0.0 and movie_16.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_16.tStart = t
                    movie_16.frameNStart = frameN  # exact frame index
                    movie_16.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_16.status == STARTED and t >= frameRemains:
                    movie_16.setAutoDraw(False)
                if movie_16.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv08Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv08"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv08Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

#Randomization 2 (social first)
if (expInfo['randomization (1 = control, 2 = social)'] == '2'):
    # Set up lists shuffling 
    svList = ['sv01', 'sv02', 'sv03', 'sv04', 'sv05', 'sv06', 'sv07', 'sv08']
    cvList = ['cv01', 'cv02', 'cv03', 'cv04', 'cv05', 'cv06', 'cv07', 'cv08']
    
    random.shuffle(svList)
    random.shuffle(cvList)
    combinedList = [svList[0], cvList[0], svList[1], cvList[1], svList[2], cvList[2], svList[3], cvList[3], svList[4], cvList[4], svList[5], cvList[5], svList[6], cvList[6], svList[7], cvList[7]]
    
    # write a .txt file to record participant's viewing order
    file = open("Participant" + expInfo['participant'] +"VideoList.txt", "w+")
    file.write("Randomization 2: begin with Social video" + '\n')
    file.close()
    
    # make the file for c videos
    file = open("Participant" + expInfo['participant'] +"c_videos.txt", "w+")
    file.close()
    
    # make the file for the s videos
    file = open("Participant" + expInfo['participant'] +"s_videos.txt", "w+")
    file.close()
    """
    added by sarah
    """
    videoClock = core.Clock()  # to get times for txt files, will time all videos and get their stop/start times
    videoClock.reset()
    # begin playing videos in combinedList
    for video in combinedList:  
        if (video == 'sv01'): 
            # ------Prepare to start Routine "sv01"-------
            t = 0
            sv01Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(15.000000)
            # update component parameters for each repeat
            movie_9 = visual.MovieStim3(
                win=win, name='movie_9',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv01.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv01Components = [movie_9]
            for thisComponent in sv01Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv01"-------
                """
                added by sarah
                """
            #write to master
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv01Clock.getTime()

                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_9* updates
                if t >= 0.0 and movie_9.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_9.tStart = t
                    movie_9.frameNStart = frameN  # exact frame index
                    movie_9.setAutoDraw(True)
                frameRemains = 0.0 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_9.status == STARTED and t >= frameRemains:
                    movie_9.setAutoDraw(False)
                if movie_9.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv01Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv01"-------
            """
            added by sarah
            """
            #write to master
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv01Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'sv02'): 
            # ------Prepare to start Routine "sv02"-------
            t = 0
            sv02Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_10 = visual.MovieStim3(
                win=win, name='movie_10',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv02.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv02Components = [movie_10]
            for thisComponent in sv02Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv02"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round( vidStartTime, 3) )+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv02Clock.getTime()
             
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_10* updates
                if t >= 0.0 and movie_10.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_10.tStart = t
                    movie_10.frameNStart = frameN  # exact frame index
                    movie_10.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_10.status == STARTED and t >= frameRemains:
                    movie_10.setAutoDraw(False)
                if movie_10.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv02Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv02"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv02Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'sv03'): 
            # ------Prepare to start Routine "sv03"-------
            t = 0
            sv03Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_11 = visual.MovieStim3(
                win=win, name='movie_11',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv03.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv03Components = [movie_11]
            for thisComponent in sv03Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv03"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3) )+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv03Clock.getTime()
                
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_11* updates
                if t >= 0.0 and movie_11.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_11.tStart = t
                    movie_11.frameNStart = frameN  # exact frame index
                    movie_11.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_11.status == STARTED and t >= frameRemains:
                    movie_11.setAutoDraw(False)
                if movie_11.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv03Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv03"-------
            """
            added by sarah
            """
            #write to master file
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv03Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

        elif (video == 'sv04'): 
            # ------Prepare to start Routine "sv04"-------
            t = 0
            sv04Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_12 = visual.MovieStim3(
                win=win, name='movie_12',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv04.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv04Components = [movie_12]
            for thisComponent in sv04Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv04"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round( vidStartTime, 3) )+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv04Clock.getTime()

                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_12* updates
                if t >= 0.0 and movie_12.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_12.tStart = t
                    movie_12.frameNStart = frameN  # exact frame index
                    movie_12.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_12.status == STARTED and t >= frameRemains:
                    movie_12.setAutoDraw(False)
                if movie_12.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv04Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv04"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv04Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

        elif (video == 'sv05'): 
            # ------Prepare to start Routine "sv05"-------
            t = 0
            sv05Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(15.000000)
            # update component parameters for each repeat
            movie_13 = visual.MovieStim3(
                win=win, name='movie_13',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv05.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv05Components = [movie_13]
            for thisComponent in sv05Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv05"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round( vidStartTime, 3) )+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv05Clock.getTime()

                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_13* updates
                if t >= 0.0 and movie_13.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_13.tStart = t
                    movie_13.frameNStart = frameN  # exact frame index
                    movie_13.setAutoDraw(True)
                frameRemains = 0.0 + 15- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_13.status == STARTED and t >= frameRemains:
                    movie_13.setAutoDraw(False)
                if movie_13.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv05Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv05"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv05Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

        elif (video == 'sv06'): 
            # ------Prepare to start Routine "sv06"-------
            t = 0
            sv06Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_14 = visual.MovieStim3(
                win=win, name='movie_14',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv06.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv06Components = [movie_14]
            for thisComponent in sv06Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv06"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round( vidStartTime, 3) )+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv06Clock.getTime()

                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_14* updates
                if t >= 0.0 and movie_14.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_14.tStart = t
                    movie_14.frameNStart = frameN  # exact frame index
                    movie_14.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_14.status == STARTED and t >= frameRemains:
                    movie_14.setAutoDraw(False)
                if movie_14.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv06Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv06"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv06Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

        elif (video == 'sv07'): 
            # ------Prepare to start Routine "sv07"-------
            t = 0
            sv07Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_15 = visual.MovieStim3(
                win=win, name='movie_15',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv07.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv07Components = [movie_15]
            for thisComponent in sv07Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv07"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round( vidStartTime,3) )+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv07Clock.getTime()
                
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_15* updates
                if t >= 0.0 and movie_15.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_15.tStart = t
                    movie_15.frameNStart = frameN  # exact frame index
                    movie_15.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_15.status == STARTED and t >= frameRemains:
                    movie_15.setAutoDraw(False)
                if movie_15.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv07Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv07"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv07Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

        elif (video == 'sv08'): 
            # ------Prepare to start Routine "sv08"-------
            t = 0
            sv08Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_16 = visual.MovieStim3(
                win=win, name='movie_16',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/sv08.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            sv08Components = [movie_16]
            for thisComponent in sv08Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "sv08"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime,3))+ '\t')
            file.close() 
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = sv08Clock.getTime()

                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_16* updates
                if t >= 0.0 and movie_16.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_16.tStart = t
                    movie_16.frameNStart = frameN  # exact frame index
                    movie_16.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_16.status == STARTED and t >= frameRemains:
                    movie_16.setAutoDraw(False)
                if movie_16.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in sv08Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "sv08"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close()  
            #write to s videos file
            file = open("Participant" + expInfo['participant'] +"s_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in sv08Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv01'): 
            # ------Prepare to start Routine "cv01"-------
            t = 0
            cv01Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie = visual.MovieStim3(
                win=win, name='movie',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv01.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv01Components = [movie]
            for thisComponent in cv01Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv01"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime,3) )+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv01Clock.getTime()

                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie* updates
                if t >= 0.0 and movie.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie.tStart = t
                    movie.frameNStart = frameN  # exact frame index
                    movie.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie.status == STARTED and t >= frameRemains:
                    movie.setAutoDraw(False)
                if movie.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv01Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv01"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in cv01Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv02'): 
            # ------Prepare to start Routine "cv02"-------
            t = 0
            cv02Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_2 = visual.MovieStim3(
                win=win, name='movie_2',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv02.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv02Components = [movie_2]
            for thisComponent in cv02Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv02"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime,3))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv02Clock.getTime()

                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_2* updates
                if t >= 0.0 and movie_2.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_2.tStart = t
                    movie_2.frameNStart = frameN  # exact frame index
                    movie_2.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_2.status == STARTED and t >= frameRemains:
                    movie_2.setAutoDraw(False)
                if movie_2.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv02Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv02"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in cv02Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv03'):
            # ------Prepare to start Routine "cv03"-------
            t = 0
            cv03Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_3 = visual.MovieStim3(
                win=win, name='movie_3',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv03.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv03Components = [movie_3]
            for thisComponent in cv03Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv03"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime,3))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv03Clock.getTime()
                
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_3* updates
                if t >= 0.0 and movie_3.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_3.tStart = t
                    movie_3.frameNStart = frameN  # exact frame index
                    movie_3.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_3.status == STARTED and t >= frameRemains:
                    movie_3.setAutoDraw(False)
                if movie_3.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv03Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv03"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in cv03Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv04'): 
            # ------Prepare to start Routine "cv04"-------
            t = 0
            cv04Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_4 = visual.MovieStim3(
                win=win, name='movie_4',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv04.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv04Components = [movie_4]
            for thisComponent in cv04Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv04"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime,3))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 

            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv04Clock.getTime()
       
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_4* updates
                if t >= 0.0 and movie_4.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_4.tStart = t
                    movie_4.frameNStart = frameN  # exact frame index
                    movie_4.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_4.status == STARTED and t >= frameRemains:
                    movie_4.setAutoDraw(False)
                if movie_4.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv04Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv04"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close()  
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in cv04Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv05'): 
            # ------Prepare to start Routine "cv05"-------
            t = 0
            cv05Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_5 = visual.MovieStim3(
                win=win, name='movie_5',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv05.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv05Components = [movie_5]
            for thisComponent in cv05Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv05"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv05Clock.getTime()
                
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_5* updates
                if t >= 0.0 and movie_5.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_5.tStart = t
                    movie_5.frameNStart = frameN  # exact frame index
                    movie_5.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_5.status == STARTED and t >= frameRemains:
                    movie_5.setAutoDraw(False)
                if movie_5.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv05Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv05"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in cv05Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv06'): 
            # ------Prepare to start Routine "cv06"-------
            t = 0
            cv06Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_6 = visual.MovieStim3(
                win=win, name='movie_6',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv06.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv06Components = [movie_6]
            for thisComponent in cv06Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv06"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime,3))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv06Clock.getTime()
                
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_6* updates
                if t >= 0.0 and movie_6.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_6.tStart = t
                    movie_6.frameNStart = frameN  # exact frame index
                    movie_6.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_6.status == STARTED and t >= frameRemains:
                    movie_6.setAutoDraw(False)
                if movie_6.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv06Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv06"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in cv06Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv07'):
            # ------Prepare to start Routine "cv07"-------
            t = 0
            cv07Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_7 = visual.MovieStim3(
                win=win, name='movie_7',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv07.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv07Components = [movie_7]
            for thisComponent in cv07Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv07"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime,3))+ '\t')
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv07Clock.getTime()
                
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_7* updates
                if t >= 0.0 and movie_7.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_7.tStart = t
                    movie_7.frameNStart = frameN  # exact frame index
                    movie_7.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_7.status == STARTED and t >= frameRemains:
                    movie_7.setAutoDraw(False)
                if movie_7.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv07Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv07"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in cv07Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
                    
        elif (video == 'cv08'): 
            # ------Prepare to start Routine "cv08"-------
            t = 0
            cv08Clock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(16.000000)
            # update component parameters for each repeat
            movie_8 = visual.MovieStim3(
                win=win, name='movie_8',
                filename=u'/Users/MRIPsychology/Documents/MATLAB/Experiments/Child/stimuli/cv08.mov',
                ori=0, pos=(0, 0), opacity=1,
                depth=0.0,
                )
            # keep track of which components have finished
            cv08Components = [movie_8]
            for thisComponent in cv08Components:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED

            # -------Start Routine "cv08"-------
                """
                added by sarah
                """
            vidStartTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime,3))+ '\t')
            file.close()            
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+") #a for append
            file.write(video + '\t' + str( round(vidStartTime, 3 ))+ '\t')
            file.close() 
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cv08Clock.getTime()
              
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *movie_8* updates
                if t >= 0.0 and movie_8.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    movie_8.tStart = t
                    movie_8.frameNStart = frameN  # exact frame index
                    movie_8.setAutoDraw(True)
                frameRemains = 0.0 + 16- win.monitorFramePeriod * 0.75  # most of one frame period left
                if movie_8.status == STARTED and t >= frameRemains:
                    movie_8.setAutoDraw(False)
                if movie_8.status == FINISHED:  # force-end the routine
                    continueRoutine = False
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cv08Components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()

            # -------Ending Routine "cv08"-------
            """
            added by sarah
            """
            vidEndTime= videoClock.getTime()
            file = open("Participant" + expInfo['participant'] +"VideoList.txt", "a+") #a for append            
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\n') 
            file.close() 
            #write to c videos file
            file = open("Participant" + expInfo['participant'] +"c_videos.txt", "a+")
            file.write( str( round(vidEndTime, 3) )+ '\t')
            file.write( str( round( (vidEndTime - vidStartTime),3) )+ '\t') 
            file.write( "1" + '\n' )
            file.close() 
            
            for thisComponent in cv08Components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
