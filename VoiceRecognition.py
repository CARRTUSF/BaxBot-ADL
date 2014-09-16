import urllib2
import json

import sys

def recognizeSpeech():
    audioFile = open("audio.flac")
    audioData = audioFile.read()
    audioFile.close()

    googleSpeechRequest = urllib2.Request('https://www.google.com/speech-api/v2/recognize?output=json&lang=en-us&key=AIzaSyBOti4mM-6x9WDnZIjIeyEU21OpBXqWBgw&results=6&pfilter=2',
                                           data=audioData, headers={'Content-type': 'audio/x-flac; rate=8000'})

    try:
        googleSpeechResponse = urllib2.urlopen(googleSpeechRequest)
    except urllib2.URLError, e:
        print "Error Recognizing Speech"
        sys.exit(1)

    rawData = googleSpeechResponse.readlines()[1:][0]
    jsonData = json.loads(rawData)
    resultIndex = int(jsonData["result_index"])

    return jsonData["result"][0]["alternative"][resultIndex]["transcript"]
