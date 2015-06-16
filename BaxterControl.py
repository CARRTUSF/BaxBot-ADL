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

# Baxter
import baxter_interface
from baxter_interface import CHECK_VERSION


class BaxterControl:
    def __init__(self):
        # initialize interfaces
        rs = baxter_interface.RobotEnable(CHECK_VERSION)
        init_state = rs.state().enabled

        self.leftGripper = baxter_interface.Gripper('left', CHECK_VERSION)
        self.rightGripper = baxter_interface.Gripper('right', CHECK_VERSION)

        # MANUAL JOINT CONTROL
        self.leftLimb = baxter_interface.Limb('left')
        self.rightLimb = baxter_interface.Limb('right')
        self.manualJointAccuracy = baxter_interface.settings.JOINT_ANGLE_TOLERANCE
        self.manualJointTimeout = 20.0

        # JOINT SPEEDS
        self.manualJointSpeed = 0.3
        self.leftLimb.set_joint_position_speed(self.manualJointSpeed)
        self.rightLimb.set_joint_position_speed(self.manualJointSpeed)

    def gripperCalibrate(self, selectedGripper):
        if selectedGripper.lower() == 'left':
            self.leftGripper.calibrate()
        elif selectedGripper.lower() == 'right':
            self.rightGripper.calibrate()
        elif selectedGripper.lower() == 'both':
            self.leftGripper.calibrate()
            self.rightGripper.calibrate()

    def setJointPositions(self, jointPositions, selectedLimb):
        if selectedLimb.lower() == 'left':
            self.leftLimb.move_to_joint_positions(jointPositions, self.manualJointTimeout, self.manualJointAccuracy)
        elif selectedLimb.lower() == 'right':
            self.rightLimb.move_to_joint_positions(jointPositions, self.manualJointTimeout, self.manualJointAccuracy)
