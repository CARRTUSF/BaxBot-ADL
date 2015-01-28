# ROS
import rospy

# Baxter
import BaxterControl
import BaxterMoveIt
import BaxterPositions

# OPE
import OPEAssist

# OTHER
import copy
import os
from subprocess import Popen
import Utilities
from Utilities import speak


class MainApplication:
    def __init__(self):
        self.my_env = os.environ

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

    def main(self):
        # Set the face
        rr = "rosrun baxter_examples xdisplay_image.py --file=./Images/USF_GreenGold.png"
        Popen(rr, env=self.my_env, shell=True, preexec_fn=os.setsid)
        
        if self.gotoWaiting():
            # Execute OPE
            print "Running OPE, please wait...."
            # OPEAssist.runOPE()
            OPEAssist.loadOPEResults()

            rospy.sleep(2)

            if OPEAssist.objCount > 0:
                # ADD Table Collision Model
                self.moveit.addObject("TABLE",
                                      OPEAssist.tablePos,
                                      OPEAssist.tableSize)

                # ADD Object Collision Models
                for x in OPEAssist.objList:
                    self.moveit.addObject("OBJECT" + str(x['objNumber']),
                                          x['objPos'],
                                          x['objSize'])

                rospy.sleep(1)

                OPEAssist.showOPEResults()
                speak("Which Object would you like?")
                rr = "rosrun baxter_examples xdisplay_image.py --file=./OPE-Release/output.png"
                Popen(rr, env=self.my_env, shell=True, preexec_fn=os.setsid)
                objectNum = int(raw_input("Which Object would you like? "))

                print "\n==ACTIONS LIST=="
                print "1) TRASH"
                print "2) BRING TO ME"
                print "3) ABORT"
                speak("What would you like me to do with this object?")
                action = int(raw_input("Select an action: "))

                rr = "rosrun baxter_examples xdisplay_image.py --file=./Faces/focused_2.png"
                Popen(rr, env=self.my_env, shell=True, preexec_fn=os.setsid)

                if action == 1:
                    self.trashObject(OPEAssist.objList[objectNum]['objPos'], [0, 0, 0, 0],
                                     BaxterPositions.trashPos, objectNum)
                elif action == 2:
                    self.bringToUser(OPEAssist.objList[objectNum]['objPos'], [0, 0, 0, 0], objectNum)
                else:
                    pass
            else:
                print "No objects detected...."
                speak("No objects detected....")
        else:
            Utilities.criticalError("Could not go to waiting position, aborting.....")

    def gotoWaiting(self):
        print "Going to waiting position...."
        # speak("Going to waiting position....")

        waitingPlan = self.moveit.createPath(BaxterPositions.waitingPos, BaxterPositions.waitingRot)
        if self.moveit.group.execute(waitingPlan):
            return True
        else:
            print "Could not move to waiting position!"
            # speak("Could not move to waiting position!")
            return False

    def setJointPositioWaiting(self):
        self.baxter.setJointPositions(BaxterPositions.goodWaitingPose, "left")

    def bringToUser(self, objectLoc, objectRot, objectNum):
        # PRE-OBJECT POSE
        preObjectLoc = copy.deepcopy(objectLoc)
        preObjectLoc[0] = preObjectLoc[0] - 0.1 # subtract 0.1 meters in x

        # OBJECT POSE (RAISED)
        objectRaisedLoc = copy.deepcopy(objectLoc)
        objectRaisedLoc[2] = objectRaisedLoc[2] + 0.2

        # Extend POSE (RAISED)
        extendRaisedLoc = copy.deepcopy(objectRaisedLoc)
        extendRaisedLoc[0] = extendRaisedLoc[0] + 0.2

        print "Going to pre-object position...."
        # speak("Going to pre-object position....")
        preObjectPlan = self.moveit.createPath(preObjectLoc, BaxterPositions.normalRot)
        if not self.moveit.group.execute(preObjectPlan):
            print "Could not move to pre-object position!"
            # speak("Could not move to pre-object position!")
            return False

        self.moveit.scene.remove_world_object("OBJECT" + str(objectNum))
        rospy.sleep(1)

        print "Opening gripper...."
        # speak("Opening gripper....")
        self.baxter.leftGripper.command_position(100)
        rospy.sleep(1)

        print "Going to object position...."
        # speak("Going to object position....")
        objectPlan = self.moveit.createPath(objectLoc, BaxterPositions.normalRot)
        if not self.moveit.group.execute(objectPlan):
            print "Could not move to object position!"
            # speak("Could not move to object position!")
            return False
        rospy.sleep(1)

        print "Closing gripper..."
        # speak("Closing gripper...")
        self.baxter.leftGripper.command_position(0)
        rospy.sleep(1)

        print "Going to object (raised) position...."
        # speak("Going to object (raised) position....")
        objectRaisedPlan = self.moveit.createPath(objectRaisedLoc, BaxterPositions.normalRot)
        if not self.moveit.group.execute(objectRaisedPlan):
            print "Could not move to object (raised) position!"
            # speak("Could not move to object (raised) position!")
            return False
        rospy.sleep(1)

        rr = "rosrun baxter_examples xdisplay_image.py --file=./Faces/neutral_1.png"
        Popen(rr, env=self.my_env, shell=True, preexec_fn=os.setsid)

        raw_input("Reverse PowerBot and Navigate to User Now....")

        print "Going to extended (raised) position...."
        # speak("Going to extended (raised) position....")
        extendRaisedPlan = self.moveit.createPath(extendRaisedLoc, BaxterPositions.normalRot)
        if not self.moveit.group.execute(extendRaisedPlan):
            print "Could not move to extended (raised) position!"
            # speak("Could not move to extended (raised) position!")
            return False
        rospy.sleep(1)

        raw_input("Do you want it?")
        speak("Here you are!")

        print "Opening gripper...."
        # speak("Opening gripper....")
        self.baxter.leftGripper.command_position(100)

        return True

    def trashObject(self, objectLoc, objectRot, trashLoc, objectNum):
        # PRE-OBJECT POSE
        preObjectLoc = copy.deepcopy(objectLoc)
        preObjectLoc[0] = preObjectLoc[0] - 0.1 # subtract 0.1 meters in x

        # OBJECT POSE (RAISED)
        objectRaisedLoc = copy.deepcopy(objectLoc)
        objectRaisedLoc[2] = objectRaisedLoc[2] + 0.2

        print "Going to pre-object position...."
        # speak("Going to pre-object position....")
        preObjectPlan = self.moveit.createPath(preObjectLoc, BaxterPositions.normalRot)
        if not self.moveit.group.execute(preObjectPlan):
            print "Could not move to pre-object position!"
            speak("Could not move to pre-object position!")
            return False

        self.moveit.scene.remove_world_object("OBJECT" + str(objectNum))
        rospy.sleep(1)

        print "Opening gripper...."
        # speak("Opening gripper....")
        self.baxter.leftGripper.command_position(100)
        rospy.sleep(1)

        print "Going to object position...."
        # speak("Going to object position....")
        objectPlan = self.moveit.createPath(objectLoc, BaxterPositions.normalRot)
        if not self.moveit.group.execute(objectPlan):
            print "Could not move to object position!"
            return False
        rospy.sleep(1)

        print "Closing gripper..."
        # speak("Closing gripper...")
        self.baxter.leftGripper.command_position(0)
        rospy.sleep(1)

        print "Going to object (raised) position...."
		# speak("Going to object (raised) position....")
        objectRaisedPlan = self.moveit.createPath(objectRaisedLoc, BaxterPositions.normalRot)
        if not self.moveit.group.execute(objectRaisedPlan):
            print "Could not move to object (raised) position!"
			# speak("Could not move to object (raised) position!")
            return False
        rospy.sleep(1)

        rr = "rosrun baxter_examples xdisplay_image.py --file=./Faces/neutral_1.png"
        Popen(rr, env=self.my_env, shell=True, preexec_fn=os.setsid)

        print "Going to trash position...."
        # speak("Going to trash position....")
        trashObjectPlan = self.moveit.createPath(trashLoc, BaxterPositions.normalRot)
        if not self.moveit.group.execute(trashObjectPlan):
            print "Could not move to trash position!"
            speak("Could not move to trash position!")
            return False
        rospy.sleep(1)

        print "Opening gripper...."
        # speak("Opening gripper....")
        self.baxter.leftGripper.command_position(100)
        rospy.sleep(1)

        return True

        # if self.gotoWaiting():
        #     return True
        # else:
        #     return False

if __name__ == "__main__":
    try:
        app = MainApplication()
        app.main()
    except rospy.ROSInterruptException:
        pass
