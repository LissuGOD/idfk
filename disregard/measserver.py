import json
from flask import Flask, render_template, request, Response
from flask_cors import CORS, cross_origin # pip install flask-cors
app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# TODO: tee lista mittauksia varten
measurements = []

@cross_origin()
@app.route('/api/meas')
def get_all_measurements():
    return(json.dumps(measurements))

# TODO: avaa sivun result.html ja näyttää mittaukset siinä
@app.route('/')
def get_all_measurements_page():
    return render_template("result.html", result = json.dumps(measurements))

# TODO: ota vastaan HTTP POSTilla lähetty mittaus ja laita se taulukkoon
@app.route('/newmeasurement/', methods = ['POST'])
def new_measurement():
    meas = request.get_json(force=True)
    row = [meas['id'], meas['pressure'], meas['temperature'], meas['humidity']]
    measurements.append(row)
    print(measurements)
    return Response(status=200)

if __name__ == '__main__':
   app.run(debug = True)
   