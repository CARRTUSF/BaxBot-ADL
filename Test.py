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

class TestApplication:
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
        # Execute OPE
        print "Running OPE, please wait...."
        # OPEAssist.runOPE()
        OPEAssist.loadOPEResults()

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

            rr = "rosrun baxter_examples xdisplay_image.py --file=./OPE-Release/output.png"
            Popen(rr, env=self.my_env, shell=True, preexec_fn=os.setsid)
            objectNum = int(raw_input("Which Object would you like? "))

            selectedObjPos = OPEAssist.objList[objectNum]['objPos']
            preObjectLoc = copy.deepcopy(selectedObjPos)
            preObjectLoc[0] = preObjectLoc[0] - 0.1

            raw_input("Press Enter to continue...")

            preObjectPlan = self.moveit.createPath(preObjectLoc, 0, BaxterPositions.normalRot)
            if not self.moveit.leftGroup.execute(preObjectPlan):
                print "Could not move to pre-object position!"
                return False

            raw_input("Press Enter to continue...")

            selectedObjectPlan = self.moveit.createPath(selectedObjPos, 0, BaxterPositions.normalRot)
            if not self.moveit.leftGroup.execute(selectedObjectPlan):
                print "Could not move to pre-object position!"
                return False

if __name__ == "__main__":
    try:
        app = TestApplication()
        app.main()
    except rospy.ROSInterruptException:
        pass
