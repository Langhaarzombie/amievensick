from neo4chain import commands, dbmanager

def createSickness(sickness):
	cmd = commands.Command().addNode("sickness", "s1")
	cmd = cmd.setProperty("name", sickness.name, "s1").setProperty("requires_mdeication", sickness.requires_medication, "s1").setProperty("prevalence", sickness.prevalence, "s1").setProperty("location", sickness.location, "s1")
	
	# Debug
	print("Executing: ")
	cmd.printCommand()
	
	result = cmd.execute(dbmanager.conn.connection.getSession())

	# Debug
	print(result)

def saveSickness(sickness):
	where = commands.WhereID(sickness.id, "s1")
	cmd = commands.Command().matchNode("sickness", "s1", where)
	cmd = cmd.setProperty("name", sickness.name, "s1").setProperty("requires_medication", sickness.requires_medication, "s1").setProperty("prevalence", sickness.prevalence, "s1").setProperty("location", sickness.location, "s1")

	# Debug
	print("Executing: ")
	cmd.printCommand()

	result = cmd.execute(dbmanager.conn.connection.getSession())

def getSicknessByName(name):
	where = commands.Where().addFilter("name", name)
	cmd = commands.Command().findNode("sickness", "s1", where)

	# Debug
	print("Executing: ")
	cmd.printCommand()

	result = cmd.execute(dbmanager.conn.connection.getSession())

	# Debug
	print(result)

	return result

def getSicknessBySymptoms(symptoms = []): # leave out paramter to get all sicknesses
	# Building match for symptoms
	cmd = commands.Command()
	cmd = cmd.matchNode("sickness", "sick")
	for x in xrange(0, len(symptoms)):
		where = commands.Where().addFilter("name", symptoms[x].name)
		cmd = cmd.matchNode("symptom", "sym"+x)
		cmd = cmd.matchRelation("indicated", "symptom", "sickness", "in"+x, "sym"+x, "sick")

	# Debug
	print("Executing: ")
	cmd.printCommand()

	result = cmd.execute(dbmanager.conn.connection.getSession())

	# Debug
	print(result)

	return result