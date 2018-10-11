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
gripper = moveit_commander.MoveGroupCommander("gripper")
# display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)

# create publisher to send reset connect motor enable commands
# mover4_hardware_commands_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)


rospy.loginfo("NACHALOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

# gripper.set_named_target("GripperOpen")
# gripper.go(wait=True)

# gripper.set_named_target("GripperClose")
# gripper.go(wait=True)

# gripper.set_named_target("GripperOpen")
# gripper.go(wait=True)

# gripper.set_named_target("GripperClose")
# gripper.go(wait=True)


# gripper.clear_pose_targets()
# gripper.get_current_pose()
gripper.set_named_target("GripperClose")
gripper.go(wait=True)
# rospy.sleep(15)
# group.clear_pose_targets()
# group.get_current_pose()
# group.set_named_target("transport_position")
# group.go(wait=True)
# rospy.sleep(10)
group.set_start_state_to_current_state()
group.clear_pose_targets()
group.get_current_pose()
group.set_named_target("reach_up")
group.go(wait=True)
# rospy.sleep(15)
# gripper.set_named_target("GripperClose")
# gripper.go(wait=True)
# group.get_current_pose().pose

# state = robot.get_current_state()
# group.set_start_state(state)


# group.set_start_state(robot.get_current_state())
group.set_start_state_to_current_state()
group.clear_pose_targets()
group.get_current_pose()
# //group.set_start_state(self,group.get_current_pose().pose)
group.set_named_target("place_on_tall_table")
group.go(wait=True)
# rospy.sleep(15)
# gripper.clear_pose_targets()
# gripper.get_current_pose()
gripper.set_named_target("GripperOpen")
gripper.go(wait=True)
# rospy.sleep(15)

# group.set_start_state(robot.get_current_state())
group.set_start_state_to_current_state()
group.clear_pose_targets()
group.get_current_pose()
group.set_named_target("transport_position")
group.go(wait=True)

# gripper.set_named_target("GripperClose")
# gripper.go(wait=True)

# ....................................................

# # pose_target = geometry_msgs.msg.Pose()
# # pose_target.orientation.w = 1.0
# # pose_target.position.x = 0.96
# # pose_target.position.y = 0
# # pose_target.position.z = 1.18
# # group.set_pose_target(pose_target)  GripperOpen GripperClose

# gripper.set_named_target("GripperOpen")
# # planG1 = gripper.plan()
# # rospy.sleep(5)
# # gripper.go(wait=True)

# # plan = gripper.go(wait=True)
# # gripper.stop()

# plan = gripper.plan()
# gripper.execute(plan)
# # gripper.clear_pose_targets()
# rospy.loginfo("OTVORIIIIIIIIIIIIIIIIII")
# # rospy.sleep(10)
# rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


# gripper.set_named_target("GripperClose")
# # planG1 = gripper.plan()
# # rospy.sleep(5)
# # gripper.go(wait=True)

# # plan1 = gripper.go(wait=True)
# # gripper.stop()

# plan = gripper.plan()
# gripper.execute(plan)

# # gripper.clear_pose_targets()
# rospy.loginfo("ZATVORIIIIIIIIIIIIIIIIII")

# # rospy.sleep(10)
# rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


# # group.set_named_target("transport_position")
# # plan1 = group.plan()
# # # rospy.sleep(5)
# # group.go(wait=True)

# group.set_named_target("reach_up")
# # plan2 = group.plan()
# # rospy.sleep(5)
# # group.go(wait=True)
# # plan2 = group.go(wait=True)
# # # Calling `stop()` ensures that there is no residual movement
# # group.stop()
# # # It is always good to clear your targets after planning with poses.
# # # Note: there is no equivalent function for clear_joint_value_targets()
# # group.clear_pose_targets()
# # rospy.sleep(10)

# plan = group.plan()
# group.execute(plan)
# group.clear_pose_targets()
# rospy.loginfo("reach_up")
# # rospy.sleep(10)
# rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


# group.set_named_target("place_on_tall_table")
# # plan2 = group.plan()
# # rospy.sleep(5)
# # group.go(wait=True)
# # # plan3 = group.go(wait=True)
# # # group.stop()
# # # group.clear_pose_targets()
# # # rospy.sleep(10)
# plan = group.plan()
# group.execute(plan)
# group.clear_pose_targets()
# rospy.loginfo("place_on_tall_table")
# # rospy.sleep(10)
# rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


# gripper.set_named_target("GripperOpen")
# # planG1 = gripper.plan()
# # rospy.sleep(5)
# # gripper.go(wait=True)
# # plan4 = group.go(wait=True)
# # gripper.stop()
# # # gripper.clear_pose_targets()
# # rospy.sleep(10)
# plan = gripper.plan()
# gripper.execute(plan)
# # gripper.clear_pose_targets()
# rospy.loginfo("OTVORIIIIIIIIIIIIIIIIII")
# # rospy.sleep(10)
# rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


# group.set_named_target("release_bottle_on_tall_table")
# # plan2 = group.plan()
# # rospy.sleep(10)
# # group.go(wait=True)
# # # plan5 = group.go(wait=True)
# # # group.stop()
# # # group.clear_pose_targets()
# # # rospy.sleep(10)
# # # group.set_named_target("clear_of_tall_table")
# plan = group.plan()
# group.execute(plan)
# group.clear_pose_targets()
# rospy.loginfo("release_bottle_on_tall_table")
# # rospy.sleep(10)
# rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


# # # plan6 = group.go(wait=True)
# # # group.stop()
# # # group.clear_pose_targets()
# # # rospy.sleep(10)

# group.set_named_target("transport_position")
# # plan2 = group.plan()
# # rospy.sleep(5)
# # group.go(wait=True)
# # # plan7 = group.go(wait=True)
# # # group.stop()
# # # group.clear_pose_targets()
# # # rospy.sleep(10)
# plan = group.plan()
# group.execute(plan)
# group.clear_pose_targets()
# rospy.loginfo("transport_position")
# # rospy.sleep(10)
# rospy.loginfo("SLED SLEEPAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")


# # # gripper.set_named_target("GripperClose")
# # # # planG1 = gripper.plan()
# # # # rospy.sleep(5)
# # # # gripper.go(wait=True)
# # # plan8 = gripper.go(wait=True)
# # # gripper.stop()
# # # # gripper.clear_pose_targets()


# # gripper.set_named_target("GripperOpen")
# # gripper.go(wait=True)
# # rospy.sleep(5)
# # gripper.set_named_target("GripperClose")
# # gripper.go(wait=True)


# # https://answers.ros.org/question/249995/how-to-check-sate-of-plan-execution-in-moveit-during-async-execution-in-python/ ??stus-feedback...????

# waypoints = []

# wpose = group.get_current_pose().pose
# wpose.position.z -= scale * 0.1  # First move up (z)
# wpose.position.y += scale * 0.2  # and sideways (y)
# waypoints.append(copy.deepcopy(wpose))

# wpose.position.x += scale * 0.1  # Second move forward/backwards in (x)
# waypoints.append(copy.deepcopy(wpose))

# wpose.position.y -= scale * 0.1  # Third move sideways (y)
# waypoints.append(copy.deepcopy(wpose))

# # We want the Cartesian path to be interpolated at a resolution of 1 cm
# # which is why we will specify 0.01 as the eef_step in Cartesian
# # translation.  We will disable the jump threshold by setting it to 0.0 disabling:
# (plan, fraction) = group.compute_cartesian_path(
#                                    waypoints,   # waypoints to follow
#                                    0.01,        # eef_step
#                                    0.0)         # jump_threshold

# # Note: We are just planning, not asking move_group to actually move the robot yet:
# return plan, fraction



# Cleanly shut down MoveIt!
moveit_commander.roscpp_shutdown()
# Exit the script
moveit_commander.os._exit(0)