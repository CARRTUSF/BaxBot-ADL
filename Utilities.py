import subprocess

def speak(message, wait=True):
    speak_process = subprocess.Popen('espeak "' + message + '"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if wait:
        speak_process.wait()