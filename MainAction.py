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

# ROS
import rospy

# Baxter
import BaxterControl
import BaxterMoveIt

# Pose Locations
import BaxterPositions

# Networking
import BCISocket

class MainApplication:
    def __init__(self):
        # Initialize ROS node
        print "Initializing ROS...."
        rospy.init_node('carrt_demo_python', anonymous=True)

        # Grab Baxter Controller
        print "Initializing Baxter...."
        self.baxter = BaxterControl.BaxterControl()

        # Calibrate Gripper
        print "Calibrating Gripper...."
        self.baxter.gripperCalibrate("left")

        # Grab MoveIt Controller for Baxter
        print "Initializing MoveIt...."
        self.moveit = BaxterMoveIt.BaxterMoveIt()

        # Initialize Socket Engine
        print "Initializing BCI Socket...."
        self.bciSocket = BCISocket.BCISocket()

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
                pass
            else:
                return False

    def gotoCamera(self, objectLoc):
        print "Going to camera location...."
        return self.moveit.group.execute(self.moveit.createPath(objectLoc))

    def gotoWaiting(self):
        print "Going to waiting position...."
        return self.moveit.group.execute(self.moveit.createPath(BaxterPositions.waitingPose))

    def trashObject(self, objectLoc):
        pass

if __name__ == "__main__":
    try:
        app = MainApplication()
        app.main()
    except rospy.ROSInterruptException:
        pass
