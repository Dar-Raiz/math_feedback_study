#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.2),
    on January 07, 2025, at 09:46
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.2'
expName = 'DAR_MATH'  # from the Builder filename that created this script
expInfo = {
    'RUID': 'INPUT RUID HERE',
    'Email Address': 'INPUT EMAIL ADDRESS HERE',
    'First Name': 'INPUT FIRST NAME HERE',
    'Last Name': 'INPUT LAST NAME HERE',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['First Name'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\daria\\OneDrive\\Documents\\Psychopy\\Math_feedback_study1\\Math_feedback_study1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1440, 960], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "Instruct" ---
text_5 = visual.TextStim(win=win, name='text_5',
    text='Introduction\n\nFor this experiment, you will be solving math multiplication problems in your head. Our primary goal is to understand how well college students perform mental arithmetic.  \n\nTo maintain the integrity of our experiment we respectfully ask please DO NOT USE a cell phone, calculator, or pen/paper for this experiment. We want you to try and do everything in your head. \n\n\nPress ‘t’ to continue to the next page\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "Prac_instruct" ---
text_8 = visual.TextStim(win=win, name='text_8',
    text='Practice Round\n\nFirst you will do a simple practice round consisting of 4 questions. You must get at least 3 questions correct in order to advance to the main task.\n \nYou will see a multiplication problem presented at the top of the screen with two possible choices underneath it. Your job is to pick the correct answer. You will have 4 seconds to make each response before moving onto the next trial.\n\nExample\n\n  8 x 1 =\n\n  a) 8\n  b) 1\n\nTo pick response a) press the ‘1’ key. \nTo pick response b) press the ‘2’ key.\n\nPress ‘1’ or ‘2’ to begin the practice round.\n',
    font='Arial',
    pos=(0, 0), height=0.036, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# --- Initialize components for Routine "GetReady" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    units='height', pos=(0, 0), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text=None,
    font='Arial',
    pos=(0, 10), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "GetReady" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    units='height', pos=(0, 0), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text=None,
    font='Arial',
    pos=(0, 10), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ChooseFbk" ---
fbkcosttext = visual.TextStim(win=win, name='fbkcosttext',
    text='',
    font='Arial',
    pos=(0, .3), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
StudyView_topsideword_4 = visual.TextStim(win=win, name='StudyView_topsideword_4',
    text='',
    font='Arial',
    pos=(0, .1), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
StudyView1_bottomsideword_4 = visual.TextStim(win=win, name='StudyView1_bottomsideword_4',
    text='',
    font='Arial',
    pos=(0, -.05), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Test3response2 = keyboard.Keyboard()

# --- Initialize components for Routine "ShowResp" ---
highlightbox_showresp = visual.Rect(
    win=win, name='highlightbox_showresp',
    width=(.33, .12)[0], height=(.33, .12)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=6,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=0.0, interpolate=True)
Fbk_target_showresp = visual.TextStim(win=win, name='Fbk_target_showresp',
    text='',
    font='Arial',
    pos=(0, .3), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Fbk_topsideword_showresp = visual.TextStim(win=win, name='Fbk_topsideword_showresp',
    text='',
    font='Arial',
    pos=(0,.1), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Fbk_bottomsideword_showresp = visual.TextStim(win=win, name='Fbk_bottomsideword_showresp',
    text='',
    font='Arial',
    pos=(0, -.05), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0, -.285], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
Error_message2 = visual.TextStim(win=win, name='Error_message2',
    text='',
    font='Arial',
    pos=(0, .2), height=.075, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "repeat_instruct" ---
text_7 = visual.TextStim(win=win, name='text_7',
    text='Please Try Again\n\nYou got less than 3 correct responses during the practice round. In order to advance to the main task, you need to get at least 3 correct responses during the practice round. \n\nRemember, to pick response a) press the ‘1’ key. To pick response b) press the ‘2’ key.\n\n\nPress ‘t’ to restart the practice round.\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "EndPart2" ---
text_2 = visual.TextStim(win=win, name='text_2',
    text='You passed the practice task!\n\nPress ‘t’ to advance to the main task instructions\n',
    font='Arial',
    pos=(0, 0), height=.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
contpart2_2 = keyboard.Keyboard()

# --- Initialize components for Routine "Instruct2" ---
text_6 = visual.TextStim(win=win, name='text_6',
    text='Main Task\n\nNow that you have gotten a feel for the task, you are now ready for the real test. You will again see multiplication problems like before, however these problems will range in their difficulty. You will have 4 seconds to make each response.\n\nPlease try your best to calculate the correct response instead of guessing.  \n\nExample\n\n12 x 2 =\n\na) 22\nb) 24\n\nTo pick response a) press the ‘1’ key. \nTo pick response b) press the ‘2’ key.\n\n\nPress ‘1’ or ‘2’ to begin the main task.',
    font='Arial',
    pos=(0, 0), height=0.033, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# --- Initialize components for Routine "GetReady" ---
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    units='height', pos=(0, 0), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text=None,
    font='Arial',
    pos=(0, 10), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "ChooseFbk" ---
fbkcosttext = visual.TextStim(win=win, name='fbkcosttext',
    text='',
    font='Arial',
    pos=(0, .3), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
StudyView_topsideword_4 = visual.TextStim(win=win, name='StudyView_topsideword_4',
    text='',
    font='Arial',
    pos=(0, .1), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
StudyView1_bottomsideword_4 = visual.TextStim(win=win, name='StudyView1_bottomsideword_4',
    text='',
    font='Arial',
    pos=(0, -.05), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
Test3response2 = keyboard.Keyboard()

# --- Initialize components for Routine "ShowResp" ---
highlightbox_showresp = visual.Rect(
    win=win, name='highlightbox_showresp',
    width=(.33, .12)[0], height=(.33, .12)[1],
    ori=0, pos=[0,0], anchor='center',
    lineWidth=6,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1, depth=0.0, interpolate=True)
Fbk_target_showresp = visual.TextStim(win=win, name='Fbk_target_showresp',
    text='',
    font='Arial',
    pos=(0, .3), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Fbk_topsideword_showresp = visual.TextStim(win=win, name='Fbk_topsideword_showresp',
    text='',
    font='Arial',
    pos=(0,.1), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
Fbk_bottomsideword_showresp = visual.TextStim(win=win, name='Fbk_bottomsideword_showresp',
    text='',
    font='Arial',
    pos=(0, -.05), height=.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=[0, -.285], size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
Error_message2 = visual.TextStim(win=win, name='Error_message2',
    text='',
    font='Arial',
    pos=(0, .2), height=.075, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "EndPart1" ---
text = visual.TextStim(win=win, name='text',
    text="That was the end of the task. \n\nTo finish the experiment press 't', then complete a brief questionnaire. \n\n",
    font='Arial',
    pos=(0, 0), height=.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
contpart2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Instruct" ---
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructComponents = [text_5, key_resp]
for thisComponent in InstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instruct" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    
    # if text_5 is starting this frame...
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_5.started')
        # update status
        text_5.status = STARTED
        text_5.setAutoDraw(True)
    
    # if text_5 is active this frame...
    if text_5.status == STARTED:
        # update params
        pass
    
    # *key_resp* updates
    waitOnFlip = False
    
    # if key_resp is starting this frame...
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp.started')
        # update status
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['t'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruct" ---
for thisComponent in InstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Prac_instruct" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
Prac_instructComponents = [text_8, key_resp_5]
for thisComponent in Prac_instructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Prac_instruct" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    
    # if text_8 is starting this frame...
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_8.started')
        # update status
        text_8.status = STARTED
        text_8.setAutoDraw(True)
    
    # if text_8 is active this frame...
    if text_8.status == STARTED:
        # update params
        pass
    
    # *key_resp_5* updates
    waitOnFlip = False
    
    # if key_resp_5 is starting this frame...
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_5.started')
        # update status
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Prac_instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Prac_instruct" ---
for thisComponent in Prac_instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "Prac_instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "GetReady" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
GetReadyComponents = [fixation, text_4]
for thisComponent in GetReadyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "GetReady" ---
routineForceEnded = not continueRoutine
while continueRoutine and routineTimer.getTime() < 1.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fixation* updates
    
    # if fixation is starting this frame...
    if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fixation.frameNStart = frameN  # exact frame index
        fixation.tStart = t  # local t and not account for scr refresh
        fixation.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fixation.started')
        # update status
        fixation.status = STARTED
        fixation.setAutoDraw(True)
    
    # if fixation is active this frame...
    if fixation.status == STARTED:
        # update params
        pass
    
    # if fixation is stopping this frame...
    if fixation.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fixation.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            fixation.tStop = t  # not accounting for scr refresh
            fixation.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation.stopped')
            # update status
            fixation.status = FINISHED
            fixation.setAutoDraw(False)
    
    # *text_4* updates
    
    # if text_4 is starting this frame...
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_4.started')
        # update status
        text_4.status = STARTED
        text_4.setAutoDraw(True)
    
    # if text_4 is active this frame...
    if text_4.status == STARTED:
        # update params
        pass
    
    # if text_4 is stopping this frame...
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.stopped')
            # update status
            text_4.status = FINISHED
            text_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in GetReadyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "GetReady" ---
for thisComponent in GetReadyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-1.000000)

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=3.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=1, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('practice_Test.xlsx'),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2:
                exec('{} = thisTrial_2[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "GetReady" ---
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        GetReadyComponents = [fixation, text_4]
        for thisComponent in GetReadyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "GetReady" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            
            # if fixation is starting this frame...
            if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fixation.frameNStart = frameN  # exact frame index
                fixation.tStart = t  # local t and not account for scr refresh
                fixation.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.started')
                # update status
                fixation.status = STARTED
                fixation.setAutoDraw(True)
            
            # if fixation is active this frame...
            if fixation.status == STARTED:
                # update params
                pass
            
            # if fixation is stopping this frame...
            if fixation.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fixation.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    fixation.tStop = t  # not accounting for scr refresh
                    fixation.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fixation.stopped')
                    # update status
                    fixation.status = FINISHED
                    fixation.setAutoDraw(False)
            
            # *text_4* updates
            
            # if text_4 is starting this frame...
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.started')
                # update status
                text_4.status = STARTED
                text_4.setAutoDraw(True)
            
            # if text_4 is active this frame...
            if text_4.status == STARTED:
                # update params
                pass
            
            # if text_4 is stopping this frame...
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_4.stopped')
                    # update status
                    text_4.status = FINISHED
                    text_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in GetReadyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "GetReady" ---
        for thisComponent in GetReadyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "ChooseFbk" ---
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_2
        selectbox_color = 'white'
        response_record = ''
        CorrResp = 1
        r3reversed = []
        topside = CorrRespDig1
        botside = CorrRespDig2
        
        if random()>.5:
            topside = CorrRespDig1
            botside = CorrRespDig2
            r3reversed = False
            CorrResp = 1
        else:
            topside = CorrRespDig2
            botside = CorrRespDig1
            r3reversed = True
            CorrResp = 2
        
        thisExp.addData('r3reversed',r3reversed)
        thisExp.addData('CorrResp',CorrResp)
        thisExp.addData('topside',topside)
        thisExp.addData('botside',botside)
        fbkcosttext.setText(mathprob)
        StudyView_topsideword_4.setText('a) ' + topside)
        StudyView1_bottomsideword_4.setText('b) ' + botside

)
        Test3response2.keys = []
        Test3response2.rt = []
        _Test3response2_allKeys = []
        # keep track of which components have finished
        ChooseFbkComponents = [fbkcosttext, StudyView_topsideword_4, StudyView1_bottomsideword_4, Test3response2]
        for thisComponent in ChooseFbkComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ChooseFbk" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 4.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fbkcosttext* updates
            
            # if fbkcosttext is starting this frame...
            if fbkcosttext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fbkcosttext.frameNStart = frameN  # exact frame index
                fbkcosttext.tStart = t  # local t and not account for scr refresh
                fbkcosttext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fbkcosttext, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fbkcosttext.started')
                # update status
                fbkcosttext.status = STARTED
                fbkcosttext.setAutoDraw(True)
            
            # if fbkcosttext is active this frame...
            if fbkcosttext.status == STARTED:
                # update params
                pass
            
            # if fbkcosttext is stopping this frame...
            if fbkcosttext.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fbkcosttext.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    fbkcosttext.tStop = t  # not accounting for scr refresh
                    fbkcosttext.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'fbkcosttext.stopped')
                    # update status
                    fbkcosttext.status = FINISHED
                    fbkcosttext.setAutoDraw(False)
            
            # *StudyView_topsideword_4* updates
            
            # if StudyView_topsideword_4 is starting this frame...
            if StudyView_topsideword_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                StudyView_topsideword_4.frameNStart = frameN  # exact frame index
                StudyView_topsideword_4.tStart = t  # local t and not account for scr refresh
                StudyView_topsideword_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(StudyView_topsideword_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StudyView_topsideword_4.started')
                # update status
                StudyView_topsideword_4.status = STARTED
                StudyView_topsideword_4.setAutoDraw(True)
            
            # if StudyView_topsideword_4 is active this frame...
            if StudyView_topsideword_4.status == STARTED:
                # update params
                pass
            
            # if StudyView_topsideword_4 is stopping this frame...
            if StudyView_topsideword_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > StudyView_topsideword_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    StudyView_topsideword_4.tStop = t  # not accounting for scr refresh
                    StudyView_topsideword_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'StudyView_topsideword_4.stopped')
                    # update status
                    StudyView_topsideword_4.status = FINISHED
                    StudyView_topsideword_4.setAutoDraw(False)
            
            # *StudyView1_bottomsideword_4* updates
            
            # if StudyView1_bottomsideword_4 is starting this frame...
            if StudyView1_bottomsideword_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                StudyView1_bottomsideword_4.frameNStart = frameN  # exact frame index
                StudyView1_bottomsideword_4.tStart = t  # local t and not account for scr refresh
                StudyView1_bottomsideword_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(StudyView1_bottomsideword_4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StudyView1_bottomsideword_4.started')
                # update status
                StudyView1_bottomsideword_4.status = STARTED
                StudyView1_bottomsideword_4.setAutoDraw(True)
            
            # if StudyView1_bottomsideword_4 is active this frame...
            if StudyView1_bottomsideword_4.status == STARTED:
                # update params
                pass
            
            # if StudyView1_bottomsideword_4 is stopping this frame...
            if StudyView1_bottomsideword_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > StudyView1_bottomsideword_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    StudyView1_bottomsideword_4.tStop = t  # not accounting for scr refresh
                    StudyView1_bottomsideword_4.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'StudyView1_bottomsideword_4.stopped')
                    # update status
                    StudyView1_bottomsideword_4.status = FINISHED
                    StudyView1_bottomsideword_4.setAutoDraw(False)
            
            # *Test3response2* updates
            waitOnFlip = False
            
            # if Test3response2 is starting this frame...
            if Test3response2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                Test3response2.frameNStart = frameN  # exact frame index
                Test3response2.tStart = t  # local t and not account for scr refresh
                Test3response2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Test3response2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Test3response2.started')
                # update status
                Test3response2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Test3response2.clock.reset)  # t=0 on next screen flip
            
            # if Test3response2 is stopping this frame...
            if Test3response2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Test3response2.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    Test3response2.tStop = t  # not accounting for scr refresh
                    Test3response2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Test3response2.stopped')
                    # update status
                    Test3response2.status = FINISHED
                    Test3response2.status = FINISHED
            if Test3response2.status == STARTED and not waitOnFlip:
                theseKeys = Test3response2.getKeys(keyList=['1', '2'], waitRelease=False)
                _Test3response2_allKeys.extend(theseKeys)
                if len(_Test3response2_allKeys):
                    Test3response2.keys = _Test3response2_allKeys[-1].name  # just the last key pressed
                    Test3response2.rt = _Test3response2_allKeys[-1].rt
                    # was this correct?
                    if (Test3response2.keys == str(CorrResp)) or (Test3response2.keys == CorrResp):
                        Test3response2.corr = 1
                    else:
                        Test3response2.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from code_4
            respbox_y = -1
            keys = event.getKeys()
            if '1' in keys:
                respbox_y = .1
            elif '2' in keys:
                respbox_y = -.05
            
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ChooseFbkComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ChooseFbk" ---
        for thisComponent in ChooseFbkComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if Test3response2.keys in ['', [], None]:  # No response was made
            Test3response2.keys = None
            # was no response the correct answer?!
            if str(CorrResp).lower() == 'none':
               Test3response2.corr = 1;  # correct non-response
            else:
               Test3response2.corr = 0;  # failed to respond (incorrectly)
        # store data for trials_2 (TrialHandler)
        trials_2.addData('Test3response2.keys',Test3response2.keys)
        trials_2.addData('Test3response2.corr', Test3response2.corr)
        if Test3response2.keys != None:  # we had a response
            trials_2.addData('Test3response2.rt', Test3response2.rt)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-4.000000)
        
        # --- Prepare to start Routine "ShowResp" ---
        continueRoutine = True
        # update component parameters for each repeat
        highlightbox_showresp.setFillColor([-1.0000, -1.0000, -1.0000])
        highlightbox_showresp.setPos((0, respbox_y))
        highlightbox_showresp.setLineColor(selectbox_color)
        Fbk_target_showresp.setText(mathprob)
        Fbk_topsideword_showresp.setText('a) ' + topside)
        Fbk_bottomsideword_showresp.setText('b) ' + botside)
        # Run 'Begin Routine' code from code_7
        x = 0
        errormsg = ''
        if Test3response2.rt >= 0:
            fbkimagefile = 'blacksquare.png'
        else:
            fbkimagefile = 'noresponse.png'
            errormsg = 'please respond faster'
        
        image.setImage(fbkimagefile)
        Error_message2.setText(errormsg)
        # keep track of which components have finished
        ShowRespComponents = [highlightbox_showresp, Fbk_target_showresp, Fbk_topsideword_showresp, Fbk_bottomsideword_showresp, image, Error_message2]
        for thisComponent in ShowRespComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "ShowResp" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *highlightbox_showresp* updates
            
            # if highlightbox_showresp is starting this frame...
            if highlightbox_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                highlightbox_showresp.frameNStart = frameN  # exact frame index
                highlightbox_showresp.tStart = t  # local t and not account for scr refresh
                highlightbox_showresp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(highlightbox_showresp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'highlightbox_showresp.started')
                # update status
                highlightbox_showresp.status = STARTED
                highlightbox_showresp.setAutoDraw(True)
            
            # if highlightbox_showresp is active this frame...
            if highlightbox_showresp.status == STARTED:
                # update params
                pass
            
            # if highlightbox_showresp is stopping this frame...
            if highlightbox_showresp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > highlightbox_showresp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    highlightbox_showresp.tStop = t  # not accounting for scr refresh
                    highlightbox_showresp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'highlightbox_showresp.stopped')
                    # update status
                    highlightbox_showresp.status = FINISHED
                    highlightbox_showresp.setAutoDraw(False)
            
            # *Fbk_target_showresp* updates
            
            # if Fbk_target_showresp is starting this frame...
            if Fbk_target_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fbk_target_showresp.frameNStart = frameN  # exact frame index
                Fbk_target_showresp.tStart = t  # local t and not account for scr refresh
                Fbk_target_showresp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fbk_target_showresp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_target_showresp.started')
                # update status
                Fbk_target_showresp.status = STARTED
                Fbk_target_showresp.setAutoDraw(True)
            
            # if Fbk_target_showresp is active this frame...
            if Fbk_target_showresp.status == STARTED:
                # update params
                pass
            
            # if Fbk_target_showresp is stopping this frame...
            if Fbk_target_showresp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fbk_target_showresp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Fbk_target_showresp.tStop = t  # not accounting for scr refresh
                    Fbk_target_showresp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fbk_target_showresp.stopped')
                    # update status
                    Fbk_target_showresp.status = FINISHED
                    Fbk_target_showresp.setAutoDraw(False)
            
            # *Fbk_topsideword_showresp* updates
            
            # if Fbk_topsideword_showresp is starting this frame...
            if Fbk_topsideword_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fbk_topsideword_showresp.frameNStart = frameN  # exact frame index
                Fbk_topsideword_showresp.tStart = t  # local t and not account for scr refresh
                Fbk_topsideword_showresp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fbk_topsideword_showresp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_topsideword_showresp.started')
                # update status
                Fbk_topsideword_showresp.status = STARTED
                Fbk_topsideword_showresp.setAutoDraw(True)
            
            # if Fbk_topsideword_showresp is active this frame...
            if Fbk_topsideword_showresp.status == STARTED:
                # update params
                pass
            
            # if Fbk_topsideword_showresp is stopping this frame...
            if Fbk_topsideword_showresp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fbk_topsideword_showresp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Fbk_topsideword_showresp.tStop = t  # not accounting for scr refresh
                    Fbk_topsideword_showresp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fbk_topsideword_showresp.stopped')
                    # update status
                    Fbk_topsideword_showresp.status = FINISHED
                    Fbk_topsideword_showresp.setAutoDraw(False)
            
            # *Fbk_bottomsideword_showresp* updates
            
            # if Fbk_bottomsideword_showresp is starting this frame...
            if Fbk_bottomsideword_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fbk_bottomsideword_showresp.frameNStart = frameN  # exact frame index
                Fbk_bottomsideword_showresp.tStart = t  # local t and not account for scr refresh
                Fbk_bottomsideword_showresp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fbk_bottomsideword_showresp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_bottomsideword_showresp.started')
                # update status
                Fbk_bottomsideword_showresp.status = STARTED
                Fbk_bottomsideword_showresp.setAutoDraw(True)
            
            # if Fbk_bottomsideword_showresp is active this frame...
            if Fbk_bottomsideword_showresp.status == STARTED:
                # update params
                pass
            
            # if Fbk_bottomsideword_showresp is stopping this frame...
            if Fbk_bottomsideword_showresp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fbk_bottomsideword_showresp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Fbk_bottomsideword_showresp.tStop = t  # not accounting for scr refresh
                    Fbk_bottomsideword_showresp.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Fbk_bottomsideword_showresp.stopped')
                    # update status
                    Fbk_bottomsideword_showresp.status = FINISHED
                    Fbk_bottomsideword_showresp.setAutoDraw(False)
            
            # *image* updates
            
            # if image is starting this frame...
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.started')
                # update status
                image.status = STARTED
                image.setAutoDraw(True)
            
            # if image is active this frame...
            if image.status == STARTED:
                # update params
                pass
            
            # if image is stopping this frame...
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.stopped')
                    # update status
                    image.status = FINISHED
                    image.setAutoDraw(False)
            
            # *Error_message2* updates
            
            # if Error_message2 is starting this frame...
            if Error_message2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Error_message2.frameNStart = frameN  # exact frame index
                Error_message2.tStart = t  # local t and not account for scr refresh
                Error_message2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Error_message2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Error_message2.started')
                # update status
                Error_message2.status = STARTED
                Error_message2.setAutoDraw(True)
            
            # if Error_message2 is active this frame...
            if Error_message2.status == STARTED:
                # update params
                pass
            
            # if Error_message2 is stopping this frame...
            if Error_message2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Error_message2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    Error_message2.tStop = t  # not accounting for scr refresh
                    Error_message2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Error_message2.stopped')
                    # update status
                    Error_message2.status = FINISHED
                    Error_message2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
                if eyetracker:
                    eyetracker.setConnectionState(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ShowRespComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ShowResp" ---
        for thisComponent in ShowRespComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials_2'
    
    # get names of stimulus parameters
    if trials_2.trialList in ([], [None], None):
        params = []
    else:
        params = trials_2.trialList[0].keys()
    # save data for this loop
    trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # --- Prepare to start Routine "repeat_instruct" ---
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    repeat_instructComponents = [text_7, key_resp_4]
    for thisComponent in repeat_instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "repeat_instruct" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        
        # if text_7 is starting this frame...
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            # update status
            text_7.status = STARTED
            text_7.setAutoDraw(True)
        
        # if text_7 is active this frame...
        if text_7.status == STARTED:
            # update params
            pass
        
        # *key_resp_4* updates
        waitOnFlip = False
        
        # if key_resp_4 is starting this frame...
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            # update status
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['t'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in repeat_instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "repeat_instruct" ---
    for thisComponent in repeat_instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials_3.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials_3.addData('key_resp_4.rt', key_resp_4.rt)
    # the Routine "repeat_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 3.0 repeats of 'trials_3'


# --- Prepare to start Routine "EndPart2" ---
continueRoutine = True
# update component parameters for each repeat
contpart2_2.keys = []
contpart2_2.rt = []
_contpart2_2_allKeys = []
# keep track of which components have finished
EndPart2Components = [text_2, contpart2_2]
for thisComponent in EndPart2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EndPart2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    
    # if text_2 is starting this frame...
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_2.started')
        # update status
        text_2.status = STARTED
        text_2.setAutoDraw(True)
    
    # if text_2 is active this frame...
    if text_2.status == STARTED:
        # update params
        pass
    
    # *contpart2_2* updates
    waitOnFlip = False
    
    # if contpart2_2 is starting this frame...
    if contpart2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        contpart2_2.frameNStart = frameN  # exact frame index
        contpart2_2.tStart = t  # local t and not account for scr refresh
        contpart2_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contpart2_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'contpart2_2.started')
        # update status
        contpart2_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(contpart2_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(contpart2_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if contpart2_2.status == STARTED and not waitOnFlip:
        theseKeys = contpart2_2.getKeys(keyList=['t'], waitRelease=False)
        _contpart2_2_allKeys.extend(theseKeys)
        if len(_contpart2_2_allKeys):
            contpart2_2.keys = _contpart2_2_allKeys[-1].name  # just the last key pressed
            contpart2_2.rt = _contpart2_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndPart2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndPart2" ---
for thisComponent in EndPart2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if contpart2_2.keys in ['', [], None]:  # No response was made
    contpart2_2.keys = None
thisExp.addData('contpart2_2.keys',contpart2_2.keys)
if contpart2_2.keys != None:  # we had a response
    thisExp.addData('contpart2_2.rt', contpart2_2.rt)
thisExp.nextEntry()
# the Routine "EndPart2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instruct2" ---
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
Instruct2Components = [text_6, key_resp_3]
for thisComponent in Instruct2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instruct2" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    
    # if text_6 is starting this frame...
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_6.started')
        # update status
        text_6.status = STARTED
        text_6.setAutoDraw(True)
    
    # if text_6 is active this frame...
    if text_6.status == STARTED:
        # update params
        pass
    
    # *key_resp_3* updates
    waitOnFlip = False
    
    # if key_resp_3 is starting this frame...
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        # update status
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['1','2'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruct2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruct2" ---
for thisComponent in Instruct2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Instruct2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Test_A.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "GetReady" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    GetReadyComponents = [fixation, text_4]
    for thisComponent in GetReadyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "GetReady" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        
        # if fixation is starting this frame...
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation.started')
            # update status
            fixation.status = STARTED
            fixation.setAutoDraw(True)
        
        # if fixation is active this frame...
        if fixation.status == STARTED:
            # update params
            pass
        
        # if fixation is stopping this frame...
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation.stopped')
                # update status
                fixation.status = FINISHED
                fixation.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_4.stopped')
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GetReadyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "GetReady" ---
    for thisComponent in GetReadyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "ChooseFbk" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_2
    selectbox_color = 'white'
    response_record = ''
    CorrResp = 1
    r3reversed = []
    topside = CorrRespDig1
    botside = CorrRespDig2
    
    if random()>.5:
        topside = CorrRespDig1
        botside = CorrRespDig2
        r3reversed = False
        CorrResp = 1
    else:
        topside = CorrRespDig2
        botside = CorrRespDig1
        r3reversed = True
        CorrResp = 2
    
    thisExp.addData('r3reversed',r3reversed)
    thisExp.addData('CorrResp',CorrResp)
    thisExp.addData('topside',topside)
    thisExp.addData('botside',botside)
    fbkcosttext.setText(mathprob)
    StudyView_topsideword_4.setText('a) ' + topside)
    StudyView1_bottomsideword_4.setText('b) ' + botside

)
    Test3response2.keys = []
    Test3response2.rt = []
    _Test3response2_allKeys = []
    # keep track of which components have finished
    ChooseFbkComponents = [fbkcosttext, StudyView_topsideword_4, StudyView1_bottomsideword_4, Test3response2]
    for thisComponent in ChooseFbkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ChooseFbk" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 4.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fbkcosttext* updates
        
        # if fbkcosttext is starting this frame...
        if fbkcosttext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fbkcosttext.frameNStart = frameN  # exact frame index
            fbkcosttext.tStart = t  # local t and not account for scr refresh
            fbkcosttext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fbkcosttext, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fbkcosttext.started')
            # update status
            fbkcosttext.status = STARTED
            fbkcosttext.setAutoDraw(True)
        
        # if fbkcosttext is active this frame...
        if fbkcosttext.status == STARTED:
            # update params
            pass
        
        # if fbkcosttext is stopping this frame...
        if fbkcosttext.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fbkcosttext.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                fbkcosttext.tStop = t  # not accounting for scr refresh
                fbkcosttext.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fbkcosttext.stopped')
                # update status
                fbkcosttext.status = FINISHED
                fbkcosttext.setAutoDraw(False)
        
        # *StudyView_topsideword_4* updates
        
        # if StudyView_topsideword_4 is starting this frame...
        if StudyView_topsideword_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StudyView_topsideword_4.frameNStart = frameN  # exact frame index
            StudyView_topsideword_4.tStart = t  # local t and not account for scr refresh
            StudyView_topsideword_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StudyView_topsideword_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StudyView_topsideword_4.started')
            # update status
            StudyView_topsideword_4.status = STARTED
            StudyView_topsideword_4.setAutoDraw(True)
        
        # if StudyView_topsideword_4 is active this frame...
        if StudyView_topsideword_4.status == STARTED:
            # update params
            pass
        
        # if StudyView_topsideword_4 is stopping this frame...
        if StudyView_topsideword_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StudyView_topsideword_4.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                StudyView_topsideword_4.tStop = t  # not accounting for scr refresh
                StudyView_topsideword_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StudyView_topsideword_4.stopped')
                # update status
                StudyView_topsideword_4.status = FINISHED
                StudyView_topsideword_4.setAutoDraw(False)
        
        # *StudyView1_bottomsideword_4* updates
        
        # if StudyView1_bottomsideword_4 is starting this frame...
        if StudyView1_bottomsideword_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StudyView1_bottomsideword_4.frameNStart = frameN  # exact frame index
            StudyView1_bottomsideword_4.tStart = t  # local t and not account for scr refresh
            StudyView1_bottomsideword_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StudyView1_bottomsideword_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StudyView1_bottomsideword_4.started')
            # update status
            StudyView1_bottomsideword_4.status = STARTED
            StudyView1_bottomsideword_4.setAutoDraw(True)
        
        # if StudyView1_bottomsideword_4 is active this frame...
        if StudyView1_bottomsideword_4.status == STARTED:
            # update params
            pass
        
        # if StudyView1_bottomsideword_4 is stopping this frame...
        if StudyView1_bottomsideword_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > StudyView1_bottomsideword_4.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                StudyView1_bottomsideword_4.tStop = t  # not accounting for scr refresh
                StudyView1_bottomsideword_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'StudyView1_bottomsideword_4.stopped')
                # update status
                StudyView1_bottomsideword_4.status = FINISHED
                StudyView1_bottomsideword_4.setAutoDraw(False)
        
        # *Test3response2* updates
        waitOnFlip = False
        
        # if Test3response2 is starting this frame...
        if Test3response2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Test3response2.frameNStart = frameN  # exact frame index
            Test3response2.tStart = t  # local t and not account for scr refresh
            Test3response2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Test3response2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Test3response2.started')
            # update status
            Test3response2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Test3response2.clock.reset)  # t=0 on next screen flip
        
        # if Test3response2 is stopping this frame...
        if Test3response2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Test3response2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                Test3response2.tStop = t  # not accounting for scr refresh
                Test3response2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Test3response2.stopped')
                # update status
                Test3response2.status = FINISHED
                Test3response2.status = FINISHED
        if Test3response2.status == STARTED and not waitOnFlip:
            theseKeys = Test3response2.getKeys(keyList=['1', '2'], waitRelease=False)
            _Test3response2_allKeys.extend(theseKeys)
            if len(_Test3response2_allKeys):
                Test3response2.keys = _Test3response2_allKeys[-1].name  # just the last key pressed
                Test3response2.rt = _Test3response2_allKeys[-1].rt
                # was this correct?
                if (Test3response2.keys == str(CorrResp)) or (Test3response2.keys == CorrResp):
                    Test3response2.corr = 1
                else:
                    Test3response2.corr = 0
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from code_4
        respbox_y = -1
        keys = event.getKeys()
        if '1' in keys:
            respbox_y = .1
        elif '2' in keys:
            respbox_y = -.05
        
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ChooseFbkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ChooseFbk" ---
    for thisComponent in ChooseFbkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Test3response2.keys in ['', [], None]:  # No response was made
        Test3response2.keys = None
        # was no response the correct answer?!
        if str(CorrResp).lower() == 'none':
           Test3response2.corr = 1;  # correct non-response
        else:
           Test3response2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('Test3response2.keys',Test3response2.keys)
    trials.addData('Test3response2.corr', Test3response2.corr)
    if Test3response2.keys != None:  # we had a response
        trials.addData('Test3response2.rt', Test3response2.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.000000)
    
    # --- Prepare to start Routine "ShowResp" ---
    continueRoutine = True
    # update component parameters for each repeat
    highlightbox_showresp.setFillColor([-1.0000, -1.0000, -1.0000])
    highlightbox_showresp.setPos((0, respbox_y))
    highlightbox_showresp.setLineColor(selectbox_color)
    Fbk_target_showresp.setText(mathprob)
    Fbk_topsideword_showresp.setText('a) ' + topside)
    Fbk_bottomsideword_showresp.setText('b) ' + botside)
    # Run 'Begin Routine' code from code_7
    x = 0
    errormsg = ''
    if Test3response2.rt >= 0:
        fbkimagefile = 'blacksquare.png'
    else:
        fbkimagefile = 'noresponse.png'
        errormsg = 'please respond faster'
    
    image.setImage(fbkimagefile)
    Error_message2.setText(errormsg)
    # keep track of which components have finished
    ShowRespComponents = [highlightbox_showresp, Fbk_target_showresp, Fbk_topsideword_showresp, Fbk_bottomsideword_showresp, image, Error_message2]
    for thisComponent in ShowRespComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ShowResp" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *highlightbox_showresp* updates
        
        # if highlightbox_showresp is starting this frame...
        if highlightbox_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            highlightbox_showresp.frameNStart = frameN  # exact frame index
            highlightbox_showresp.tStart = t  # local t and not account for scr refresh
            highlightbox_showresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(highlightbox_showresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'highlightbox_showresp.started')
            # update status
            highlightbox_showresp.status = STARTED
            highlightbox_showresp.setAutoDraw(True)
        
        # if highlightbox_showresp is active this frame...
        if highlightbox_showresp.status == STARTED:
            # update params
            pass
        
        # if highlightbox_showresp is stopping this frame...
        if highlightbox_showresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > highlightbox_showresp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                highlightbox_showresp.tStop = t  # not accounting for scr refresh
                highlightbox_showresp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'highlightbox_showresp.stopped')
                # update status
                highlightbox_showresp.status = FINISHED
                highlightbox_showresp.setAutoDraw(False)
        
        # *Fbk_target_showresp* updates
        
        # if Fbk_target_showresp is starting this frame...
        if Fbk_target_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbk_target_showresp.frameNStart = frameN  # exact frame index
            Fbk_target_showresp.tStart = t  # local t and not account for scr refresh
            Fbk_target_showresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbk_target_showresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fbk_target_showresp.started')
            # update status
            Fbk_target_showresp.status = STARTED
            Fbk_target_showresp.setAutoDraw(True)
        
        # if Fbk_target_showresp is active this frame...
        if Fbk_target_showresp.status == STARTED:
            # update params
            pass
        
        # if Fbk_target_showresp is stopping this frame...
        if Fbk_target_showresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fbk_target_showresp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Fbk_target_showresp.tStop = t  # not accounting for scr refresh
                Fbk_target_showresp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_target_showresp.stopped')
                # update status
                Fbk_target_showresp.status = FINISHED
                Fbk_target_showresp.setAutoDraw(False)
        
        # *Fbk_topsideword_showresp* updates
        
        # if Fbk_topsideword_showresp is starting this frame...
        if Fbk_topsideword_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbk_topsideword_showresp.frameNStart = frameN  # exact frame index
            Fbk_topsideword_showresp.tStart = t  # local t and not account for scr refresh
            Fbk_topsideword_showresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbk_topsideword_showresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fbk_topsideword_showresp.started')
            # update status
            Fbk_topsideword_showresp.status = STARTED
            Fbk_topsideword_showresp.setAutoDraw(True)
        
        # if Fbk_topsideword_showresp is active this frame...
        if Fbk_topsideword_showresp.status == STARTED:
            # update params
            pass
        
        # if Fbk_topsideword_showresp is stopping this frame...
        if Fbk_topsideword_showresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fbk_topsideword_showresp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Fbk_topsideword_showresp.tStop = t  # not accounting for scr refresh
                Fbk_topsideword_showresp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_topsideword_showresp.stopped')
                # update status
                Fbk_topsideword_showresp.status = FINISHED
                Fbk_topsideword_showresp.setAutoDraw(False)
        
        # *Fbk_bottomsideword_showresp* updates
        
        # if Fbk_bottomsideword_showresp is starting this frame...
        if Fbk_bottomsideword_showresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Fbk_bottomsideword_showresp.frameNStart = frameN  # exact frame index
            Fbk_bottomsideword_showresp.tStart = t  # local t and not account for scr refresh
            Fbk_bottomsideword_showresp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Fbk_bottomsideword_showresp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Fbk_bottomsideword_showresp.started')
            # update status
            Fbk_bottomsideword_showresp.status = STARTED
            Fbk_bottomsideword_showresp.setAutoDraw(True)
        
        # if Fbk_bottomsideword_showresp is active this frame...
        if Fbk_bottomsideword_showresp.status == STARTED:
            # update params
            pass
        
        # if Fbk_bottomsideword_showresp is stopping this frame...
        if Fbk_bottomsideword_showresp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Fbk_bottomsideword_showresp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Fbk_bottomsideword_showresp.tStop = t  # not accounting for scr refresh
                Fbk_bottomsideword_showresp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Fbk_bottomsideword_showresp.stopped')
                # update status
                Fbk_bottomsideword_showresp.status = FINISHED
                Fbk_bottomsideword_showresp.setAutoDraw(False)
        
        # *image* updates
        
        # if image is starting this frame...
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            # update status
            image.status = STARTED
            image.setAutoDraw(True)
        
        # if image is active this frame...
        if image.status == STARTED:
            # update params
            pass
        
        # if image is stopping this frame...
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.stopped')
                # update status
                image.status = FINISHED
                image.setAutoDraw(False)
        
        # *Error_message2* updates
        
        # if Error_message2 is starting this frame...
        if Error_message2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Error_message2.frameNStart = frameN  # exact frame index
            Error_message2.tStart = t  # local t and not account for scr refresh
            Error_message2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Error_message2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Error_message2.started')
            # update status
            Error_message2.status = STARTED
            Error_message2.setAutoDraw(True)
        
        # if Error_message2 is active this frame...
        if Error_message2.status == STARTED:
            # update params
            pass
        
        # if Error_message2 is stopping this frame...
        if Error_message2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Error_message2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                Error_message2.tStop = t  # not accounting for scr refresh
                Error_message2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Error_message2.stopped')
                # update status
                Error_message2.status = FINISHED
                Error_message2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
            if eyetracker:
                eyetracker.setConnectionState(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ShowRespComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ShowResp" ---
    for thisComponent in ShowRespComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'

# get names of stimulus parameters
if trials.trialList in ([], [None], None):
    params = []
else:
    params = trials.trialList[0].keys()
# save data for this loop
trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# --- Prepare to start Routine "EndPart1" ---
continueRoutine = True
# update component parameters for each repeat
contpart2.keys = []
contpart2.rt = []
_contpart2_allKeys = []
# keep track of which components have finished
EndPart1Components = [text, contpart2]
for thisComponent in EndPart1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "EndPart1" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    
    # if text is starting this frame...
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        # update status
        text.status = STARTED
        text.setAutoDraw(True)
    
    # if text is active this frame...
    if text.status == STARTED:
        # update params
        pass
    
    # *contpart2* updates
    waitOnFlip = False
    
    # if contpart2 is starting this frame...
    if contpart2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        contpart2.frameNStart = frameN  # exact frame index
        contpart2.tStart = t  # local t and not account for scr refresh
        contpart2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(contpart2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'contpart2.started')
        # update status
        contpart2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(contpart2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(contpart2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if contpart2.status == STARTED and not waitOnFlip:
        theseKeys = contpart2.getKeys(keyList=['t'], waitRelease=False)
        _contpart2_allKeys.extend(theseKeys)
        if len(_contpart2_allKeys):
            contpart2.keys = _contpart2_allKeys[-1].name  # just the last key pressed
            contpart2.rt = _contpart2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
        if eyetracker:
            eyetracker.setConnectionState(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndPart1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "EndPart1" ---
for thisComponent in EndPart1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if contpart2.keys in ['', [], None]:  # No response was made
    contpart2.keys = None
thisExp.addData('contpart2.keys',contpart2.keys)
if contpart2.keys != None:  # we had a response
    thisExp.addData('contpart2.rt', contpart2.rt)
thisExp.nextEntry()
# the Routine "EndPart1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
