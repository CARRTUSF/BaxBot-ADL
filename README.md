BaxBot-ADL
==========

## Launching the example
* First, make sure Baxter is enabled. To do this, type the following in a new Baxter SDK terminal window:

    ```
    rosrun baxter_tools enable_robot.py -e
    ```

* Next, in the same Baxter SDK terminal window type the following:

    ```
    rosrun baxter_interface joint_trajectory_action_server.py
    ```

    This will launch the trajectory action server for Baxter

* In another new Baxter SDK terminal window type the following:

    ```
    roslaunch baxter_moveit_config demo_baxter.launch
    ```

    This will launch MoveIt! for use with Baxter

* Finally, in another new Baxter SDK terminal run the MainAction.py program with:

    ```
    python MainAction.py
    ```
