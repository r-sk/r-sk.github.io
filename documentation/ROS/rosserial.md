# Introduction

* See: [rosserial](http://wiki.ros.org/rosserial)
* Helps for the communication between ROS nodes in various devices via **serial port** or **network socket**.
* Devices(nodes) running rosserial code require a node on the host machine to bridge the connection from the serial protocol to the more general ROS network.
* This node in host can be run using following packages:
  * rosserial_python (python based)
  * rosserial_server (C++ based)
* Various client libraries are available for easy communication with client ros nodes. Some of these client libraries are:
  * rosserial_arduino (for arduino, esp32, esp8266)
  * rosserial_windows (for windows applications)
  * rosserial_stm32 (for stm32)
  * etc...
* Installation

        sudo apt-get install ros-melodic-rosserial

# Communication via serial port

* Run following in host computer:

        rosrun rosserial_python serial_node.py /dev/ttyACM0

* Replace the above port name with the target port you need.

# Communication via network socket

* Run following in host computer:

        rosrun rosserial_python serial_node.py tcp

* Output:

        [INFO] [1589114115.055138]: ROS Serial Python Node
        Fork_server is:  False
        [INFO] [1589114115.076898]: Waiting for socket connections on port 11411
        waiting for socket connection

https://github.com/agnunez/espros

