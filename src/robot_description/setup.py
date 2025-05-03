from setuptools import find_packages, setup
import os
from glob import glob as glob
package_name = 'robot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/models', glob('models/*.sdf')),
        ('share/' + package_name + '/models/rob_arm', glob('models/rob_arm/*.*')),
        ('share/' + package_name + '/models/puzzlebot/meshes', glob('models/puzzlebot/meshes/*.*')),
        ('share/' + package_name + '/models/puzzlebot/meshes', glob('models/puzzlebot/meshes/collision/*')),
        ('share/' + package_name + '/models/puzzlebot/meshes', glob('models/puzzlebot/meshes/visual/*')),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='brad',
    maintainer_email='hilarioruben09@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
