from flask import Flask
from flask_restful import Resource, Api
from flask import Response, request

from backend import service

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def hello():
    return "Hello World"

## Symptom Actions ##

@app.route('/symptom', methods=['GET'])
def getAllSymptoms():
	out = service.getAllSymptoms()
	resp = Response(out, status=200, mimetype='application/json')
	return resp

@app.route('/symptom/<sym>', methods=['GET'])
def getSymptomByName(sym):
	out = service.getSymptomByName(sym)
	resp = Response(out, status=200, mimetype='application/json')
	return resp

## Sickness Action ##

@app.route('/sickness', methods=['GET'])
def getAllSicknesses():
	out = service.getAllSicknesses()
	resp = Response(out, status=200, mimetype='application/json')
	return resp

@app.route('/sickness/<sick>', methods=['GET'])
def getSicknessByName(sick):
	out = service.getSicknessByName(sick)
	resp = Response(out, status=200, mimetype='application/json')
	return resp

## Combined Actions ##

@app.route('/sbs', methods=['POST'])
def getSicknessBySymptom():
	income = request.get_json()
	out = service.getSicknessBySymptoms(income)
	resp = Response(out, status=200, mimetype='application/json')
	return resp

if __name__ == '__main__':
    app.run(debug=True)