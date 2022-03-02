#!/bin/sh 

echo "1 empty_world"
echo "2 turtlebot3_world"
echo "3 turtlebot3_house"

read -p "Choose your world: " RESULT


export TURTLEBOT3_MODEL=burger

if [ $RESULT = 1 ] 
then
    roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
fi

if [ $RESULT = 2 ] 
then
    roslaunch turtlebot3_gazebo turtlebot3_world.launch
fi

if [ $RESULT = 3 ] 
then
    roslaunch turtlebot3_gazebo turtlebot3_house.launch
fi