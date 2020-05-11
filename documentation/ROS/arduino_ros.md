# Installation

* See: [rosserial_arduino](http://wiki.ros.org/rosserial_arduino)
* Tutorial in : [rosserial arfuino Tutorials](http://wiki.ros.org/rosserial_arduino/Tutorials)
* Two main steps:
    1. Install rosserial in computer
    2. Add roslib library for Arduino

## Install 'rossserial'

    sudo apt-get install ros-melodic-rosserial-arduino
    sudo apt-get install ros-melodic-rosserial

## Add 'ros_lib' library to Arduino IDE

* First go to Libraries folder of Arduino. For me, it was:
        
        ~/snap/arduino/7/Arduino/libraries

* Remove any existing **ros_lib** library
  
        rm -rf ros_lib

* Install **ros_lib** library
  
        rosrun rosserial_arduino make_libraries.py .

# Examples

## Publish 'Hello World' by Arduino

* [Tutorial](http://wiki.ros.org/rosserial_arduino/Tutorials/Hello%20World)

Follow steps:

1. Upload Example Hello World sketch (of ros_lib) to arduino
2. roscore
3. Run rosserial

        rosrun rosserial_python serial_node.py /dev/ttyACM0
    
* That was all.
* Now you can see new node named **/serial_node**
* And new topic **/chatter**
* Echo the chatter topic to see the message 'Hello World'
* The codes of Arduino for ros is similar to ROS code C++ version.
* So, better to learn C++ version of ROS codes to understand arduino easily.
  

  




