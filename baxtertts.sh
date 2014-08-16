pico2wave -l=en-US -w=/tmp/baxtertts.wav "$1"
aplay /tmp/baxtertts.wav
rm /tmp/baxtertts.wav
