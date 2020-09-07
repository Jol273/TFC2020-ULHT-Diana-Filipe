from CameraReceiver import CameraReceiver
import json

file = open('data.json')
stored_data = json.loads(file.read())
camera_ip = stored_data["camera_ip"]
file.close()

receiver = CameraReceiver([camera_ip])
