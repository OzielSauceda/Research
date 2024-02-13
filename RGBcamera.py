import carla
import cv2
import numpy as np

def process_image(image):
    # Convert the raw image data to a NumPy array
    array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
    array = np.reshape(array, (image.height, image.width, 4))

    # Extract RGB data and ignore the alpha channel
    rgb_data = array[:, :, :3]

    # Display the image (you can replace this with your processing logic)
    cv2.imshow("Carla RGB Camera", rgb_data)
    cv2.waitKey(1)

    # Save the image to disk (optional)
    cv2.imwrite("carla_rgb_image.png", cv2.cvtColor(rgb_data, cv2.COLOR_RGB2BGR))

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
camera_bp.set_attribute('fps', '10')  # Set the frame rate to 10 fps
camera_transform = carla.Transform(carla.Location(x=1.5, z=2.4))
camera = world.spawn_actor(camera_bp, camera_transform, attach_to=vehicle)

# Set up a callback function to process the image data
camera.listen(process_image)

# Run the simulation for a certain amount of time (you can adjust this as needed)
world.tick()

# Cleanup
camera.destroy()
vehicle.destroy()
cv2.destroyAllWindows()
