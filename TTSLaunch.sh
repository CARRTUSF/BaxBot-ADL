#!/bin/bash
pico2wave -l=en-US -w=./test.wav "$1"
aplay ./test.wav
rm ./test.wav
