#!/bin/sh 

echo "Set full path of map: " MAP
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$MAP