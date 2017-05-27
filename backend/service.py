from domain import symptom, sickness, indicates
from persistance import sicknessrepo, symptomrepo

def getAllSymptoms():
	pass

def getAllSicknesses():
	pass

def getSicknessBySymptoms():
	pass

def getSymptomByName(name):
	result = symptomrepo.getSymptomByName(str(name))
	string = ""
	for x in result:
		string = string + " | " + str(x)
	return string

def getSicknessByName():
	pass