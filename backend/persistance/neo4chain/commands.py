#!/usr/bin/python

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
		print(self.build())

	def build(self):
		out = "{"
		temp = ""
		for x in xrange(0,len(self.filter)):
			out = out + temp + self.filter[x].build()
			temp = ", "
		out = out + "}"
		return out

	def addFilter(self, name, value):
		self.filter.append(Filter(name, value))
		out = Where(self.filter)
		return out

	def __init__(self, init_filter = []):
		self.filter = init_filter

class FilterID:

	 def build(self):
	 	return "ID("+self.context_name+") = "+str(self.eyed)

	 def __init__(self, context_name, eyed):
	 	self.context_name = context_name
	 	self.eyed = eyed

class WhereID:

	def printFilter(self):
		print(self.build())

	def build(self):
		return "WHERE "+self.filter.build()

	def __init__(self, context_name, id = 0):
		self.filter = FilterID(context_name, id)

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

	def findNode(self, label, where = None, whereID = None , context_name = "result_find_node_default_context_name"):
		
		out = Command(self.command + "\n" + "MATCH ("+context_name+":"+label)

		if(where is not None and len(where.filter) > 0):
			out = Command(out.command + where.build())

		out = Command(out.command + ") ")

		if(whereID is not None and whereID.filter is not None):
			out = Command(out.command + whereID.build())

		out = Command(out.command + " return "+context_name)

		return out

	def printCommand(self):
		print(self.command)
		return self

	def execute(self, session):
		out = session.run(self.command)
		return out

	def __init__(self, init_command = ""):
		self.command = init_command

