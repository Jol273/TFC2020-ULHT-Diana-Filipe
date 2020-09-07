from CameraReceiver import CameraReceiver
import json

file = open('data.json')
stored_data = json.loads(file.read())
cameraIP = stored_data["cameraIP"]
file.close()

receiver = CameraReceiver([cameraIP])
