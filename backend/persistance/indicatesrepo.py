from neo4chain import commands, dbmanager

def createIndicates(indi, sym, sick):
	whereSym = commands.Where().addFilter("name", sym.name)
	whereSick = commands.Where().addFilter("name", sick.name)
	cmd = commands.Command().matchNode("symptom", "sym", whereSym).matchNode("sickness", "sick", whereSick)
	cmd = cmd.addRelation("indicates", "sym", "sick", "indi").setProperty("severity", indi.severity, "indi")

	# Debug
	print("Executing: ")
	cmd.printCommand()

	result = cmd.execute(dbmanager.conn.connection.getSession())

	# Debug
	print(result)

	return result

def getIndiForNodes(sym, sick):
	whereSym = commands.Where().addFilter("name", sym.name)
	whereSick = commands.Where().addFilter("name", sick.name)
	cmd = commands.Command().matchNode("symptom", "sym", whereSym).matchNode("sickness", "sick", whereSick)
	cmd = cmd.findRelation("indicates", "symptom", "sickness", "indi", "sym", "sick")

	# Debug
	print("Executing: ")
	cmd.printCommand()

	result = cmd.execute(dbmanager.conn.connection.getSession())

	# Debug
	print(result)

	return result