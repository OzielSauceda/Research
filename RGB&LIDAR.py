# This code is just creating two different sensors and cameras that arent functioning as one, but instead 2 sepereate ones. 
# In order to have them function as one, we need to plan a fusion algorithm that allows them to know the highs and lows of
# each one, so that they can function well with each other.
import carla
import cv2
import numpy as np

def process_rgb_image(image):
    # Process RGB image data (replace this with your processing logic)
    rgb_data = np.frombuffer(image.raw_data, dtype=np.uint8).reshape((image.height, image.width, 4))[:, :, :3]
    # Perform RGB-specific processing

def process_lidar_data(lidar_data):
    # Process lidar data (replace this with your processing logic)
    lidar_points = np.frombuffer(lidar_data.raw_data, dtype=np.float32).reshape([-1, 4])
    # Perform lidar-specific processing

# Connect to the Carla server
client = carla.Client('localhost', 2000)
client.set_timeout(2.0)

# Get the world and its blueprint library
world = client.get_world()
blueprint_library = world.get_blueprint_library()

# Spawn a vehicle
vehicle_bp = blueprint_library.filter('vehicle.*')[0]
spawn_point = world.get_map().get_spawn_points()[0]
vehicle = world.spawn_actor(vehicle_bp, spawn_point)

# Add an RGB camera sensor to the vehicle
camera_bp = blueprint_library.find('sensor.camera.rgb')
camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
camera = world.spawn_actor(camera_bp, camera_transform, attach_to=vehicle)
camera.listen(process_rgb_image)

# Add a lidar sensor to the vehicle
lidar_bp = blueprint_library.find('sensor.lidar.ray_cast')
lidar_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
lidar = world.spawn_actor(lidar_bp, lidar_transform, attach_to=vehicle)
lidar.listen(process_lidar_data)

# Run the simulation for a certain amount of time
world.tick()

# Cleanup
camera.destroy()
lidar.destroy()
vehicle.destroy()
