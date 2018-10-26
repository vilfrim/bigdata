# Local development environment for Big data and Cloud computing courses' project
Local development environment implemented with Docker and Docker compose

## Running

Install Docker and run ```docker-compose up``` on project root. Run ```docker-compose down``` to stop the instances.

### database
MariaDb database for storing sensor readings. Database runs on localhost's port 3306

### raspberry_client 
Client for collecting data from RuuviTags on RaspberryPi

Requires:
```
sudo apt-get install python-dev python-psutil bluez-hcidump
pip install ruuvitag_sensor
```

### read_endpoint
REST-endpoint implemented with Python and Flask to read sensor readings from database. Endpoint can be found 
http://localhost:4000/measurement

Example response
```
[{
	"sensor_id": "living_room",
	"measurements": [{
			"humidity": 40.0,
			"pressure": 1030.26,
			"temperature": 20.56,
			"time": "2018-11-15 20:52:07"
		},
		{
			"humidity": 40.0,
			"pressure": 1030.36,
			"temperature": 20.52,
			"time": "2018-11-15 20:54:07"
		},
		{
			"humidity": 40.0,
			"pressure": 1030.42,
			"temperature": 20.49,
			"time": "2018-11-15 20:56:07"
		}
	]
}]
```
### web
Simple html page with ChartJs to visualize sensor readings from read_endpoint. Chart can found http://localhost:2000

### write_endpoint
REST-endpoint implemented with Python and Flask to write sensor readings into database.
Endpoint's address is http://localhost:8000/measurement

Example of POST body
```
{
	"measurement_time": "2018-11-15 20:52:07",
	"controller_id": "raspberrypi",
	"measurements": [{
			"pressure": 1030.54,
			"sensor_id": "bedroom",
			"temperature": 20.0,
			"humidity": 40.5
		},
		{
			"pressure": 1031.19,
			"sensor_id": "living_room",
			"temperature": 21.21,
			"humidity": 41.0
		}
	]
}
```

