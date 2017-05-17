from neo4chain import commands, dbmanager

def createSymptom(symptom):
	cmd = commands.Command().addNode("symptom", "s1").setProperty("name", symptom.name, "s1")
	
	# Debug
	print(Executing: )
	cmd.printCommand()
	
	result = cmd.execute(dbmanager.Connection().getSession())

	# Debug
	print(result)

def saveSymptom(symptom):
	pass

def deleteSymptom(symptom):
	pass

def getSymptom(id):
	pass

def getSymptomsForSickness(sickness):
	pass