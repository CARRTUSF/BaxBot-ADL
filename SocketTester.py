#!/usr/bin/env python

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

import BCISocket

class MainApplication:
    def __init__(self):
        self.socket = BCISocket.BCISocket()

    def main(self):
        while True:
            commandArgs = self.socket.waitForCommand()
            self.parseAction(commandArgs)

    def parseAction(self, commandArgs):
        if len(commandArgs) > 0:
            command = commandArgs[0]
            commandArgs = commandArgs[1:]

            print "COMMAND RECEIVED:", command

            if command == "GO_TO_WAITING":
                self.gotoWaiting()
            elif command == "CAMERA_VIEW_CLOSE":
                pass
            elif command == "TRASH":
                if(len(commandArgs) == 9):
                    objectLoc = [float(listItem) for listItem in commandArgs[0:3]]
                    objectRot = [float(listItem) for listItem in commandArgs[3:6]]
                    trashLoc = [float(listItem) for listItem in commandArgs[6:9]]
                    return self.trashObject(objectLoc, objectRot, trashLoc)
                else:
                    return False
            else:
                return False

    def gotoCamera(self, objectLoc):
        print "Going to camera location...."

    def gotoWaiting(self):
        print "Going to waiting position...."

    def trashObject(self, objectLoc, objectRot, trashLoc):
        return True

if __name__ == "__main__":
    app = MainApplication()
    app.main()
