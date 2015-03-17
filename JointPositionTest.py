# PYTHON
import signal
import sys

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
        self.baxter.gripperCalibrate("left")

        # Grab MoveIt Controller for Baxter
        print "Initializing MoveIt...."
        self.moveit = BaxterMoveIt.BaxterMoveIt()

    def exit(self, signal, frame):
        sys.exit(0)

    def main(self):
        raw_input("Press Enter to continue....")
        pathPlan = self.moveit.createPath(BaxterPositions.testPosStart, BaxterPositions.testRotStart)
        raw_input("Verify path plan....")
        if not self.moveit.group.execute(pathPlan):
            print "Could not execute path plan!"

        raw_input("Press Enter to continue....")
        pathPlan = self.moveit.createPath(BaxterPositions.testPosEnd, BaxterPositions.testRotEnd)
        raw_input("Verify path plan....")
        if not self.moveit.group.execute(pathPlan):
            print "Could not execute path plan!"

if __name__ == "__main__":
    try:
        app = MainApplication()
        signal.signal(signal.SIGINT, app.exit)
        app.main()
    except rospy.ROSInterruptException:
        pass