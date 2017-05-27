from flask import Flask
from flask_restful import Resource, Api

from backend import service

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return "Hello World"

class Symptom(Resource):
	def get(self, sym):
		return service.getSymptomByName(sym)

class SymptomList(Resource):
	def get(self):
		return service.getAllSymptoms()

class Sickness(Resource):
	def get(self, sick):
		return service.getSicknessByName(sick)

class SicknessList(Resource):
	def get(self):
		return service.getAllSicknesses()

api.add_resource(HelloWorld, '/')

api.add_resource(SymptomList, '/symptom')
api.add_resource(Symptom, '/symptom/<sym>')

api.add_resource(SicknessList, '/sickness')
api.add_resource(Sickness, '/sickness/<sick>')

if __name__ == '__main__':
    app.run(debug=True)