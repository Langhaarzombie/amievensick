import json

class Sickness:
	def __init__(self, sick_id, name, requires_medication, prevalence, location):
		self.id = sick_id
		self.name = name
		self.requires_medication = requires_medication
		self.prevalence = prevalence
		self.location = location

	def toJSON(self):
		return json.dumps({"sickness": {"id": self.id, "name": self.name, "requires_medication": self.requires_medication, "prevalence": self.prevalence, "location": self.location}})