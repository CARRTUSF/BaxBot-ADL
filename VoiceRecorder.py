import pygst
pygst.require('0.10')
import gst

import time

class VoiceRecorder:
    def __init__(self):
        self.recordingOn = 0
        self.pipeline = gst.parse_launch('gconfaudiosrc ! audioconvert ! audioresample '
                                         + '! vader name=vad auto-threshold=true '
                                         + '! flacenc '
                                         + '! filesink location=audio.flac')

        vader = self.pipeline.get_by_name('vad')
        vader.connect('vader_start', self.detected)
        vader.connect('vader_stop', self.lost)

        self.pipeline.set_state(gst.STATE_PAUSED)

    def beginrecording(self):
        self.recordingOn = 1
        self.pipeline.set_state(gst.STATE_PLAYING)

    def detected(self, vad, text):
        print "Sound Detected"

    def lost(self, vad, text):
        print "Sound Lost"
        self.recordingOn = 0
        self.pipeline.set_state(gst.STATE_PAUSED)

