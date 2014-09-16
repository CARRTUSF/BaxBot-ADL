# ROS
import rospy

# Baxter
import BaxterControl
import BaxterMoveIt

import OPEAssist
# import Utilities

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

        else:
            print "No objects detected...."

if __name__ == "__main__":
    try:
        app = MainApplication()
        app.main()
    except rospy.ROSInterruptException:
        pass
