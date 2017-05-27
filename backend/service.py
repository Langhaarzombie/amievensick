from domain import symptom, sickness, indicates
from persistance import sicknessrepo, symptomrepo
import convert

def getAllSymptoms():
	result = symptomrepo.getAllSymptoms()
	return convert.symptomBoltToJSON(result)

def getAllSicknesses():
	result = sicknessrepo.getAllSicknesses()
	return convert.sicknessBoltToJSON(result)

def getSymptomByName(name):
	result = symptomrepo.getSymptomByName(str(name))
	return convert.symptomBoltToJSON(result)

def getSicknessByName(name):
	result = sicknessrepo.getSicknessByName(str(name))
	return convert.sicknessBoltToJSON(result)

def getSicknessBySymptoms():
	pass