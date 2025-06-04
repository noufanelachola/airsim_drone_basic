import airsim
import time
import numpy as np
import cv2 as cv

# Connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
# client.reset()
client.armDisarm(True)

print("Taking off...")
client.takeoffAsync().join()

client.hoverAsync().join()
time.sleep(10)

response = client.simGetImages(
    [airsim.ImageRequest("0", airsim.ImageType.Scene, False, False)])[0]

img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8)
img_rgb = img1d.reshape(response.height, response.width, 3)

# time.sleep(3)
# client.moveByVelocityAsync(6, 0, 2, 3).join()

# time.sleep(3)

# print("Landing..." + str(client.getMultirotorState()))
client.landAsync().join()


client.armDisarm(False)
client.enableApiControl(False)

cv.imshow("Image", img_rgb)
cv.waitKey(0)
cv.destroyAllWindows()

print("Done.")
