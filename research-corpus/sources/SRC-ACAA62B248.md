> Source: https://carla.readthedocs.io/en/latest/ref_sensors/

Sensors reference - CARLA Simulator
CARLA Simulator
Home
Getting started
Introduction
Quick start package installation
First steps
Building CARLA
Next steps
Content authoring - maps
Content authoring - vehicles
Content authoring - props
CARLA topics
Coordinates and transformations
Foundations
Actors
Maps
Sensors and data
Traffic
AI rendering
Development
Custom assets
Resources
Python API
Catalogue
C++ reference
Blueprint library
Tutorials
Extended documentation
Downloads
CARLA Ecosystem
ANSYS
AWS
CarSIM
Chrono
MathWorks
Inverted AI
NVIDIA
ASAM OpenDRIVE
PTV Vissim
RSS
ROS
Scenic
SUMO
SYNKROTRON
Contributing
Guidelines
Coding standards
Documentation standard
CARLA Simulator
Sensors reference
Edit on GitHub
You are currently reading documentation for the "dev" branch of CARLA. This documentation refers to features currently in development and may result in unexpected behaviour. To read documentation for previous releases, select the desired version in the bottom, right-hand corner of the screen.
Sensors reference
Collision detector
Depth camera
GNSS sensor
IMU sensor
Lane invasion detector
LIDAR sensor
Obstacle detector
Radar sensor
RGB camera
Wide-angle camera
RSS sensor
Semantic LIDAR sensor
Semantic segmentation camera
Instance segmentation camera
DVS camera
Optical Flow camera
V2X sensor
Cooperative awareness
Custom message
Important
All the sensors use the UE coordinate system ( x- forward, y- right, z- up), and return coordinates in local space. When using any visualization software, pay attention to its coordinate system. Many invert the Y-axis, so visualizing the sensor data directly may result in mirrored outputs.
Collision detector
Blueprint: sensor.other.collision
Output: carla.CollisionEvent per collision.
This sensor registers an event each time its parent actor collides against something in the world. Each collision sensor produces one collision event per collision per frame. Multiple collision events may be produced in a single frame by collisions with multiple other actors. To ensure that collisions with any kind of object are detected, the server creates "fake" actors for elements such as buildings or bushes so the semantic tag can be retrieved to identify it.
Collision detectors do not have any configurable attribute.
Output attributes
Depth camera
Blueprint: sensor.camera.depth
Output: carla.Image per step (unless sensor_tick says otherwise).
The camera provides a raw data of the scene codifying the distance of each pixel to the camera (also known as depth buffer or z-buffer) to create a depth map of the elements.
The image codifies depth value per pixel using 3 channels of the RGB color space, from less to more significant bytes: R -> G -> B. The actual distance in meters can be decoded with:
The output carla.Image should then be saved to disk using a carla.colorConverter that will turn the distance stored in RGB channels into a [0,1] float containing the distance and then translate this to grayscale. There are two options in carla.colorConverter to get a depth view: Depth and Logaritmic depth. The precision is milimetric in both, but the logarithmic approach provides better results for closer objects.
Basic camera attributes
Camera lens distortion attributes
Output attributes
GNSS sensor
Blueprint: sensor.other.gnss
Output: carla.GNSSMeasurement per step (unless sensor_tick says otherwise).
Reports current gnss position of its parent object. This is calculated by adding the metric position to an initial geo reference location defined within the OpenDRIVE map definition.
GNSS attributes
Output attributes
IMU sensor
Blueprint: sensor.other.imu
Output: carla.IMUMeasurement per step (unless sensor_tick says otherwise).
Provides measures that accelerometer, gyroscope and compass would retrieve for the parent object. The data is collected from the object's current state.
IMU attributes
Output attributes
Note
For the compass, North is 0 radians. East is pi/2 radians, South is pi radians, West is3pi **/2 radians. North is in the direction of decreasing Y in CARLA's global coordinate system. East is in the direction of increasing X. The compass value converted to degrees is equal to 90 - yaw.
Lane invasion detector
Blueprint: sensor.other.lane_invasion
Output: carla.LaneInvasionEvent per crossing.
Registers an event each time its parent crosses a lane marking. The sensor uses road data provided by the OpenDRIVE description of the map to determine whether the parent vehicle is invading another lane by considering the space between wheels. However there are some things to be taken into consideration:
Discrepancies between the OpenDRIVE file and the map will create irregularities such as crossing lanes that are not visible in the map.
The output retrieves a list of crossed lane markings: the computation is done in OpenDRIVE and considering the whole space between the four wheels as a whole. Thus, there may be more than one lane being crossed at the same time.
This sensor does not have any configurable attribute.
Important
This sensor works fully on the client-side.
Output attributes
LIDAR sensor
Blueprint: sensor.lidar.ray_cast
Output: carla.LidarMeasurement per step (unless sensor_tick says otherwise).
This sensor simulates a rotating LIDAR implemented using ray-casting. The points are computed by adding a laser for each channel distributed in the vertical FOV. The rotation is simulated computing the horizontal angle that the Lidar rotated in a frame. The point cloud is calculated by doing a ray-cast for each laser in every step. points_per_channel_each_step = points_per_second / (FPS * channels)
A LIDAR measurement contains a package with all the points generated during a 1/FPS interval. During this interval the physics are not updated so all the points in a measurement reflect the same "static picture" of the scene.
This output contains a cloud of simulation points and thus, it can be iterated to retrieve a list of their carla.Location :
The information of the LIDAR measurement is encoded 4D points. Being the first three, the space points in xyz coordinates and the last one intensity loss during the travel. This intensity is computed by the following formula.  a — Attenuation coefficient. This may depend on the sensor's wavelenght, and the conditions of the atmosphere. It can be modified with the LIDAR attribute atmosphere_attenuation_rate . d — Distance from the hit point to the sensor.
For a better realism, points in the cloud can be dropped off. This is an easy way to simulate loss due to external perturbations. This can done combining two different.
General drop-off — Proportion of points that are dropped off randomly. This is done before the tracing, meaning the points being dropped are not calculated, and therefore improves the performance. If dropoff_general_rate = 0.5 , half of the points will be dropped.
Instensity-based drop-off — For each point detected, and extra drop-off is performed with a probability based in the computed intensity. This probability is determined by two parameters. dropoff_zero_intensity is the probability of points with zero intensity to be dropped. dropoff_intensity_limit is a threshold intensity above which no points will be dropped. The probability of a point within the range to be dropped is a linear proportion based on these two parameters.
Additionally, the noise_stddev attribute makes for a noise model to simulate unexpected deviations that appear in real-life sensors. For positive values, each point is randomly perturbed along the vector of the laser ray. The result is a LIDAR sensor with perfect angular positioning, but noisy distance measurement.
The rotation of the LIDAR can be tuned to cover a specific angle on every simulation step (using a fixed time-step). For example, to rotate once per step (full circle output, as in the picture below), the rotation frequency and the simulated FPS should be equal.
1. Set the sensor's frequency sensors_bp['lidar'][0].set_attribute('rotation_frequency','10') .
2. Run the simulation using python3 config.py --fps=10 . 
Lidar attributes
Output attributes
Hybrid Solid State LiDAR sensor
Blueprint: sensor.lidar.hss_lidar
Output: carla.LidarMeasurement per step (unless sensor_tick says otherwise).
This sensor simulates a Hybrid Solid State LIDAR implemented using ray-casting. For the default parameters, the Hesai AT128 specifications were selected. The points are computed by adding a laser for each channel distributed in the vertical FOV. The point cloud is calculated by doing a ray-cast for each laser in every step.
The information of the LIDAR measurement is encoded 4D points. Being the first three, the space points in xyz coordinates and the last one intensity loss during the travel. This intensity is computed by the following formula.  a — Attenuation coefficient. This may depend on the sensor's wavelenght, and the conditions of the atmosphere. It can be modified with the LIDAR attribute atmosphere_attenuation_rate . d — Distance from the hit point to the sensor.
For a better realism, points in the cloud can be dropped off. This is an easy way to simulate loss due to external perturbations. This can done combining two different.
General drop-off — Proportion of points that are dropped off randomly. This is done before the tracing, meaning the points being dropped are not calculated, and therefore improves the performance. If dropoff_general_rate = 0.5 , half of the points will be dropped.
Instensity-based drop-off — For each point detected, and extra drop-off is performed with a probability based in the computed intensity. This probability is determined by two parameters. dropoff_zero_intensity is the probability of points with zero intensity to be dropped. dropoff_intensity_limit is a threshold intensity above which no points will be dropped. The probability of a point within the range to be dropped is a linear proportion based on these two parameters.
Additionally, the noise_stddev attribute makes for a noise model to simulate unexpected deviations that appear in real-life sensors. For positive values, each point is randomly perturbed along the vector of the laser ray. The result is a LIDAR sensor with perfect angular positioning, but noisy distance measurement.
The rotation of the LIDAR can be tuned to cover a specific angle on every simulation step (using a fixed time-step). For example, to rotate once per step (full circle output, as in the picture below), the rotation frequency and the simulated FPS should be equal.
1. Set the sensor's frequency sensors_bp['lidar'][0].set_attribute('rotation_frequency','10') .
2. Run the simulation using python3 config.py --fps=10 .
The LiDAR configured as AT128, AT360 and AT1440 shown in figure below: 
Lidar attributes
Output attributes
Obstacle detector
Blueprint: sensor.other.obstacle
Output: carla.ObstacleDetectionEvent per obstacle (unless sensor_tick says otherwise).
Registers an event every time the parent actor has an obstacle ahead. In order to anticipate obstacles, the sensor creates a capsular shape ahead of the parent vehicle and uses it to check for collisions. To ensure that collisions with any kind of object are detected, the server creates "fake" actors for elements such as buildings or bushes so the semantic tag can be retrieved to identify it.
Output attributes
Radar sensor
Blueprint: sensor.other.radar
Output: carla.RadarMeasurement per step (unless sensor_tick says otherwise).
The sensor creates a conic view that is translated to a 2D point map of the elements in sight and their speed regarding the sensor. This can be used to shape elements and evaluate their movement and direction. Due to the use of polar coordinates, the points will concentrate around the center of the view.
Points measured are contained in carla.RadarMeasurement as an array of carla.RadarDetection, which specifies their polar coordinates, distance and velocity. This raw data provided by the radar sensor can be easily converted to a format manageable by numpy:
The provided script manual_control.py uses this sensor to show the points being detected and paint them white when static, red when moving towards the object and blue when moving away: 
Output attributes
RGB camera
Blueprint: sensor.camera.rgb
Output: carla.Image per step (unless sensor_tick says otherwise)..
The "RGB" camera acts as a regular camera capturing images from the scene. carla.colorConverter
If enable_postprocess_effects is enabled, a set of post-process effects is applied to the image for the sake of realism:
Vignette: darkens the border of the screen.
Grain jitter: adds some noise to the render.
Bloom: intense lights burn the area around them.
Auto exposure: modifies the image gamma to simulate the eye adaptation to darker or brighter areas.
Lens flares: simulates the reflection of bright objects on the lens.
Depth of field: blurs objects near or very far away of the camera.
The sensor_tick tells how fast we want the sensor to capture the data. A value of 1.5 means that we want the sensor to capture data each second and a half. By default a value of 0.0 means as fast as possible. 
Basic camera attributes
Camera lens distortion attributes
Advanced camera attributes
Since these effects are provided by UE, please make sure to check their documentation:
Automatic Exposure
Cinematic Depth of Field Method
Color Grading and Filmic Tonemapper
Blueprint attribute
Type
Default
Description min_fstop
float
1.2
Maximum aperture. blade_count
int
5
Number of blades that make up the diaphragm mechanism. exposure_mode
str histogram
Can be manual or histogram . More in UE4 docs. exposure_compensation
float
Linux: +0.75
Windows: 0.0
Logarithmic adjustment for the exposure. 0: no adjustment, -1:2x darker, -2:4 darker, 1:2x brighter, 2:4x brighter. exposure_min_bright
float
10.0
In exposure_mode: "histogram" . Minimum brightness for auto exposure. The lowest the eye can adapt within. Must be greater than 0 and less than or equal to exposure_max_bright . exposure_max_bright
float
12.0
In exposure_mode: "histogram". Maximum brightness for auto exposure. The highestthe eye can adapt within. Must be greater than 0 and greater than or equal to exposure_min_bright. exposure_speed_up
float
3.0
In exposure_mode: "histogram" . Speed at which the adaptation occurs from dark to bright environment. exposure_speed_down
float
1.0
In exposure_mode: "histogram" . Speed at which the adaptation occurs from bright to dark environment. calibration_constant
float
16.0
Calibration constant for 18% albedo. focal_distance
float
1000.0
Distance at which the depth of field effect should be sharp. Measured in cm (UE units). blur_amount
float
1.0
Strength/intensity of motion blur. blur_radius
float
0.0
Radius in pixels at 1080p resolution to emulate atmospheric scattering according to distance from camera. motion_blur_intensity
float
0.45
Strength of motion blur [0,1]. motion_blur_max_distortion
float
0.35
Max distortion caused by motion blur. Percentage of screen width. motion_blur_min_object_screen_size
float
0.1
Percentage of screen width objects must have for motion blur, lower value means less draw calls. slope
float
0.88
Steepness of the S-curve for the tonemapper. Larger values make the slope steeper (darker) [0.0, 1.0]. toe
float
0.55
Adjusts dark color in the tonemapper [0.0, 1.0]. shoulder
float
0.26
Adjusts bright color in the tonemapper [0.0, 1.0]. black_clip
float
0.0
This should NOT be adjusted. Sets where the crossover happens and black tones start to cut off their value [0.0, 1.0]. white_clip
float
0.04
Set where the crossover happens and white tones start to cut off their value. Subtle change in most cases [0.0, 1.0]. temp
float
6500.0
White balance in relation to the temperature of the light in the scene. White light: when this matches light temperature. Warm light: When higher than the light in the scene, it is a yellowish color. Cool light: When lower than the light. Blueish color. tint
float
0.0
White balance temperature tint. Adjusts cyan and magenta color ranges. This should be used along with the white balance Temp property to get accurate colors. Under some light temperatures, the colors may appear to be more yellow or blue. This can be used to balance the resulting color to look more natural. chromatic_aberration_intensity
float
0.0
Scaling factor to control color shifting, more noticeable on the screen borders. chromatic_aberration_offset
float
0.0
Normalized distance to the center of the image where the effect takes place. enable_postprocess_effects
bool
True
Post-process effects activation.
Output attributes
Wide-angle cameras
Blueprint RGB: sensor.camera.rgb.wide_angle_lens
Blueprint depth: sensor.camera.depth.wide_angle_lens
Blueprint semantic segmentation: sensor.camera.semantic_segmentation.wide_angle_lens
Blueprint instance segmentation: sensor.camera.instance_segmentation.wide_angle_lens
Output: carla.Image per step (unless sensor_tick says otherwise)..
The wide-angle camera models multiple types of specialized cameras such as standard wide-angle, 360 degree cameras and fisheye lenses. The wide-angle camera model offers standard RGB output along with depth, semantic segmentation and instance segmentation. There are numerous projection models available, including perspective, stereographic, equidistant, equisolid, orthographic and Kannala-Brandt.
The Kannala-Brandt model used matches the implementation used in OpenCV.
Output attributes
RSS sensor
Blueprint: sensor.other.rss
Output: carla.RssResponse per step (unless sensor_tick says otherwise).
Important
It is highly recommended to read the specific rss documentation before reading this.
This sensor integrates the C++ Library for Responsibility Sensitive Safety in CARLA. It is disabled by default in CARLA, and it has to be explicitly built in order to be used.
The RSS sensor calculates the RSS state of a vehicle and retrieves the current RSS Response as sensor data. The carla.RssRestrictor will use this data to adapt a carla.VehicleControl before applying it to a vehicle.
These controllers can be generated by an Automated Driving stack or user input. For instance, hereunder there is a fragment of code from PythonAPI/examples/rss/manual_control_rss.py , where the user input is modified using RSS when necessary.
1. Checks if the RssSensor generates a valid response containing restrictions. 2. Gathers the current dynamics of the vehicle and the vehicle physics. 3. Applies restrictions to the vehicle control using the response from the RssSensor, and the current dynamics and physicis of the vehicle.
The carla.RssSensor class
The blueprint for this sensor has no modifiable attributes. However, the carla.RssSensor object that it instantiates has attributes and methods that are detailed in the Python API reference. Here is a summary of them.
Warning
This sensor works fully on the client side. There is no blueprint in the server. Changes on the attributes will have effect after the listen() has been called.
The methods available in this class are related to the routing of the vehicle. RSS calculations are always based on a route of the ego vehicle through the road network.
The sensor allows to control the considered route by providing some key points, which could be the carla.Transform in a carla.Waypoint. These points are best selected after the intersections to force the route to take the desired turn.
Note
If no routing targets are defined, a random route is created.
Output attributes
In case a actor_constellation_callback is registered, a call is triggered for:
default calculation ( actor_constellation_data.other_actor=None )
per-actor calculation
Semantic LIDAR sensor
Blueprint: sensor.lidar.ray_cast_semantic
Output: carla.SemanticLidarMeasurement per step (unless sensor_tick says otherwise).
This sensor simulates a rotating LIDAR implemented using ray-casting that exposes all the information about the raycast hit. Its behaviour is quite similar to the LIDAR sensor, but there are two main differences between them.
The raw data retrieved by the semantic LIDAR includes more data per point.
Coordinates of the point (as the normal LIDAR does).
The cosine between the angle of incidence and the normal of the surface hit.
Instance and semantic ground-truth. Basically the index of the CARLA object hit, and its semantic tag.
The semantic LIDAR does not include neither intensity, drop-off nor noise model attributes.
The points are computed by adding a laser for each channel distributed in the vertical FOV. The rotation is simulated computing the horizontal angle that the LIDAR rotated in a frame. The point cloud is calculated by doing a ray-cast for each laser in every step.
A LIDAR measurement contains a package with all the points generated during a 1/FPS interval. During this interval the physics are not updated so all the points in a measurement reflect the same "static picture" of the scene.
This output contains a cloud of lidar semantic detections and therefore, it can be iterated to retrieve a list of their carla.SemanticLidarDetection :
The rotation of the LIDAR can be tuned to cover a specific angle on every simulation step (using a fixed time-step). For example, to rotate once per step (full circle output, as in the picture below), the rotation frequency and the simulated FPS should be equal.
1. Set the sensor's frequency sensors_bp['lidar'][0].set_attribute('rotation_frequency','10') .
2. Run the simulation using python3 config.py --fps=10 . 
SemanticLidar attributes
Output attributes
Sensor data attribute
Type
Description frame
int
Frame number when the measurement took place. timestamp
double
Simulation time of the measurement in seconds since the beginning of the episode. transform
carla.Transform
Location and rotation in world coordinates of the sensor at the time of the measurement. horizontal_angle
float
Angle (radians) in the XY plane of the LIDAR in the current frame. channels
int
Number of channels (lasers) of the LIDAR. get_point_count(channel)
int
Number of points per channel captured in the current frame. raw_data
bytes
Array containing the point cloud with instance and semantic information. For each point, four 32-bits floats are stored.
XYZ coordinates.
cosine of the incident angle.
Unsigned int containing the index of the object hit.
Unsigned int containing the semantic tag of the object it.
Semantic segmentation camera
Blueprint: sensor.camera.semantic_segmentation
Output: carla.Image per step (unless sensor_tick says otherwise).
This camera classifies every object in sight by displaying it in a different color according to its tags (e.g., pedestrians in a different color than vehicles). When the simulation starts, every element in scene is created with a tag. So it happens when an actor is spawned. The objects are classified by their relative file path in the project. For example, meshes stored in Unreal/CarlaUE4/Content/Static/Pedestrians are tagged as Pedestrian . 
The server provides an image with the tag information encoded in the red channel: A pixel with a red value of x belongs to an object with tag x . This raw carla.Image can be stored and converted it with the help of CityScapesPalette in carla.ColorConverter to apply the tags information and show picture with the semantic segmentation.
The following tags are currently available (Note, tags changed from version 0.9.13 to 0.9.14):
Note
Read this tutorial to create new semantic tags.
Instance segmentation camera
Blueprint: sensor.camera.instance_segmentation
Output: carla.Image per step (unless sensor_tick says otherwise).
This camera classifies every object in the field of view both by class and also by instance ID. When the simulation starts, every element in scene is created with a tag. So it happens when an actor is spawned. The objects are classified by their relative file path in the project. For example, meshes stored in Unreal/CarlaUE4/Content/Static/Pedestrians are tagged as Pedestrian . 
The server provides an image with the tag information encoded in the red channel: A pixel with a red value of x belongs to an object with tag x . The green and blue values of the pixel define the object's unique ID. For example a pixel with an 8 bit RGB value of [10, 20, 55] is a vehicle (Semantic tag 10) with a unique instance ID 20-55 .
Basic camera attributes
Camera lens distortion attributes
Output attributes
DVS camera
Blueprint: sensor.camera.dvs
Output: carla.DVSEventArray per step (unless sensor_tick says otherwise).
A Dynamic Vision Sensor (DVS) or Event camera is a sensor that works radically differently from a conventional camera. Instead of capturing intensity images at a fixed rate, event cameras measure changes of intensity asynchronously, in the form of a stream of events, which encode per-pixel brightness changes. Event cameras possess distinct properties when compared to standard cameras. They have a very high dynamic range (140 dB versus 60 dB), no motion blur, and high temporal resolution (in the order of microseconds). Event cameras are thus sensors that can provide high-quality visual information even in challenging high-speed scenarios and high dynamic range environments, enabling new application domains for vision-based algorithms.
The DVS camera outputs a stream of events. An event e=(x,y,t,pol) is triggered at a pixel x , y at a timestamp t when the change in logarithmic intensity L reaches a predefined constant threshold C (typically between 15% and 30%). L(x,y,t) - L(x,y,t-\delta t) = pol C t-\delta t is the time when the last event at that pixel was triggered and pol is the polarity of the event according to the sign of the brightness change. The polarity is positive +1 when there is increment in brightness and negative -1 when a decrement in brightness occurs. The working principles depicted in the following figure. The standard camera outputs frames at a fixed rate, thus sending redundant information when no motion is present in the scene. In contrast, event cameras are data-driven sensors that respond to brightness changes with microsecond latency. At the plot, a positive (resp. negative) event (blue dot, resp. red dot) is generated whenever the (signed) brightness change exceeds the contrast threshold C for one dimension x over time t . Observe how the event rate grows when the signal changes rapidly. 
The current implementation of the DVS camera works in a uniform sampling manner between two consecutive synchronous frames. Therefore, in order to emulate the high temporal resolution (order of microseconds) of a real event camera, the sensor requires to execute at a high frequency (much higher frequency than a conventional camera). Effectively, the number of events increases the faster a CARLA car drives. Therefore, the sensor frequency should increase accordingly with the dynamics of the scene. The user should find a balance between time accuracy and computational cost.
The provided script manual_control.py uses the DVS camera in order to show how to configure the sensor, how to get the stream of events and how to depict such events in an image format, usually called event frame.
Note that due to the sampling method of the DVS camera, if there is no pixel difference between two consecutive synchronous frames the camera will not return an image. This will always occur in the first frame, as there is no previous frame to compare to and also in the event that there has been no movement between frames. 
DVS is a camera and therefore has all the attributes available in the RGB camera. Nevertheless, there are few attributes exclusive to the working principle of an Event camera.
DVS camera attributes
Optical Flow Camera
The Optical Flow camera captures the motion perceived from the point of view of the camera. Every pixel recorded by this sensor encodes the velocity of that point projected to the image plane. The velocity of a pixel is encoded in the range [-2,2]. To obtain the motion in pixel units, this information can be scaled with the image size to [-2 * image_size, 2 * image_size]. 
Optical Flow camera attributes
Optical Flow camera lens distortion attributes
Output attributes
V2X sensor
Vehicle-to-everything (V2X) communication is an important aspect for future applications of cooperative intelligent transportation systems. In real vehicles, this requires a dedicated onboard unit (OBU) in each vehicle, that is able to send and receive information over wireless channels. Depending on the region (Europe, China, USA), different physical technologies, protocols and application messaging formats are used.
CARLA currently supports simulation of a simple broadcast wireless channel and two application messages. Protocols for network access and forwarding are not supported yet. The two implemented messages are the Cooperative Awarness Message according to the European standard ETSI, and a custom message type, that can be used to transmit arbitrary string data (e.g. JSON). There are two distinct sensors for V2X communication, that can be used separately, one for each application message type.
Basically, the wireless channel incorporates the following calculation for both sensors:
To simulate V2X communication, at least two V2X sensors of the same type need to be spawned (at least one sender-receiver pair). Because the received power is calculated on the receiver-side V2X sensor, only the antenna gain that is specified on the receiver-side sensor is incorporated in this calculation. Transmission power and receiver sensitivity can be configured (see Blueprint attributes).
The loss calculation depends on - the visbility condition between sender and receiver: line of sight (no obstacles), non-line of sight obstructed by buildings, or non-line of sight obstructed by vehicles, and - the scenario: highway, rural, or urban environment
While the visibility is simulated within CARLA, the scenario can be configured by the user (see Blueprint attributes), as well as several other attributes of the wireless channel.
Sensor (sub)types
Cooperative Awareness Message
Blueprint: sensor.other.v2x
Output: carla.CAMData, triggered according to the ETSI CAM standard, unless configured otherwise
Triggering conditions according to ETSI standard: - Heading angle change > 4° - Position difference > 4 m - Speed change > 5 m/s - Time elapsed > CAM Generation time (configurable) - Low Frequency Container Time Elapsed > 500 ms
For the CAM V2X sensor, additional blueprint attributes apply:
Custom V2X Message
Blueprint: sensor.other.v2x_custom
Output: carla.CustomV2XData, triggered with next tick after a send() was called
Methods
send( self, callback) The function the user has to call every time to send a message. This function needs for an argument containing an object type carla.SensorData to work with.
Parameters:
data ( function) - The called function with one argument containing the sensor data.
The custom V2X message sensor works a little bit different than other sensors, because it has the send function in addition to the listen function, that needs to be called, before another sensor of this type will receive anything. The transmission of a custom message is only triggered, when send is called. Each message given to the send function is only transmitted once to all Custom V2X Message sensors currently spawned. Independent communcation channels can be created by the sensors 'channel_id' attribute. Only sensors having the same 'channel_id' are communicating with each other. This allows to create different sender/receiver groups within the system.
Example:
V2X sensors blueprint attributes
Built with MkDocs using a theme provided by Read the Docs. 
latest
Versions
latest
0.9.16
0.9.15
0.9.14
0.9.13
0.9.12
0.9.11
0.9.10
0.9.9
0.9.8
0.9.7
0.9.6
0.9.5
0.9.4
0.9.3
0.9.2
0.9.1
0.9.0
0.8.4
On Read the Docs
Project Home
Builds
Search
Addons documentation ― Hosted by Read the Docs
Filters
[x] subprojects:carla/latest Include subprojects
No recent searches
Enter to select
Up / Down to navigate
Esc to close
Search powered by