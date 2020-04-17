# image_pipeline

* http://wiki.ros.org/image_pipeline
* It fills the gap between getting raw images from a camera driver and higher-level vision processing.
* It has collection of packages which includes:
    * camera_calibration
    * depth_image_proc
    * image_proc
    * image_publisher
    * image_rotate
    * image_view
    * stereo_image_proc

# Generic camera node

* In ROS, camera is also defined as a node which gives the raw images.
* Generic camera node is defined by following parameters:

## Published Topics
* image_raw (sensor_msgs/Image)  
    The unprocessed image data.
* camera_info (sensor_msgs/CameraInfo)  
    Contains the camera calibration (if calibrated) and extra data about the camera configuration.

## Services
* set_camera_info (sensor_msgs/SetCameraInfo)  
        Used by camera_calibration to save the calibration parameters.

## Moreover
* 'stereo_image_proc' has runtime-configurable stereo processing parameters of its own
* rqt_reconfigure is useful for tweaking configuration to get best results

# 'camera_calibration' package


# 'image_proc' package

* http://wiki.ros.org/image_proc
* The raw image can be piped through the image_proc to remove camera distortion.
* If necessary, will convert Bayer or YUV422 format image data to color image.

```
$ ROS_NAMESPACE=my_camera rosrun image_proc image_proc
```

<img src="image_proc.png">