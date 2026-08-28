from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'mbot_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),

        # Launch files
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')
        ),

        # World files
        (
            os.path.join('share', package_name, 'worlds'),
            glob('worlds/*')
        ),

        # Robot models
        (
            os.path.join('share', package_name, 'models', 'turtlebot3_burger'),
            glob('models/turtlebot3_burger/*')
        ),

        # URDF files
        (
            os.path.join('share', package_name, 'urdf'),
            glob('urdf/*')
        ),

        # Bridge configuration
        (
            os.path.join('share', package_name, 'params'),
            glob('params/*')
        ),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='adithi',
    maintainer_email='234905714+adithichoco1@users.noreply.github.com',
    description='ROS 2 simulation and autonomous navigation project for a TurtleBot3 Burger.',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'controller_node = mbot_sim.controller1:main',
            'lidar_node = mbot_sim.lidar1:main',
            'odom_node = mbot_sim.odom:main',
        ],
    },
)