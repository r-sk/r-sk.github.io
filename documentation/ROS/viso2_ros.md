# 'viso2_ros' package

* See: [viso2](http://wiki.ros.org/viso2_ros)
* Function: Estimate camera motion based on incoming rectified images from calibrated cameras
* Has 3 nodes:
    * mono_odometer
    * mono_odometer_omnidirectional
    * stereo_odometer 
* To estimate the scale of the motion, the mono odometer uses the ground plane and therefore needs information about the camera's z-coordinate and its pitch.
* Stereo odometer just needs stereo images.
* Tf tree structure needed:  
        world → odom → base_link → camera

> Well Looks like VISO2 don't use base_footprint as its root link  
> VISO2 is preety old and back then, base_link was used as root link  
> So just omit base_footprint link in the URDF file

* This package publishes:  
        odom → base_link
* For this to work, it needs to know:  
        base_link → camera
* If not published, it assumes it as the identity matrix which means the robot frame and the camera frame are identical

> The coordinate frame of the camera is expected to be the optical frame (like in monitor).  
> i.e x is pointing right, y downwards and z from the camera into the scene.



# Extras

* Uses **dense** stereo point clouds coming from stereo_image_proc
* using in Empty env wonk work hola ni aba

