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
import Utilities

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

    def main(self):
        # Execute OPE
        print "Running OPE, please wait...."
        OPEAssist.runOPE()
        OPEAssist.loadOPEResults()

        rospy.sleep(2)

        if OPEAssist.objCount > 0:
            self.moveit.addObject("TABLE",
                                  OPEAssist.tablePos,
                                  OPEAssist.tableSize)

            rospy.sleep(1)

            for x in OPEAssist.objList:
                self.moveit.addObject("OBJECT" + str(x['objNumber']),
                                      x['objPos'],
                                      x['objSize'])

            rospy.sleep(1)

            if self.gotoWaiting():
                self.trashObject([0, 0, 0], [0, 0, 0, 0], BaxterPositions.trashPos)
            else:
                Utilities.criticalError("Could not go to waiting position, aborting.....")

        else:
            print "No objects detected...."

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
        trashObjectPlan = self.moveit.createPath(trashLoc, BaxterPositions.normalRot)
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
