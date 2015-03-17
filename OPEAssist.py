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