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
        rospy.init_node('carrt_jpostest_python', anonymous=True)

        # Grab Baxter Controller
        print "Initializing Baxter...."
        self.baxter = BaxterControl.BaxterControl()

        # Calibrate Gripper
        print "Calibrating Gripper...."
        # self.baxter.gripperCalibrate("left")

        # Grab MoveIt Controller for Baxter
        print "Initializing MoveIt...."
        # self.moveit = BaxterMoveIt.BaxterMoveIt()

    def main(self):
        self.setJointPositioWaiting()

    def setJointPositioWaiting(self):
        self.baxter.setJointPositions(BaxterPositions.goodWaitingPose, "left")

if __name__ == "__main__":
    try:
        app = MainApplication()
        app.main()
    except rospy.ROSInterruptException:
        pass
