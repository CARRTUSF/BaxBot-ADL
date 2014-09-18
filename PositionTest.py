# ROS
import rospy

# Baxter
import BaxterControl
import BaxterMoveIt
import BaxterPositions

# Other
import Utilities

class MainApplication:
    def __init__(self):
        # Initialize ROS node
        print "Initializing ROS...."
        rospy.init_node('carrt_testpos_python', anonymous=True)

        # Grab Baxter Controller
        print "Initializing Baxter...."
        self.baxter = BaxterControl.BaxterControl()

        # Calibrate Gripper
        print "Calibrating Gripper...."
        # self.baxter.gripperCalibrate("left")

        # Grab MoveIt Controller for Baxter
        print "Initializing MoveIt...."
        self.moveit = BaxterMoveIt.BaxterMoveIt()

    def main(self):
        print "Adjusting Coordinates...."
        BaxterPositions.testPos[0]  = BaxterPositions.testPos[0] - 0.15 # X
        BaxterPositions.testPos[1]  = BaxterPositions.testPos[1] - 0.02 # Y
        BaxterPositions.testPos[2]  = BaxterPositions.testPos[2] - 0.0 # Z

        print "Going to test position...."
        testPlan = self.moveit.createPath(BaxterPositions.testPos, BaxterPositions.testRot)
        if self.moveit.group.execute(testPlan):
            return True
        else:
            Utilities.criticalError("Could not move to test position!")
            return False

if __name__ == "__main__":
    try:
        app = MainApplication()
        app.main()
    except rospy.ROSInterruptException:
        pass
