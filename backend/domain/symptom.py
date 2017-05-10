import json

class Symptom:
	def __init__(self, sym_id, name):
		self.id = sym_id
		self.name = name

	def toJSON(self):
		return json.dumps({"symptom": {"id": self.id, "name": self.name}})
