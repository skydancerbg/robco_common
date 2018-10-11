
!/usr/bin/env python



# From
# https://github.com/RobotnikAutomation/training/blob/indigo-devel/mico/mico_arm_nav/scripts/get_arm_pose.py


# """
# Display the current joint positions of the arm in kinematic order of the links
# """

# import rospy, sys
# import moveit_commander
# from moveit_commander import MoveGroupCommander

# class GetJointStates:
#     def __init__(self):
#         # Initialize the move_group API
#         moveit_commander.roscpp_initialize(sys.argv)

#         # Initialize the ROS node
#         rospy.init_node('get_joint_states', anonymous=True)
                
#         # Initialize the MoveIt! commander for the arm
#         arm = MoveGroupCommander('arm')
        
#         # Get the end-effector link
#         end_effector_link = arm.get_end_effector_link()
        
#         # Joints are stored in the order they appear in the kinematic chain
#         joint_names = arm.get_active_joints()
        
#         joint_names = ['mico_joint_1',
#                        'mico_joint_2',
#                        'mico_joint_3',
#                        'mico_joint_4',
#                        'mico_joint_5',
#                        'mico_joint_6'
#                        ]
        
#         # Display the joint names
#         rospy.loginfo("Joint names:\n"  + str(joint_names) + "\n")
        
#         # Get the current joint angles
#         joint_values = arm.get_current_joint_values()
        
#         # Display the joint values
#         rospy.loginfo("Joint values:\n"  + str(joint_values) + "\n")
        
#         # Get the end-effector pose
#         ee_pose = arm.get_current_pose(end_effector_link)
        
#         # Display the end-effector pose
#         rospy.loginfo("End effector pose:\n" + str(ee_pose))
        
#         moveit_commander.roscpp_shutdown()
#         moveit_commander.os._exit(0)

# if __name__ == "__main__":
#     GetJointStates()

# From :
    # https://github.com/pirobot/rbx2/blob/indigo-devel/rbx2_arm_nav/src/rbx2_arm_nav/arm_utils.py
# Ros by example vol 2

    #!/usr/bin/env python

"""
    arm_utils.py - Version 0.1 2014-01-14
    
    Utitilties for working with multijointed arms
    
    Created for the Pi Robot Project: http://www.pirobot.org
    Copyright (c) 2014 Patrick Goebel.  All rights reserved.
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.5
    
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details at:
    
    http://www.gnu.org/licenses/gpl.html
"""

import rospy
from moveit_msgs.msg import RobotTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from geometry_msgs.msg import PoseStamped, Pose

def scale_trajectory_speed(traj, scale):
       # Create a new trajectory object
       new_traj = RobotTrajectory()
       
       # Initialize the new trajectory to be the same as the input trajectory
       new_traj.joint_trajectory = traj.joint_trajectory
       
       # Get the number of joints involved
       n_joints = len(traj.joint_trajectory.joint_names)
       
       # Get the number of points on the trajectory
       n_points = len(traj.joint_trajectory.points)
        
       # Store the trajectory points
       points = list(traj.joint_trajectory.points)
       
       # Cycle through all points and joints and scale the time from start,
       # as well as joint speed and acceleration
       for i in range(n_points):
           point = JointTrajectoryPoint()
           
           # The joint positions are not scaled so pull them out first
           point.positions = traj.joint_trajectory.points[i].positions

           # Next, scale the time_from_start for this point
           point.time_from_start = traj.joint_trajectory.points[i].time_from_start / scale
           
           # Get the joint velocities for this point
           point.velocities = list(traj.joint_trajectory.points[i].velocities)
           
           # Get the joint accelerations for this point
           point.accelerations = list(traj.joint_trajectory.points[i].accelerations)
           
           # Scale the velocity and acceleration for each joint at this point
           for j in range(n_joints):
               point.velocities[j] = point.velocities[j] * scale
               point.accelerations[j] = point.accelerations[j] * scale * scale
        
           # Store the scaled trajectory point
           points[i] = point

       # Assign the modified points to the new trajectory
       new_traj.joint_trajectory.points = points

       # Return the new trajecotry
       return new_traj
   
def set_trajectory_speed(traj, speed):
       # Create a new trajectory object
       new_traj = RobotTrajectory()
       
       # Initialize the new trajectory to be the same as the input trajectory
       new_traj.joint_trajectory = traj.joint_trajectory
       
       # Get the number of joints involved
       n_joints = len(traj.joint_trajectory.joint_names)
       
       # Get the number of points on the trajectory
       n_points = len(traj.joint_trajectory.points)
        
       # Store the trajectory points
       points = list(traj.joint_trajectory.points)
       
       # Cycle through all points and joints and scale the time from start,
       # as well as joint speed and acceleration
       for i in range(n_points):
           point = JointTrajectoryPoint()
           
           # The joint positions are not scaled so pull them out first
           point.positions = traj.joint_trajectory.points[i].positions

           # Next, scale the time_from_start for this point
           point.time_from_start = traj.joint_trajectory.points[i].time_from_start
           
           # Initialize the joint velocities for this point
           point.velocities = [speed] * n_joints
           
           # Get the joint accelerations for this point
           point.accelerations = [speed / 4.0] * n_joints
        
           # Store the scaled trajectory point
           points[i] = point

       # Assign the modified points to the new trajectory
       new_traj.joint_trajectory.points = points

       # Return the new trajecotry
       return new_traj