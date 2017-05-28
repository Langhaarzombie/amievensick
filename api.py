from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask import Response, request

from backend import service

app = Flask(__name__)
api = Api(app)

## Default stuff ##

@app.route('/', methods=['GET'])
def hello():
    return "Hello World"

## Symptom Actions ##

@app.route('/symptom', methods=['GET'])
def getAllSymptoms():
	out = service.getAllSymptoms()
	resp = Response(out, status=200, mimetype='application/json')
	return resp

@app.route('/symptom/<string:sym>', methods=['GET'])
def getSymptomByName(sym):
	out = service.getSymptomByName(sym)
	resp = Response(out, status=200, mimetype='application/json')
	return resp

@app.route('/symptom', methods=['POST'])
def createSymptom():
	income = request.get_json()
	out = service.createSymptom(income)
	return "Success! Info: " + str(out)

## Sickness Action ##

@app.route('/sickness', methods=['GET'])
def getAllSicknesses():
	out = service.getAllSicknesses()
	resp = Response(out, status=200, mimetype='application/json')
	return resp

@app.route('/sickness/<string:sick>', methods=['GET'])
def getSicknessByName(sick):
	out = service.getSicknessByName(sick)
	resp = Response(out, status=200, mimetype='application/json')
	return resp

@app.route('/symptom', methods=['POST'])
def createSickness():
	income = request.get_json(force=True)
	out = service.createSickness(income)
	return "Success! Info: " + str(out)

## Indicated Action ##

@app.route('/indicates/<string:sym>/<string:sick>', methods=['GET'])
def getIndicatesForNodes(sym, sick):
	out = service.getIndicatesForNodes(sym, sick)
	resp = Response(out, status=200, mimetype='application/json')
	return resp

@app.route('/indicates', methods=['POST'])
def createIndicates():
	income = request.get_json(force=True)
	out = service.createIndicates(income)
	resp = Response(out, status=200, mimetype='application/json')
	return "Success! Info: " + str(out)

## Combined Actions ##

@app.route('/sbs', methods=['POST'])
def getSicknessBySymptom():
	income = request.get_json(force=True)
	out = service.getSicknessBySymptoms(income)
	resp = Response(out, status=200, mimetype='application/json')
	return resp

if __name__ == '__main__':
    app.run(debug=True)