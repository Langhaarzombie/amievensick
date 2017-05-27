import json

class Indicates:
	def __init__(self, in_id, severity, symptom, sickness):
		self.id = in_id
		self.severity = severity
		self.symptom = symptom
		self.sickness = sickness

	def toJSON(self):
		return json.dumps({"indicates": {"id": self.id, "severity": self.severity, "symptom": {"id": self.symptom.id, "name": self.symptom.name}, "sickness": {"id": self.sickness.id, "name": self.sickness.name, "requires_medication": self.sickness.requires_medication, "prevalence": self.sickness.prevalence, "location": self.sickness.location}}})