import airsim
import time
import numpy as np
import cv2 as cv

client = airsim.MultirotorClient()

client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

print("Taking off...")
client.takeoffAsync().join()

client.hoverAsync().join()
time.sleep(1)

response = client.simGetImages([
    airsim.ImageRequest("0", airsim.ImageType.Scene, False, False),
    airsim.ImageRequest("0", airsim.ImageType.DepthVis, True)
]
)

# img1d = np.fromstring(response[0].image_data_uint8, dtype=np.uint8)
img1d = np.frombuffer(response[0].image_data_uint8, dtype=np.uint8)
img_rgb = img1d.reshape(response[0].height, response[0].width, 3)

depth1d = np.array(response[1].image_data_float, dtype=np.float32)
depth_img = depth1d.reshape(response[1].height, response[1].width)

# print("Depth image height : ", response[1].height)
# print("Depth Raw Data : ", depth1d[0])

# time.sleep(3)
# client.moveByVelocityAsync(6, 0, 2, 3).join()

# time.sleep(3)

# print("Landing..." + str(client.getMultirotorState()))
client.landAsync().join()


client.armDisarm(False)
client.enableApiControl(False)

cv.imshow("Image", img_rgb)
cv.imshow("Depth image", depth_img)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite("images/output.png", img_rgb)
print("image saved")

print("Done.")
