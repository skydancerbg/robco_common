#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

moveit_commander.roscpp_initialize(sys.argv)
# rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
rospy.init_node('mover4_move_group_python_interface', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()    
group = moveit_commander.MoveGroupCommander("robot")
# gripper = moveit_commander.MoveGroupCommander("gripper")


rospy.loginfo("release_bottle_on_tall_table execute.py")



group.get_current_pose()
group.set_named_target("release_bottle_on_tall_table")
group.go(wait=True)


moveit_commander.roscpp_shutdown()