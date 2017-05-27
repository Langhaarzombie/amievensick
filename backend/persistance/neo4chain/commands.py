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
		out = self.name + ": " + properDataFormat(self.value)
		return out

	def __init__(self, fname, fvalue):
		self.name = fname
		self.value = fvalue

class Where:

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
		return self

	def __init__(self, init_filter = []):
		self.filter = init_filter

class FilterID:

	 def build(self):
	 	out = "ID("+self.context_name+") = "+str(self.eyed)
	 	return out

	 def __init__(self, context_name, eyed):
	 	self.context_name = context_name
	 	self.eyed = eyed

class WhereID: # When searching for an ID the context name passed in findNode(...) must be the same as in WhereId(...)

	def build(self):
		out = "WHERE "+self.filter.build()
		return out

	def __init__(self, id = 0, context_name = "result_find_node_default_context_name"):
		self.filter = FilterID(context_name, id)

class Command:

	def addNode(self, label, context_name = ""):
		out = Command(self.command + "\n" + "CREATE ("+context_name+":"+label+")")
		return out

	def addRelation(self, label, node_from, node_to, context_name = ""):
		out = Command(self.command + "\n" + "CREATE ("+node_from+")-["+context_name+":"+label+"]->("+node_to+")")
		return out

	def setProperty(self, name, value, context_name):
		out = Command(self.command + "\n" + "SET "+context_name+"."+name+" = "+properDataFormat(value))
		return out

	#find a node and immediately return it (! onyl at the end of a statement)
	def findNode(self, label, context_name = "result_find_node_default_context_name", where = None): # the default context name should only be used when searching for exactly one node
		# Build match clause
		out = Command(self.command + "\n" + "MATCH ("+context_name+":"+label)

		# Build where clause
		if(where is not None):
			if(where.__class__.__name__ == "Where"):
				if(len(where.filter) > 0):
					out = Command(out.command + " " + where.build() + ")")
			elif(where.__class__.__name__ == "WhereID"):
				out = Command(out.command + ") " + where.build())
		else:
			out = Command(out.command + ") ")

		# Build return clause 
		out = Command(out.command + " return "+context_name)

		return out

	#find a relation and immediately return it (! onyl at the end of a statement)
	def findRelation(self, rel_label, node_label_from, node_label_to, context_name = "result_find_relation_default_context_name", node_from = "", node_to = "", where = None):
		# Build match clause
		out = Command(self.command + "\n" + "MATCH (" + node_from + ":" + node_label_from + ")-[" + context_name + ":" + rel_label)

		# Build where clause
		if(where is not None):
			if(where.__class__.__name__ == "Where"):
				if(len(where.filter) > 0):
					out = Command(out.command + " " + where.build() + "]-(" + node_to + ":" + node_label_to + ")")
			elif(where.__class__.__name__ == "WhereID"):
				out = Command(out.command + "]-(" + node_to + ":" + node_label_to + ") " + where.build())
		else:
			out = Command(out.command + "]-(" + node_to + ":" + node_label_to + ")")

		# Build return clause 
		out = Command(out.command + " return "+context_name)

		return out

	#match a node and use it in later code
	def matchNode(self, label, context_name, where = None):
		# Build match clause
		out = Command(self.command + "\n" + "MATCH ("+context_name+":"+label)

		# Build where clause
		if(where is not None):
			if(where.__class__.__name__ == "Where"):
				if(len(where.filter) > 0):
					out = Command(out.command + where.build() + ") ")
			elif(where.__class__.__name__ == "WhereID"):
				out = Command(out.command + ") " + where.build())
		else:
			out = Command(out.command + ") ")

		return out

	#match a relation and use it in later code
	def matchRelation(self, rel_label, node_label_from, node_label_to, context_name, node_from = "", node_to = "", where = None):
		# Build match clause
		out = Command(self.command + "\n" + "MATCH (" + node_from + ":" + node_label_from + ")-[" + context_name + ":" + rel_label)

		# Build where clause
		if(where is not None):
			if(where.__class__.__name__ == "Where"):
				if(len(where.filter) > 0):
					out = Command(out.command + " " + where.build() + "]-(" + node_to + ":" + node_label_to + ")")
			elif(where.__class__.__name__ == "WhereID"):
				out = Command(out.command + "]-(" + node_to + ":" + node_label_to + ") " + where.build())
		else:
			out = Command(out.command + "]-(" + node_to + ":" + node_label_to + ")")

		return out


	# used at the end to return a specific value
	def returnSingleValue(self, context_name):
		out = Command(self.command + "\n" + "RETURN " + context_name)
		return out

	# TODO add methods for removing nodes

	def printCommand(self):
		print(self.command)
		return self

	def execute(self, session):
		out = session.run(self.command)
		return out

	def __init__(self, init_command = ""):
		self.command = init_command