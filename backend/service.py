from domain import symptom, sickness, indicates
from persistance import sicknessrepo, symptomrepo

def getAllSymptoms():
	result = symptomrepo.getAllSymptoms()
	string = ""
	for x in result:
		string = string + ", " + str(x)
	return string

def getAllSicknesses():
	result = sicknessrepo.getAllSicknesses()
	string = ""
	for x in result:
		string = string + ", " + str(x)
	return string

def getSymptomByName(name):
	result = symptomrepo.getSymptomByName(str(name))
	string = ""
	for x in result:
		string = str(x)
	return string

def getSicknessByName(name):
	result = sicknessrepo.getSicknessByName(str(name))
	string = ""
	for x in result:
		string = str(x)
	return string

def getSicknessBySymptoms():
	pass