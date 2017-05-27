import json

class Symptom:
	def __init__(self, sym_id, name):
		self.id = sym_id
		self.name = name

	def jdefault(self):
		return self.__dict__
