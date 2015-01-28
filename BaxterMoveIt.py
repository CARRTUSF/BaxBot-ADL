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
import geometry_msgs.msg

# MoveIt
import moveit_commander
import moveit_msgs.msg

import sys

class BaxterMoveIt:
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)

        # initialize MoveIt
        self.robot = moveit_commander.RobotCommander()
        self.scene = moveit_commander.PlanningSceneInterface()
        self.leftGroup = moveit_commander.MoveGroupCommander("left_arm")
        self.rightGroup = moveit_commander.MoveGroupCommander("right_arm")
        self.display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                            moveit_msgs.msg.DisplayTrajectory)

    def __del__(self):
        moveit_commander.roscpp_shutdown()

    def addObject(self, objName, objPos, objSize, objRot = [0, 0, 0, 1]):
        """Adds collision object to the environment
           objName, objPos, objSize, objRot
        """
        objPose = geometry_msgs.msg.PoseStamped()
        objPose.header.frame_id = self.robot.get_planning_frame()
        objPose.pose.position.x = objPos[0]
        objPose.pose.position.y = objPos[1]
        objPose.pose.position.z = objPos[2]
        objPose.pose.orientation.x = objRot[0]
        objPose.pose.orientation.y = objRot[1]
        objPose.pose.orientation.z = objRot[2]
        objPose.pose.orientation.w = objRot[3]
        self.scene.add_box(objName, objPose, (objSize[0], objSize[1], objSize[2]))

    def createPath(self, objpos, arm=0, gripperorientation=[0, 0.74419, 0, 0.6679]):
        pose_target = geometry_msgs.msg.Pose()
        pose_target.orientation.x = gripperorientation[0]
        pose_target.orientation.y = gripperorientation[1]
        pose_target.orientation.z = gripperorientation[2]
        pose_target.orientation.w = gripperorientation[3]
        pose_target.position.x = objpos[0]
        pose_target.position.y = objpos[1]
        pose_target.position.z = objpos[2]

        if arm == 0:
            self.leftGroup.set_start_state_to_current_state()
            self.leftGroup.set_pose_target(pose_target)

            return self.leftGroup.plan()
        else:
            self.rightGroup.set_start_state_to_current_state()
            self.rightGroup.set_pose_target(pose_target)

            return self.rightGroup.plan()
