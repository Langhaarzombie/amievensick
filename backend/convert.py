from domain import symptom, sickness
import json

def symptomBoltToDomain(bolt):
	symptoms = []

	for x in bolt.records():
		for y in x.values():
			symptoms.append(symptom.Symptom(y.id, y.get("name")))

	return symptoms


def sicknessBoltToDomain(bolt):
	sicknesses = []

	for x in bolt.records():
		for y in x.values():
			sicknesses.append(sickness.Sickness(y.id, y.get("name"), y.get("requires_medication"), y.get("prevalence"), y.get("location")))

	return sicknesses

def symptomBoltToJSON(bolt):
	result = symptomBoltToDomain(bolt)

	data = []
	for x in result:
		data.append(x.__dict__)

	return json.dumps(data)

def sicknessBoltToJSON(bolt):
	result = sicknessBoltToDomain(bolt)

	data = []
	for x in result:
		data.append(x.__dict__)

	return json.dumps(data)
