from domain import symptom, sickness, indicates
from persistance import sicknessrepo, symptomrepo
import convert

## Symptom Actions ##

def getAllSymptoms():
	result = symptomrepo.getAllSymptoms()
	return convert.symptomBoltToJSON(result)

def getSymptomByName(name):
	result = symptomrepo.getSymptomByName(str(name))
	return convert.symptomBoltToJSON(result)

def createSymptom(json):
	name = json.get("symptom").get("name")
	result = symptomrepo.createSymptom(symptom.Symptom(0, str(name))) # Id does not matter at this point
	return result

## Sickness Actions ##

def getAllSicknesses():
	result = sicknessrepo.getAllSicknesses()
	return convert.sicknessBoltToJSON(result)

def getSicknessByName(name):
	result = sicknessrepo.getSicknessByName(str(name))
	return convert.sicknessBoltToJSON(result)

def createSickness(json):
	name 					= json.get("sickness").get("name")
	requires_medication 	= json.get("sickness").get("requires_medication")
	prevalence 				= json.get("sickness").get("prevalence")
	location 				= json.get("sickness").get("location")
	result = sicknessrepo.createSickness(sickness.Sickness(0, str(name), str(requires_medication), str(prevalence), str(location))) # Id does not matter at this point
	return result

## Combined Actions ##

def getSicknessBySymptoms(json):

	symptoms = []
	for s in json.get("symptoms"):
		symptoms.append(symptom.Symptom(0, str(s.get("name")))) # id does not matter at this point

	result = sicknessrepo.getSicknessBySymptoms(symptoms)

	return convert.sicknessBoltToJSON(result)