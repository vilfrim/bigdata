import json
import datetime
import requests
from ruuvitag_sensor.ruuvi import RuuviTagSensor, RunFlag

class RuuvitagMeasurementCollector:
   # List of macs of sensors which will execute callback function
   # D1:BC:BE:67:B0:F7 : living_room
   # EE:8E:66:FC:A4:72 : kitchen
    macs = ['D1:BC:BE:67:B0:F7','EE:8E:66:FC:A4:72']
    timeout_in_sec = 4
    mac_identities = {'EE:8E:66:FC:A4:72': "kitchen", 'D1:BC:BE:67:B0:F7': "living_room"}
    
    def send_to_endpoint(self, payload):
        headers = {'Content-Type': 'application/json'}
        r = requests.post('http://192.168.1.152:8000/measurement', data=json.dumps(payload), headers=headers)
        print(r.status_code, r.reason)
        
    def measurement_to_structure(self, beacon_mac, data):
        measurement = {
            "sensor_id": self.mac_identities[beacon_mac],
            "pressure": data['pressure'],
            "temperature": data['temperature'],
            "humidity": data['humidity']
        }
        return measurement


    def handle_data(self, found_data):
        m = []
        for beacon in found_data:
            m.append(self.measurement_to_structure(beacon, found_data[beacon]))
        payload = {
            'controller_id': "raspberrypi",
            'measurement_time':""+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'measurements': m
        }
        print("Sending data endpoint", json.dumps(payload))
        self.send_to_endpoint(payload)

    def start_collection(self):

       print "starting to collect data"
       collected_data = RuuviTagSensor.get_data_for_sensors(self.macs, self.timeout_in_sec)
       self.handle_data(collected_data)


if __name__ == "__main__":
    collector = RuuvitagMeasurementCollector()
    collector.start_collection()