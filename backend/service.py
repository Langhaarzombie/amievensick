from domain import symptom, sickness, indicates
from persistance import sicknessrepo, symptomrepo, indicatesrepo
import convert

import requests

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

	# Send update to elastic search
	elastic = updateElastic(name)

	return result, elastic

# Our elastic search only cares aout the names of the symptoms. But they need to be up to date
def updateElastic(name):
	url = 'https://3tqci0amyj:l2s1jag1tn@first-cluster-1485543977.eu-west-1.bonsaisearch.net/amisick/symptom'
	response = requests.post(url, json= {"name": name})
	return response

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

## Indicates Actions ##

def getIndicatesForNodes(sym, sick):
	sym1 = symptom.Symptom(0, str(sym)) # Id does not matter, name passed via url
	sick1 = sickness.Sickness(0, str(sick), None, None, None) # Id does not matter, name is the only thing that is checked

	result = indicatesrepo.getIndiForNodes(sym1, sick1)

	return convert.indicatesBoltToJSON(result)

def createIndicates(json):
	sym_name = json.get("indicates").get("from")
	sick_name = json.get("indicates").get("to")
	severity = json.get("indicates").get("severity")

	result = indicatesrepo.createIndicates(indicates.Indicates(0, str(severity), None, None), symptom.Symptom(0, str(sym_name)), sickness.Sickness(0, str(sick_name), None, None, None))

	return result

## Combined Actions ##

def getSicknessBySymptoms(json):

	symptoms = []
	for s in json.get("symptoms"):
		symptoms.append(symptom.Symptom(0, str(s.get("name")))) # id does not matter at this point

	result = sicknessrepo.getSicknessBySymptoms(symptoms)

	return convert.sicknessBoltToJSON(result)