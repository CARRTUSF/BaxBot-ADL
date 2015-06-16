# Copyright (c) 2014, Andoni Aguirrezabal
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import subprocess

objCount = 0
objList = []
selectedObject = 0
tablePos = []
tableSize= []


def runOPE(wait=True):
    ope_process = subprocess.Popen("./ope-init.sh", shell=True,
                                                            cwd="./OPE-Release/")
    if wait:
        ope_process.wait()

def loadOPEResults():
    global objCount
    global objList
    global selectedObject
    global tablePos
    global tableSize

    ope_results = open("./OPE-Release/OPE-Results.txt")

    objCount = int(ope_results.readline())
    selectedObject = int(ope_results.readline())

    if objCount > 0:
        tablePos = [float(x) for x in ope_results.readline().split()]
        tableSize = [float(x) for x in ope_results.readline().split()]

        # GLOBAL TABLE ADJUSTMENT
        tablePos[0] = tablePos[0] - 0 # X
        tablePos[1] = tablePos[1] - 0 # Y
        tablePos[2] = tablePos[2] - 0 # Z

        for k in range(objCount):
            ope_results.readline()
            temp_objPos = [float(x) for x in ope_results.readline().split()]
            temp_objSize = [float(x) for x in ope_results.readline().split()]
            temp_objRot = [float(x) for x in ope_results.readline().split()]

            # GLOBAL OBJECT ADJUSTMENT
            temp_objPos[0] = temp_objPos[0] - 0# X
            temp_objPos[1] = temp_objPos[1] - 0 # Y
            temp_objPos[2] = temp_objPos[2] - 0 # Z

            objList.append({'objNumber':k,
                            'objPos':temp_objPos,
                            'objSize':temp_objSize,
                            'objRot':temp_objRot})

    ope_results.close()

def showOPEResults():
    subprocess.Popen("ristretto output.png", shell=True,
                                   cwd="./OPE-Release/")
