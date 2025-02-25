from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'sza_h3q_turtlesim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[ 
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='A ROS 2 csomag, amely a Turtlesim segítségével háromszöget rajzol.',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'draw = sza_h3q_turtlesim.draw:main',  # a draw.py node indítása
        ],
    },
)


# from setuptools import find_packages, setup
# from glob import glob
# import os

# package_name = 'sza_h3q_turtlesim'

# setup(
#     name=package_name,
#     version='0.0.0',
#     packages=find_packages(exclude=['test']),
#     data_files=[
#         ('share/ament_index/resource_index/packages',
#             ['resource/' + package_name]),
#         ('share/' + package_name, ['package.xml']),
#         (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
#     ],
#     install_requires=['setuptools'],
#     zip_safe=True,
#     maintainer='todo',
#     maintainer_email='todo@todo.com',
#     description='TODO: Package description',
#     license='GNU General Public License v3.0',
#     tests_require=['pytest'],
#     entry_points={
#         'console_scripts': [
#             'draw = sza_h3q_turtlesim.draw:main',
#             # 'control_vehicle = sza_h3q_turtlesim.control_vehicle:main',
#         ],
#     },
# )
