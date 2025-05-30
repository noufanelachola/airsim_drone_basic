import airsim
import time

# Connect to the AirSim simulator
client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)

print("Taking off...")
client.takeoffAsync().join()

time.sleep(3)
client.moveByVelocityAsync(6, 0, 2, 3).join()

time.sleep(3)

print("Landing..." + str(client.getMultirotorState()))
client.landAsync().join()
client.armDisarm(False)
client.enableApiControl(False)

print("Done.")
