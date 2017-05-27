import json

class Sickness:
	def __init__(self, sick_id, name, requires_medication, prevalence, location):
		self.id = sick_id
		self.name = name
		self.requires_medication = requires_medication
		self.prevalence = prevalence
		self.location = location

	def jdefault(self):
		return self.__dict__

	# TODO delete JSON form domain tests