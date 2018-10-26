import os
from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL
from itertools import groupby

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_DATABASE')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST')
mysql.init_app(app)

@app.route('/measurement')
@cross_origin()
def get_measurements():
    conn = mysql.connect()
    cursor = conn.cursor()
    try: 
        cursor.execute("SELECT sensor_id, measurement_time, temperature, humidity, pressure FROM measurement ORDER BY sensor_id, measurement_time")
        result_set = cursor.fetchall()
    except conn.Error as error:
        print("Error: {}".format(error))
        return jsonify({'error': "{}".format(error)}), 400
    
    payload = []
    for key, group in groupby(result_set, lambda x: x[0]):
        measurements = []
        for measurement in group:
            content = {'time': measurement[1].strftime('%Y-%m-%d %H:%M:%S'), 'temperature': measurement[2], 'humidity': measurement[3], 'pressure': measurement[4]}
            measurements.append(content)
        sensor = {'sensor_id': key, 'measurements': measurements}
        payload.append(sensor)
    return jsonify(payload)



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('APP_PORT'))
