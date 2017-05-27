from neo4chain import commands, dbmanager

def createSymptom(symptom):
	cmd = commands.Command().addNode("symptom", "s1").setProperty("name", symptom.name, "s1")
	
	# Debug
	print("Executing: ")
	cmd.printCommand()
	
	result = cmd.execute(dbmanager.conn.connection.getSession())

	# Debug
	print(result)

def saveSymptom(symptom): #setting the id is forbidden
	where = commands.WhereID(symptom.id, "s1")
	cmd = commands.Command().matchNode("smyptom", "s1", where).setProperty("name", symptom.name, "s1")

	# Debug
	print("Executing: ")
	cmd.printCommand()

	result = cmd.execute(dbmanager.conn.connection.getSession())

	# Debug
	print(result)

# TODO add method for deleting

def getSymptomById(id):
	where = commands.WhereID(symptom.id, "s1")
	cmd = commands.Command().findNode("symptom", "s1", where)

	# Debug
	print("Executing: ")
	cmd.printCommand()

	result = cmd.execute(dbmanager.conn.connection.getSession())

	# Debug
	print(result)

	return result

def getSymptomByName(name):
	where = commands.Where().addFilter("name", name)
	cmd = commands.Command().findNode("symptom", "s1", where)

	# Debug
	print("Executing: ")
	cmd.printCommand()

	result = cmd.execute(dbmanager.conn.connection.getSession())

	# Debug
	print(result)

	return result

def getSymptomsForSickness(sickness):
	#find sickness
	whereS = commands.WhereID(sickness.id, "sick")
	cmd = commands.Command().matchNode("sickness", "sick", whereS).matchRelation("indicated", "symptom", "sickness", "rel", "sym", "sick").returnSingleValue("sym")

	# Debug
	print("Executing: ")
	cmd.printCommand()

	result = cmd.execute(dbmanager.conn.connection.getSession())

	# Debug
	print(result)

	return result

def getAllSymptoms():
	cmd = commands.Command().findNode("symptom")

	# Debug
	print("Executing: ")
	cmd.printCommand()

	result = cmd.execute(dbmanager.conn.connection.getSession())

	# Debug
	print(result)

	return result