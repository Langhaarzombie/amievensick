from flask import Flask
from flask_restful import Resource, Api
from flask import Response, request

from backend import service

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return "Hello World"

class Symptom(Resource):
	def get(self, sym):
		out = service.getSymptomByName(sym)
		resp = Response(out, status=200, mimetype='application/json')
		return resp

class SymptomList(Resource):
	def get(self):
		out = service.getAllSymptoms()
		resp = Response(out, status=200, mimetype='application/json')
		return resp

class Sickness(Resource):
	def get(self, sick):
		out = service.getSicknessByName(sick)
		resp = Response(out, status=200, mimetype='application/json')
		return resp

class SicknessList(Resource):
	def get(self):
		out = service.getAllSicknesses()
		resp = Response(out, status=200, mimetype='application/json')
		return resp

@app.route('/sbs', methods=['GET'])
def getSicknessBySymptom():
	income = request.get_json()
	out = service.getSicknessBySymptoms(income)
	resp = Response(out, status=200, mimetype='application/json')
	return resp

api.add_resource(HelloWorld, '/')

api.add_resource(SymptomList, '/symptom')
api.add_resource(Symptom, '/symptom/<sym>')

api.add_resource(SicknessList, '/sickness')
api.add_resource(Sickness, '/sickness/<sick>')

#api.add_resource(SicknessBySymptoms, "/sbs", endpoint = "sicknessbysymptoms")

if __name__ == '__main__':
    app.run(debug=True)