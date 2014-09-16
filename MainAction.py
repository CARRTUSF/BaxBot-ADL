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

# Python
import copy

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
            commandArgs = self.bciSocket.waitForCommand()
            if (self.parseAction(commandArgs)):
                print "Action complete!"
                self.bciSocket.sendMessage("DONE\n")

    def parseAction(self, commandArgs):
        if len(commandArgs) > 1:
            if commandArgs[0] == "COMMAND":
                command = commandArgs[1]
                commandArgs = commandArgs[2:]

                print "COMMAND RECEIVED:", command

                if command == "GO_TO_WAITING":
                    return self.gotoWaiting()
                elif command == "CAMERA_VIEW_CLOSE":
                    if(len(commandArgs) == 6):
                        objectLoc = [(float(listItem)/1000) for listItem in commandArgs[0:3]]
                        return self.gotoCamera(objectLoc)
                    else:
                        return False
                elif command == "TRASH":
                    if(len(commandArgs) == 9):
                        objectLoc = [(float(listItem)/1000) for listItem in commandArgs[0:3]]
                        objectRot = [float(listItem) for listItem in commandArgs[3:6]]
                        trashLoc = [float(listItem) for listItem in commandArgs[6:9]]
                        return self.trashObject(objectLoc, objectRot, trashLoc)
                    else:
                        return False
                else:
                    print "Message Format Wrong (Action Not Implemented)!"
                    return False
            else:
                print "Message Format Wrong (KEYWORD Missing)!"
                return False
        else:
            print "Message Format Wrong (Not Enough Arguments)!"
            return False

    def gotoCamera(self, objectLoc):
        print "Going to camera position...."
        if (self.moveit.group.execute(self.moveit.createPath(objectLoc))):
            return True
        else:
            print "Could not move to camera position!"
            return False

    def gotoWaiting(self):
        print "Going to waiting position...."
        waitingPlan = self.moveit.createPath(BaxterPositions.waitingPose, BaxterPositions.normalRot)
        if (self.moveit.group.execute(waitingPlan)):
            return True
        else:
            print "Could not move to waiting position!"
            return False

    def trashObject(self, objectLoc, objectRot, trashLoc):
        # PRE-OBJECT POSE
        preObjectLoc = copy.deepcopy(objectLoc)
        preObjectLoc[0] = preObjectLoc[0] # subtract 0.2 meters in x

        # PRE-OBJECT POSE (RAISED)
        preObjectRaisedLoc = copy.deepcopy(preObjectLoc)
        preObjectRaisedLoc = preObjectRaisedLoc[1] + 0.2

        print "Going to pre-object position...."
        preObjectPlan = self.moveit.createPath(preObjectLoc, BaxterPositions.normalRot)
        if not self.moveit.group.execute(preObjectPlan):
            print "Could not move to pre-object position!"
            return False

        print "Opening gripper...."
        self.baxter.leftGripper.command_position(100)

        print "Going to object position...."
        objectPlan = self.moveit.createPath(objectLoc, BaxterPositions.normalRot)
        if not self.moveit.group.execute(objectPlan):
            print "Could not move to object position!"
            return False

        print "Closing gripper..."
        self.baxter.leftGripper.command_position(65)

        print "Going to pre-object (raised) position...."
        preObjectRaisedPlan = self.moveit.createPath(preObjectRaisedLoc, BaxterPositions.normalRot)
        if not self.moveit.group.execute(preObjectRaisedPlan):
            print "Could not move to pre-object (raised) position!"
            return False

        print "Going to trash position...."
        trashObjectPlan = self.moveit.createPath(BaxterPositions.trashPos, BaxterPositions.normalRot)
        if not self.moveit.group.execute(trashObjectPlan):
            print "Could not move to trash position!"
            return False

        print "Opening gripper...."
        self.baxter.leftGripper.command_position(100)

        if (self.gotoWaiting()):
            return True
        else:
            return False

if __name__ == "__main__":
    try:
        app = MainApplication()
        app.main()
    except rospy.ROSInterruptException:
        pass
