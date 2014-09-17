import subprocess
def criticalError(message):
    critical_sound_process = subprocess.Popen('aplay pacman_death.wav', shell=True,
                                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    critical_process = subprocess.Popen('./spacey.sh "' + '\033[1m\033[31m[CRITICAL]\033[0m ' + message + '"', shell=True)
    critical_process.wait()

criticalError("A critical error has occured")