import json

class Indicates:
	def __init__(self, in_id, severity, symptom, sickness):
		self.id = in_id
		self.severity = severity
		self.symptom = symptom
		self.sickness = sickness

	def jdefault(self):
		return self.__dict__