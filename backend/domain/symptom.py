import json

class Symptom:
	def __init__(self, name):
		self.name = name

	def toJSON(self):
		return json.dumps({"symptom": {"name": self.name}})
