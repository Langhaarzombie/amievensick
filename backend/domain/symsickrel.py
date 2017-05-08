import json

class SymSickRel: #a class to represent the realtion between a sickness and a symptom
	def __init__(self, frequency, location):
		self.frequency = frequency
		self.location = location

	def toJSON(self):
		return json.dumps({"symsickrel": {"frequency": self.frequency, "location": self.location}})