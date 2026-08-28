Instructions to get the simulation running:



In Terminal1:



source install/setup.bash


colcon build


ros2 launch mbot_sim turtlebot3_world.launch.py



In Terminal-2:



source install/setup.bash


ros2 run mbot_sim lidar_node



In Terminal-3:



source install/setup.bash


ros2 run mbot_sim controller_node
