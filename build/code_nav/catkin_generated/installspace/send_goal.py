#!/usr/bin/env python3


import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client():

    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
    client.wait_for_server()

    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
    goal.target_pose.pose.position.x = -0.5813636779785156
    goal.target_pose.pose.position.y = 2.040489673614502
    goal.target_pose.pose.orientation.w = 0.1

    client.send_goal(goal)
    wait = client.wait_for_result()
    rospy.loginfo("Arrived on 1. point")


    goal.target_pose.pose.position.x = -1.6181565523147583
    goal.target_pose.pose.position.y = 1.4766523838043213
    goal.target_pose.pose.orientation.w = 0.1

    client.send_goal(goal)    
    wait = client.wait_for_result()
    rospy.loginfo("Arrived on 2. point")

    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
        return client.get_result()


    



if __name__ == '__main__':
    try:
        rospy.init_node('movebase_client_py')
        result = movebase_client()
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")

