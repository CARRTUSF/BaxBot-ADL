import subprocess

def speak(message, wait=True):
    speak_process = subprocess.Popen('espeak "' + message + '"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if wait:
        speak_process.wait()

def criticalError(message):
    critical_sound_process = subprocess.Popen('aplay pacman_death.wav', shell=True,
                                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                              cwd="./ErrorLib/")
    critical_process = subprocess.Popen('./spacey.sh "' + '\033[1m\033[31m[CRITICAL]\033[0m ' + message + '"', shell=True,
                                        cwd="./ErrorLib/")
    critical_process.wait()
