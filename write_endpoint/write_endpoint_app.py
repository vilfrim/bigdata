import os
from flask import Flask, jsonify, request, abort
from flaskext.mysql import MySQL

app = Flask(__name__)

measurements = []

mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.getenv('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.getenv('DB_DATABASE')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('DB_HOST')
mysql.init_app(app)
mysql.init_app(app)

@app.route('/measurement', methods=['POST'])
def save_measurements():
    if not request.json:
        abort(400)
    conn = mysql.connect()
    cursor = conn.cursor()
    request_data = request.get_json()
    measurement_data = request_data['measurements']
    try:
        for m in measurement_data:
            cursor.execute("INSERT INTO measurement (controller_id, measurement_time, sensor_id, temperature, humidity, pressure) VALUES(%s, %s, %s, %s, %s, %s)", (request_data['controller_id'], request_data['measurement_time'], m['sensor_id'], m['temperature'], m['humidity'], m['pressure']))
            conn.commit()
    except conn.Error as error:
        print("Error: {}".format(error))
        return jsonify({'error': "{}".format(error)}), 400
    finally:
        cursor.close()
        conn.close()
    
    return jsonify({}), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.getenv('APP_PORT'))
