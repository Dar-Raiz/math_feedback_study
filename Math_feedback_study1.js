/***************************** 
 * Math_Feedback_Study1 Test *
 *****************************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2023.1.2.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'Math_feedback_study1';  // from the Builder filename that created this script
let expInfo = {
    'RUID': 'INPUT RUID HERE',
    'Email Address': 'INPUT EMAIL ADDRESS HERE',
    'First Name': 'INPUT FIRST NAME HERE',
    'Last Name': 'INPUT LAST NAME HERE',
};

// Start code blocks for 'Before Experiment'
var myBrowser;
var sUsrAg;
var nIdx;

function getBrowserId () {
    var browsers = ["MSIE", "Firefox", "Safari", "Chrome", "Opera"];
    sUsrAg = window.navigator.userAgent,
    nIdx = browsers.length - 1;
    for (nIdx; nIdx > -1 && sUsrAg.indexOf(browsers [nIdx]) === -1; nIdx--);

  return browsers[nIdx];
}

myBrowser = getBrowserId();


var nCorr = 0;
var nCorr2 = 0;
var nCorr3 = 0;
var practice_round = 0;
var eachResp = 0;
console.log(nCorr);


// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('black'),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(InstructRoutineBegin());
flowScheduler.add(InstructRoutineEachFrame());
flowScheduler.add(InstructRoutineEnd());
flowScheduler.add(Prac_instructRoutineBegin());
flowScheduler.add(Prac_instructRoutineEachFrame());
flowScheduler.add(Prac_instructRoutineEnd());
flowScheduler.add(GetReadyRoutineBegin());
flowScheduler.add(GetReadyRoutineEachFrame());
flowScheduler.add(GetReadyRoutineEnd());
const trials_3LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_3LoopBegin(trials_3LoopScheduler));
flowScheduler.add(trials_3LoopScheduler);
flowScheduler.add(trials_3LoopEnd);
flowScheduler.add(EndPart2RoutineBegin());
flowScheduler.add(EndPart2RoutineEachFrame());
flowScheduler.add(EndPart2RoutineEnd());
flowScheduler.add(Instruct2RoutineBegin());
flowScheduler.add(Instruct2RoutineEachFrame());
flowScheduler.add(Instruct2RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(EndPart1RoutineBegin());
flowScheduler.add(EndPart1RoutineEachFrame());
flowScheduler.add(EndPart1RoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'practice_Test.xlsx', 'path': 'practice_Test.xlsx'},
    {'name': 'Test_A.xlsx', 'path': 'Test_A.xlsx'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
    {'name': 'Test_A.xlsx', 'path': 'Test_A.xlsx'},
    {'name': 'blacksquare.png', 'path': 'blacksquare.png'},
    {'name': 'noresponse.png', 'path': 'noresponse.png'},
    {'name': 'practice_Test.xlsx', 'path': 'practice_Test.xlsx'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.1.2';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://rutgers.ca1.qualtrics.com/jfe/form/SV_9LgaDNDbNhqMQvQ', '');


  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["First Name"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}


var InstructClock;
var text_5;
var key_resp;
var Prac_instructClock;
var text_8;
var key_resp_5;
var GetReadyClock;
var fixation;
var text_4;
var ChooseFbkClock;
var fbkcosttext;
var StudyView_topsideword_4;
var StudyView1_bottomsideword_4;
var Test3response2;
var ShowRespClock;
var highlightbox_showresp;
var Fbk_target_showresp;
var Fbk_topsideword_showresp;
var Fbk_bottomsideword_showresp;
var image;
var Error_message2;
var repeat_instructClock;
var text_7;
var key_resp_4;
var EndPart2Clock;
var text_2;
var contpart2_2;
var Instruct2Clock;
var text_6;
var key_resp_3;
var EndPart1Clock;
var text;
var contpart2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Instruct"
  InstructClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: 'Introduction\n\nFor this experiment, you will be solving math multiplication problems in your head. Our primary goal is to understand how well college students perform mental arithmetic.  \n\nTo maintain the integrity of our experiment we respectfully ask please DO NOT USE a cell phone, calculator, or pen/paper for this experiment. We want you to try and do everything in your head. \n\n\nPress ‘t’ to continue to the next page\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  psychoJS.experiment.addData("Browser", myBrowser)
  
  // Initialize components for Routine "Prac_instruct"
  Prac_instructClock = new util.Clock();
  text_8 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_8',
    text: 'Practice Round\n\nFirst you will do a simple practice round consisting of 4 questions. You must get at least 3 questions correct in order to advance to the main task.\n \nYou will see a multiplication problem presented at the top of the screen with two possible choices underneath it. Your job is to pick the correct answer. You will have 10 seconds to make each response before moving onto the next trial.\n\nExample\n\n  8 x 1 =\n\n  a) 8\n  b) 1\n\nTo pick response a) press the ‘1’ key. \nTo pick response b) press the ‘2’ key.\n\nPress ‘1’ or ‘2’ to begin the practice round.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.036,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "GetReady"
  GetReadyClock = new util.Clock();
  fixation = new visual.TextStim({
    win: psychoJS.window,
    name: 'fixation',
    text: '+',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 10], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "ChooseFbk"
  ChooseFbkClock = new util.Clock();
  fbkcosttext = new visual.TextStim({
    win: psychoJS.window,
    name: 'fbkcosttext',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  StudyView_topsideword_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'StudyView_topsideword_4',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  StudyView1_bottomsideword_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'StudyView1_bottomsideword_4',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.05)], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  Test3response2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ShowResp"
  ShowRespClock = new util.Clock();
  highlightbox_showresp = new visual.Rect ({
    win: psychoJS.window, name: 'highlightbox_showresp', 
    width: [0.33, 0.12][0], height: [0.33, 0.12][1],
    ori: 0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 6, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  Fbk_target_showresp = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fbk_target_showresp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.3], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  Fbk_topsideword_showresp = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fbk_topsideword_showresp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.1], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  Fbk_bottomsideword_showresp = new visual.TextStim({
    win: psychoJS.window,
    name: 'Fbk_bottomsideword_showresp',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.05)], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, (- 0.285)], size : [0.3, 0.3],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  Error_message2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Error_message2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.2], height: 0.075,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('red'),  opacity: 1,
    depth: -6.0 
  });
  
  // Initialize components for Routine "repeat_instruct"
  repeat_instructClock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'Please Try Again\n\nYou got less than 3 correct responses during the practice round. In order to advance to the main task, you need to get at least 3 correct responses during the practice round. \n\nRemember, to pick response a) press the ‘1’ key. To pick response b) press the ‘2’ key.\n\n\nPress ‘t’ to restart the practice round.\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "EndPart2"
  EndPart2Clock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'You passed the practice task!\n\nPress ‘t’ to advance to the main task instructions\n',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  contpart2_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instruct2"
  Instruct2Clock = new util.Clock();
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'Main Task\n\nNow that you have gotten a feel for the task, you are now ready for the real test. You will again see multiplication problems like before, however these problems will range in their difficulty. You will have 10 seconds to make each response.\n\nPlease try your best to calculate the correct response instead of guessing.  \n\nExample\n\n12 x 2 =\n\na) 22\nb) 24\n\nTo pick response a) press the ‘1’ key. \nTo pick response b) press the ‘2’ key.\n\n\nPress ‘1’ or ‘2’ to begin the main task.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.033,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "EndPart1"
  EndPart1Clock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: "That was the end of the task. \n\nTo finish the experiment press 't', then complete a brief questionnaire. \n\n",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  contpart2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_allKeys;
var InstructComponents;
function InstructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruct' ---
    t = 0;
    InstructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    InstructComponents = [];
    InstructComponents.push(text_5);
    InstructComponents.push(key_resp);
    
    for (const thisComponent of InstructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruct' ---
    // get current time
    t = InstructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['t'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstructComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruct' ---
    for (const thisComponent of InstructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_5_allKeys;
var Prac_instructComponents;
function Prac_instructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Prac_instruct' ---
    t = 0;
    Prac_instructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    Prac_instructComponents = [];
    Prac_instructComponents.push(text_8);
    Prac_instructComponents.push(key_resp_5);
    
    for (const thisComponent of Prac_instructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Prac_instructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Prac_instruct' ---
    // get current time
    t = Prac_instructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_8* updates
    if (t >= 0.0 && text_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_8.tStart = t;  // (not accounting for frame time here)
      text_8.frameNStart = frameN;  // exact frame index
      
      text_8.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['1', '2'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Prac_instructComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Prac_instructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Prac_instruct' ---
    for (const thisComponent of Prac_instructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "Prac_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var GetReadyComponents;
function GetReadyRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'GetReady' ---
    t = 0;
    GetReadyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    GetReadyComponents = [];
    GetReadyComponents.push(fixation);
    GetReadyComponents.push(text_4);
    
    for (const thisComponent of GetReadyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function GetReadyRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'GetReady' ---
    // get current time
    t = GetReadyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixation* updates
    if (t >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixation.tStart = t;  // (not accounting for frame time here)
      fixation.frameNStart = frameN;  // exact frame index
      
      fixation.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixation.setAutoDraw(false);
    }
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_4.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of GetReadyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function GetReadyRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'GetReady' ---
    for (const thisComponent of GetReadyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 3, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_3 of trials_3) {
      snapshot = trials_3.getSnapshot();
      trials_3LoopScheduler.add(importConditions(snapshot));
      const trials_2LoopScheduler = new Scheduler(psychoJS);
      trials_3LoopScheduler.add(trials_2LoopBegin(trials_2LoopScheduler, snapshot));
      trials_3LoopScheduler.add(trials_2LoopScheduler);
      trials_3LoopScheduler.add(trials_2LoopEnd);
      trials_3LoopScheduler.add(repeat_instructRoutineBegin(snapshot));
      trials_3LoopScheduler.add(repeat_instructRoutineEachFrame());
      trials_3LoopScheduler.add(repeat_instructRoutineEnd(snapshot));
      trials_3LoopScheduler.add(trials_3LoopEndIteration(trials_3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.FULLRANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'practice_Test.xlsx',
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(GetReadyRoutineBegin(snapshot));
      trials_2LoopScheduler.add(GetReadyRoutineEachFrame());
      trials_2LoopScheduler.add(GetReadyRoutineEnd(snapshot));
      trials_2LoopScheduler.add(ChooseFbkRoutineBegin(snapshot));
      trials_2LoopScheduler.add(ChooseFbkRoutineEachFrame());
      trials_2LoopScheduler.add(ChooseFbkRoutineEnd(snapshot));
      trials_2LoopScheduler.add(ShowRespRoutineBegin(snapshot));
      trials_2LoopScheduler.add(ShowRespRoutineEachFrame());
      trials_2LoopScheduler.add(ShowRespRoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trials_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Test_A.xlsx',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(GetReadyRoutineBegin(snapshot));
      trialsLoopScheduler.add(GetReadyRoutineEachFrame());
      trialsLoopScheduler.add(GetReadyRoutineEnd(snapshot));
      trialsLoopScheduler.add(ChooseFbkRoutineBegin(snapshot));
      trialsLoopScheduler.add(ChooseFbkRoutineEachFrame());
      trialsLoopScheduler.add(ChooseFbkRoutineEnd(snapshot));
      trialsLoopScheduler.add(ShowRespRoutineBegin(snapshot));
      trialsLoopScheduler.add(ShowRespRoutineEachFrame());
      trialsLoopScheduler.add(ShowRespRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var selectbox_color;
var response_record;
var CorrResp;
var r3reversed;
var topside;
var botside;
var _Test3response2_allKeys;
var ChooseFbkComponents;
function ChooseFbkRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ChooseFbk' ---
    t = 0;
    ChooseFbkClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(10.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_2
    selectbox_color = "white";
    response_record = "";
    CorrResp = 1;
    r3reversed = [];
    topside = CorrRespDig1;
    botside = CorrRespDig2;
    if ((Math.random() > 0.5)) {
        topside = CorrRespDig1;
        botside = CorrRespDig2;
        r3reversed = false;
        CorrResp = 1;
    } else {
        topside = CorrRespDig2;
        botside = CorrRespDig1;
        r3reversed = true;
        CorrResp = 2;
    }
    psychoJS.experiment.addData("r3reversed", r3reversed);
    psychoJS.experiment.addData("CorrResp", CorrResp);
    psychoJS.experiment.addData("topside", topside);
    psychoJS.experiment.addData("botside", botside);
    
    fbkcosttext.setText(mathprob);
    StudyView_topsideword_4.setText(("a) " + topside));
    StudyView1_bottomsideword_4.setText(("b) " + botside));
    Test3response2.keys = undefined;
    Test3response2.rt = undefined;
    _Test3response2_allKeys = [];
    // keep track of which components have finished
    ChooseFbkComponents = [];
    ChooseFbkComponents.push(fbkcosttext);
    ChooseFbkComponents.push(StudyView_topsideword_4);
    ChooseFbkComponents.push(StudyView1_bottomsideword_4);
    ChooseFbkComponents.push(Test3response2);
    
    for (const thisComponent of ChooseFbkComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var _pj;
var respbox_y;
var keys;
function ChooseFbkRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ChooseFbk' ---
    // get current time
    t = ChooseFbkClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fbkcosttext* updates
    if (t >= 0.0 && fbkcosttext.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fbkcosttext.tStart = t;  // (not accounting for frame time here)
      fbkcosttext.frameNStart = frameN;  // exact frame index
      
      fbkcosttext.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fbkcosttext.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fbkcosttext.setAutoDraw(false);
    }
    
    // *StudyView_topsideword_4* updates
    if (t >= 0.0 && StudyView_topsideword_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StudyView_topsideword_4.tStart = t;  // (not accounting for frame time here)
      StudyView_topsideword_4.frameNStart = frameN;  // exact frame index
      
      StudyView_topsideword_4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (StudyView_topsideword_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      StudyView_topsideword_4.setAutoDraw(false);
    }
    
    // *StudyView1_bottomsideword_4* updates
    if (t >= 0.0 && StudyView1_bottomsideword_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      StudyView1_bottomsideword_4.tStart = t;  // (not accounting for frame time here)
      StudyView1_bottomsideword_4.frameNStart = frameN;  // exact frame index
      
      StudyView1_bottomsideword_4.setAutoDraw(true);
    }

    frameRemains = 0.0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (StudyView1_bottomsideword_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      StudyView1_bottomsideword_4.setAutoDraw(false);
    }
    
    // *Test3response2* updates
    if (t >= 0 && Test3response2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Test3response2.tStart = t;  // (not accounting for frame time here)
      Test3response2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Test3response2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Test3response2.start(); }); // start on screen flip
    }

    frameRemains = 0 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Test3response2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Test3response2.status = PsychoJS.Status.FINISHED;
  }

    if (Test3response2.status === PsychoJS.Status.STARTED) {
      let theseKeys = Test3response2.getKeys({keyList: ['1', '2'], waitRelease: false});
      _Test3response2_allKeys = _Test3response2_allKeys.concat(theseKeys);
      if (_Test3response2_allKeys.length > 0) {
        Test3response2.keys = _Test3response2_allKeys[_Test3response2_allKeys.length - 1].name;  // just the last key pressed
        Test3response2.rt = _Test3response2_allKeys[_Test3response2_allKeys.length - 1].rt;
        // was this correct?
        if (Test3response2.keys == CorrResp) {
            Test3response2.corr = 1;
        } else {
            Test3response2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // Run 'Each Frame' code from code_4
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    respbox_y = (- 1);
    keys = psychoJS.eventManager.getKeys();
    if (_pj.in_es6("1", keys)) {
        respbox_y = 0.1;
    } else {
        if (_pj.in_es6("2", keys)) {
            respbox_y = (- 0.05);
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ChooseFbkComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ChooseFbkRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ChooseFbk' ---
    for (const thisComponent of ChooseFbkComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (Test3response2.keys === undefined) {
      if (['None','none',undefined].includes(CorrResp)) {
         Test3response2.corr = 1;  // correct non-response
      } else {
         Test3response2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Test3response2.corr, level);
    }
    psychoJS.experiment.addData('Test3response2.keys', Test3response2.keys);
    psychoJS.experiment.addData('Test3response2.corr', Test3response2.corr);
    if (typeof Test3response2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Test3response2.rt', Test3response2.rt);
        routineTimer.reset();
        }
    
    Test3response2.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var x;
var errormsg;
var fbkimagefile;
var ShowRespComponents;
function ShowRespRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ShowResp' ---
    t = 0;
    ShowRespClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    highlightbox_showresp.setFillColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
    highlightbox_showresp.setPos([0, respbox_y]);
    highlightbox_showresp.setLineColor(new util.Color(selectbox_color));
    Fbk_target_showresp.setText(mathprob);
    Fbk_topsideword_showresp.setText(("a) " + topside));
    Fbk_bottomsideword_showresp.setText(("b) " + botside));
    // Run 'Begin Routine' code from code_7
    x = 0;
    errormsg = "";
    if ((Test3response2.rt >= 0)) {
        fbkimagefile = "blacksquare.png";
    } else {
        fbkimagefile = "noresponse.png";
        errormsg = "please respond faster";
    }
    
    image.setImage(fbkimagefile);
    Error_message2.setText(errormsg);
    // keep track of which components have finished
    ShowRespComponents = [];
    ShowRespComponents.push(highlightbox_showresp);
    ShowRespComponents.push(Fbk_target_showresp);
    ShowRespComponents.push(Fbk_topsideword_showresp);
    ShowRespComponents.push(Fbk_bottomsideword_showresp);
    ShowRespComponents.push(image);
    ShowRespComponents.push(Error_message2);
    
    for (const thisComponent of ShowRespComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ShowRespRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ShowResp' ---
    // get current time
    t = ShowRespClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *highlightbox_showresp* updates
    if (t >= 0.0 && highlightbox_showresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      highlightbox_showresp.tStart = t;  // (not accounting for frame time here)
      highlightbox_showresp.frameNStart = frameN;  // exact frame index
      
      highlightbox_showresp.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (highlightbox_showresp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      highlightbox_showresp.setAutoDraw(false);
    }
    
    // *Fbk_target_showresp* updates
    if (t >= 0.0 && Fbk_target_showresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fbk_target_showresp.tStart = t;  // (not accounting for frame time here)
      Fbk_target_showresp.frameNStart = frameN;  // exact frame index
      
      Fbk_target_showresp.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fbk_target_showresp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fbk_target_showresp.setAutoDraw(false);
    }
    
    // *Fbk_topsideword_showresp* updates
    if (t >= 0.0 && Fbk_topsideword_showresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fbk_topsideword_showresp.tStart = t;  // (not accounting for frame time here)
      Fbk_topsideword_showresp.frameNStart = frameN;  // exact frame index
      
      Fbk_topsideword_showresp.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fbk_topsideword_showresp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fbk_topsideword_showresp.setAutoDraw(false);
    }
    
    // *Fbk_bottomsideword_showresp* updates
    if (t >= 0.0 && Fbk_bottomsideword_showresp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Fbk_bottomsideword_showresp.tStart = t;  // (not accounting for frame time here)
      Fbk_bottomsideword_showresp.frameNStart = frameN;  // exact frame index
      
      Fbk_bottomsideword_showresp.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Fbk_bottomsideword_showresp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Fbk_bottomsideword_showresp.setAutoDraw(false);
    }
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    
    // *Error_message2* updates
    if (t >= 0.0 && Error_message2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Error_message2.tStart = t;  // (not accounting for frame time here)
      Error_message2.frameNStart = frameN;  // exact frame index
      
      Error_message2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Error_message2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Error_message2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ShowRespComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ShowRespRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ShowResp' ---
    for (const thisComponent of ShowRespComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_round;
var eachResp;
var _key_resp_4_allKeys;
var repeat_instructComponents;
function repeat_instructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'repeat_instruct' ---
    t = 0;
    repeat_instructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    console.log(nCorr)
    practice_round = practice_round + 1;
    eachResp = 0;
    console.log(nCorr)
    console.log(nCorr2)
    console.log(nCorr3)
    
    
    
    if (practice_round === 1) {
      for (eachResp=0; eachResp<psychoJS.experiment._trialsData.length; eachResp++){
        if ('Test3response2.corr' in psychoJS.experiment._trialsData[eachResp]) {
        nCorr += psychoJS.experiment._trialsData[eachResp]['Test3response2.corr'];
        }
      }
    }else if (practice_round === 2) {
      for (eachResp=0; eachResp<psychoJS.experiment._trialsData.length; eachResp++){
        if ('Test3response2.corr' in psychoJS.experiment._trialsData[eachResp]) {
        nCorr2 += psychoJS.experiment._trialsData[eachResp]['Test3response2.corr'];
        }
      }
        nCorr2 = nCorr2 - nCorr;
    } else{
      for (eachResp=0; eachResp<psychoJS.experiment._trialsData.length; eachResp++){
        if ('Test3response2.corr' in psychoJS.experiment._trialsData[eachResp]) {
        nCorr3 += psychoJS.experiment._trialsData[eachResp]['Test3response2.corr'];
        }
      }
        nCorr3 = nCorr3 - (nCorr + nCorr2);
    }
    
    if (practice_round === 1) {
    if (nCorr > 2) {
        trials_3.finished = true;
        } 
    } else if (practice_round === 2) {
        if (nCorr2 > 2) {
        trials_3.finished = true;
        } 
        } else { 
            trials_3.finished = false;
            }
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    repeat_instructComponents = [];
    repeat_instructComponents.push(text_7);
    repeat_instructComponents.push(key_resp_4);
    
    for (const thisComponent of repeat_instructComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function repeat_instructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'repeat_instruct' ---
    // get current time
    t = repeat_instructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }

    console.log(practice_round)
    console.log(nCorr)
    console.log(nCorr2)
    console.log(nCorr3)
    
    
    if (practice_round === 1) {
    if (nCorr > 2) {
        console.log("true")
        continueRoutine = false; // until we're told otherwise
        } else {
            console.log("false")
            continueRoutine = true;
            }
        }
    
    if (practice_round === 2) {
    if (nCorr2 > 2) {
        console.log("true")
        continueRoutine = false; // until we're told otherwise
        } else {
            console.log("false")
            continueRoutine = true;
            }
        }
    
    if (practice_round === 3) {
    if (nCorr3 > 2) {
        console.log("true")
        continueRoutine = false; // until we're told otherwise
        } else {
            console.log("false")
            continueRoutine = true;
            }
        }
    
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['t'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of repeat_instructComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function repeat_instructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'repeat_instruct' ---
    for (const thisComponent of repeat_instructComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "repeat_instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _contpart2_2_allKeys;
var EndPart2Components;
function EndPart2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndPart2' ---
    t = 0;
    EndPart2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    contpart2_2.keys = undefined;
    contpart2_2.rt = undefined;
    _contpart2_2_allKeys = [];
    // keep track of which components have finished
    EndPart2Components = [];
    EndPart2Components.push(text_2);
    EndPart2Components.push(contpart2_2);
    
    for (const thisComponent of EndPart2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndPart2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndPart2' ---
    // get current time
    t = EndPart2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    
    // *contpart2_2* updates
    if (t >= 0.0 && contpart2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      contpart2_2.tStart = t;  // (not accounting for frame time here)
      contpart2_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { contpart2_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { contpart2_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { contpart2_2.clearEvents(); });
    }

    if (contpart2_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = contpart2_2.getKeys({keyList: ['t'], waitRelease: false});
      _contpart2_2_allKeys = _contpart2_2_allKeys.concat(theseKeys);
      if (_contpart2_2_allKeys.length > 0) {
        contpart2_2.keys = _contpart2_2_allKeys[_contpart2_2_allKeys.length - 1].name;  // just the last key pressed
        contpart2_2.rt = _contpart2_2_allKeys[_contpart2_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndPart2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndPart2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndPart2' ---
    for (const thisComponent of EndPart2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(contpart2_2.corr, level);
    }
    psychoJS.experiment.addData('contpart2_2.keys', contpart2_2.keys);
    if (typeof contpart2_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('contpart2_2.rt', contpart2_2.rt);
        routineTimer.reset();
        }
    
    contpart2_2.stop();
    // the Routine "EndPart2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_3_allKeys;
var Instruct2Components;
function Instruct2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruct2' ---
    t = 0;
    Instruct2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    Instruct2Components = [];
    Instruct2Components.push(text_6);
    Instruct2Components.push(key_resp_3);
    
    for (const thisComponent of Instruct2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instruct2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruct2' ---
    // get current time
    t = Instruct2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['1', '2'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instruct2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruct2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruct2' ---
    for (const thisComponent of Instruct2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "Instruct2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _contpart2_allKeys;
var EndPart1Components;
function EndPart1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'EndPart1' ---
    t = 0;
    EndPart1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    contpart2.keys = undefined;
    contpart2.rt = undefined;
    _contpart2_allKeys = [];
    // keep track of which components have finished
    EndPart1Components = [];
    EndPart1Components.push(text);
    EndPart1Components.push(contpart2);
    
    for (const thisComponent of EndPart1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndPart1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'EndPart1' ---
    // get current time
    t = EndPart1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *contpart2* updates
    if (t >= 0.0 && contpart2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      contpart2.tStart = t;  // (not accounting for frame time here)
      contpart2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { contpart2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { contpart2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { contpart2.clearEvents(); });
    }

    if (contpart2.status === PsychoJS.Status.STARTED) {
      let theseKeys = contpart2.getKeys({keyList: ['t'], waitRelease: false});
      _contpart2_allKeys = _contpart2_allKeys.concat(theseKeys);
      if (_contpart2_allKeys.length > 0) {
        contpart2.keys = _contpart2_allKeys[_contpart2_allKeys.length - 1].name;  // just the last key pressed
        contpart2.rt = _contpart2_allKeys[_contpart2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndPart1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndPart1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'EndPart1' ---
    for (const thisComponent of EndPart1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(contpart2.corr, level);
    }
    psychoJS.experiment.addData('contpart2.keys', contpart2.keys);
    if (typeof contpart2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('contpart2.rt', contpart2.rt);
        routineTimer.reset();
        }
    
    contpart2.stop();
    // the Routine "EndPart1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
