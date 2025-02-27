# `sza_h3q_turtlesim` package
ROS 2 python package.  [![Static Badge](https://img.shields.io/badge/ROS_2-Humble-34aec5)](https://docs.ros.org/en/humble/)
## Packages and build

It is assumed that the workspace is `~/ros2_ws/`.

### Clone the packages
``` r
cd ~/ros2_ws/src
```
``` r
git clone https://github.com/szabo-armin/sza_h3q_turtlesim
```

### Build ROS 2 packages
``` r
cd ~/ros2_ws
```
``` r
colcon build --packages-select sza_h3q_turtlesim --symlink-install
```

### Don't forget to source before ROS commands.

``` r
source ~/ros2_ws/install/setup.bash
```

``` r
ros2 launch sza_h3q_turtlesim launch_example1.launch.py
```
