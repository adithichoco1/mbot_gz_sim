from setuptools import find_packages, setup

package_name = 'mbot_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='adithi',
    maintainer_email='adithi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
entry_points={
    'console_scripts': [
        'controller_node = mbot_sim.controller1:main',
        'lidar_node = mbot_sim.lidar1:main',
        'odom_node = mbot_sim.odom:main'
    ],
}
)
