from flask import Flask, request, Response, render_template
import json
from flask_cors import CORS, cross_origin # pip install flask-cors

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

measurements = []

@cross_origin
@app.route('/api/diagramdata')
def showdiagramdata():
    diagramdata = {}
    diagramdata["minus4"] = 0
    diagramdata["minus4minus2"] = 0
    diagramdata["minus2plus2"] = 0
    diagramdata["plus2plus4"] = 0
    diagramdata["plus4"] = 0

    # käydään lämpötilamittaukset läpi
    for mittausolio in measurements:
        temperature = mittausolio["temperature"]
        if temperature < -4:
            diagramdata["minus4"] += 1



@cross_origin
@app.route('/api/measurements')
def showmeas():
    # muutetaan lista sanakirjoja listaksi listoja
    isolista = []
    for mittausolio in measurements:
        # tehdään uusi lista
        row = []
        # lisätään listaan tiedot
        row.append(mittausolio["time"])
        row.append(mittausolio["pressure"])
        row.append(mittausolio["temperature"])
        row.append(mittausolio["humidity"])
        isolista.append(row)
        
    #sarjallistetaan
    s = json.dumps(isolista, indent=True)
    resp = Response(s, status=200, mimetype='application/json')
    return(resp)

# Lisää POST:n käsittely (katso mallia PowerPointista)
# Tee sitten simulaattori ThingsPeak-simulaattorin mallin mukaan
@app.route('/api/measurements', methods = ['POST'])
def newmeas():
    # poimitaan mittaus HTTP POST -viestistä
    print("newmeas POST")
    meas = request.get_json()
    # lisätään mittaus listaan
    measurements.append(meas)
    # palautetaan mittaus
    meas_json = json.dumps(meas)
    return meas_json

@app.route('/')
def showpage():
    return render_template('measurements.html')

@app.route('/diagram')
def showdiagram():
    return render_template('diagram.html')    

if __name__ == '__main__':
    app.run(debug=True)