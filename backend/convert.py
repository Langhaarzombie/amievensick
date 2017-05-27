from domain import symptom, sickness

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

	string = "{["
	tmp = ""
	for x in result:
		string = string + tmp + x.toJSON()
		tmp = ","
	string = string + "]}"

	return json.dumps(string)

def sicknessBoltToJSON(bolt):
	result = sicknessBoltToDomain(bolt)

	string = "{["
	tmp = ""
	for x in result:
		string = string + tmp + x.toJSON()
		tmp = ","
	string = string + "]}"

	return json.dumps(string)
