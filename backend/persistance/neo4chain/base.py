
def properDataFormat(value):
		out = ""
		if(type(value) is bool):
			out = "toBoolean("+str(value)+")"
		elif(type(value) is str):
			out = "toString(\""+value+"\")"
		elif(type(value) is int):
			out = "toInteger("+str(value)+")"
		elif(type(value) is float):
			out = "toFloat("+str(value)+")"
		return out

class Filter:

	def build(self):
		return self.name + ": " + properDataFormat(self.value)

	def __init__(self, fname, fvalue):
		self.name = fname
		self.value = fvalue

class Where:

	def printFilter(self):
		print(self.filter)
		for f in self.filter:
			print(f.build())

	def addFilter(self, name, value):
		self.filter.append(Filter(name, value))
		out = Where(self.filter)
		return out

	def __init__(self, init_filter = []):
		self.filter = init_filter

class Command:

	def addNode(self, label, context_name = ""):
		out = Command(self.command + "\n" + "CREATE ("+context_name+":"+label+")")
		return out

	def addRelation(self, label, node_from, node_to, context_name = ""):
		out = Command(self.command + "\n" + "CREATE ("+node_from+")-["+context_name+":"+label+"]->("+node_to+")")
		return out

	def addProperty(self, name, value, node):
		out = Command(self.command + "\n" + "SET "+node+"."+name+" = "+properDataFormat(value))
		return out

	def findNode(self, label, where = None, context_name = "result_find_node_default_context_name"):
		
		out = Command(self.command + "\n" + "MATCH ("+context_name+":"+label)

		if(where is not None and len(where.filter) > 0):
			out = Command(out.command + " {")
			for f in where.filter:
				out = Command(out.command + f.build()) #TODO multiple filter with ","
			out = Command(out.command + "}")

		out = Command(out.command + ") return "+context_name)
		return out

	def printCommand(self):
		print(self.command)
		return self

	def execute(self, session):
		out = session.run(self.command)
		return out

	def __init__(self, init_command = ""):
		self.command = init_command

#CREATE (Keanu:Person {name:'Keanu Reeves', born:1964})

#CREATE (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrix)

#MATCH (tom {name: "Tom Hanks"}) RETURN tom

#MATCH (cloudAtlas {title: "Cloud Atlas"})<-[:DIRECTED]-(directors) RETURN directors.name

