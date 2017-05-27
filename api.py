from flask import Flask
from flask_restful import Resource, Api

from backend import service

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return "Hello World"

class SymptomRouter(Resource):
	def get(self, sym):
		return service.getSymptomByName(sym)

api.add_resource(HelloWorld, '/')
api.add_resource(SymptomRouter, '/<sym>')


if __name__ == '__main__':
    app.run(debug=True)