# Installation
* http://wiki.ros.org/navigation
* sudo apt-get install ros-melodic-navigation

# Packages list
* amcl
* base_local_planner
* carrot_planner
* clear_costmap_recovery
* costmap_2d
* dwa_local_planner
* fake_localization
* global_planner
* map_server
* move_base
* move_base_msgs
* move_slow_and_clear
* nav_core
* navfn
* rotate_recovery
* Voxel_grid

# Basic Overview
* Navigation Stack takes in information from odometry and sensor streams and outputs velocity commands to send to a mobile base.
* Robot should have a tf transform tree in place, and publish sensor data using the correct ROS Message types.
* It is meant for both differential drive and holonomic wheeled robots only.
* It requires a planar laser mounted somewhere on the mobile base.
* 3 important part we need to know about are:
    * Setting up your robot using tf
    * Publishing Sensor Streams
    * Publishing Odometry Information

# Setting up robot using tf
* A proper tf tree needs to be set up while designing the robot.
* At an abstract level, a tf tree defines offsets in terms of both translation and rotation between different coordinate frames.
* Conventions used for naming frames:
* https://www.ros.org/reps/rep-0105.html
* Consider a robot with base (base_link) and laser scanner (base_scanner)
* Base_link is parent and laser is child here.
* tf assumes that all transforms move from parent to child.
* Tf tree gives translation and rotation from parent to child
* With this transform tree set up, converting the laser scan received in the "base_laser" frame to the "base_link" frame is as simple as making a call to the tf library.
* So, it helps to convert laser scan obtained at base_laser frame to map frame

# ‘amcl’ package
```
├── cfg
│   └── AMCL.cfg
├── CHANGELOG.rst
├── CMakeLists.txt
├── examples
│   ├── amcl_diff.launch
│   └── amcl_omni.launch
├── include
│   └── amcl
│       ├── map
│       │   └── map.h
│       ├── pf
│       │   ├── eig3.h
│       │   ├── pf.h
│       │   ├── pf_kdtree.h
│       │   ├── pf_pdf.h
│       │   └── pf_vector.h
│       └── sensors
│           ├── amcl_laser.h
│           ├── amcl_odom.h
│           └── amcl_sensor.h
├── package.xml
├── src
│   ├── amcl
│   │   ├── map
│   │   │   ├── map.c
│   │   │   ├── map_cspace.cpp
│   │   │   ├── map_draw.c
│   │   │   ├── map_range.c
│   │   │   └── map_store.c
│   │   ├── pf
│   │   │   ├── eig3.c
│   │   │   ├── pf.c
│   │   │   ├── pf_draw.c
│   │   │   ├── pf_kdtree.c
│   │   │   ├── pf_pdf.c
│   │   │   └── pf_vector.c
│   │   └── sensors
│   │       ├── amcl_laser.cpp
│   │       ├── amcl_odom.cpp
│   │       └── amcl_sensor.cpp
│   ├── amcl_node.cpp
│   └── include
│       └── portable_utils.hpp
└── test
    ├── basic_localization.py
    ├── basic_localization_stage.xml
    ├── global_localization_stage.xml
    ├── rosie_multilaser.xml
    ├── set_initial_pose_delayed.xml
    ├── set_initial_pose.xml
    ├── set_pose.py
    ├── small_loop_crazy_driving_prg_corrected.xml
    ├── small_loop_crazy_driving_prg.xml
    ├── small_loop_prf.xml
    ├── texas_greenroom_loop_corrected.xml
    ├── texas_greenroom_loop.xml
    ├── texas_willow_hallway_loop_corrected.xml
    └── texas_willow_hallway_loop.xml
```