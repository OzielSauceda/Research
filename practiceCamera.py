'''
import cv2
import numpy as np
import os  # Add this line for working with paths

output_folder = "staticOutput"

def process_image(image):
    array = np.frombuffer(image.raw_data, dtype=np.dtype("uint8"))
    array = np.reshape(array, (image.height, image.width, 4))
    rgb_data = array[:, :, :3]

    # Save the image to the specified folder
    image_path = os.path.join(output_folder, f"carla_rgb_image_{image.frame}.png")
    cv2.imwrite(image_path, cv2.cvtColor(rgb_data, cv2.COLOR_RGB2BGR))

# Rest of the code remains unchanged
def process_static_image():
    # Load a sample image (replace this with your own image)
    static_image = cv2.imread('C:/Users/jlz679/Desktop/Code/Research/cat.jpg')

    # Display the image (you can replace this with your processing logic)
    cv2.imshow("Static Image", static_image)
    cv2.waitKey(0)

    # Save the image to disk (optional)
    cv2.imwrite("static_image.png", static_image)

# Call the function to process a static image
process_static_image()

# Cleanup
cv2.destroyAllWindows()
'''

import cv2

# Specify the correct path to your video file
video_path = 'C:/Users/jlz679/Desktop/Code/Research/TestingFiles/NewTestDrive.mp4'
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print(f"Error: Could not open video file at '{video_path}'.")
    exit()

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to grab frame.")
            break

        cv2.imshow("Video Playback", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()



