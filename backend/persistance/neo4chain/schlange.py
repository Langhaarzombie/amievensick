#!/usr/bin/python

from neo4j.v1 import GraphDatabase, basic_auth
import base

# Managing db connection

def auth(url, username, password): #default: bolt://localhost:7687, neo4j, neo4j
	return GraphDatabase.driver(url, auth=basic_auth(username, password))
	
def getSession():
	return driver.session()

def disconnect():
	session.close()

# Basic command executions

def executeCommand(command):
	result = session.run(command)

# Creating nodes

def createFile(name, path):
	result = session.run("CREATE (f:File {name: {name}, path: {path}})", {"name": name, "path": path})
	return result

# Matching

def findAllNodes(label):
	result = session.run("MATCH (n:"+label+") RETURN n.name AS name, n.path AS path")
	return result

# Printing

def printResult(result):
	for record in result:
		print("%s" % (record["name"]))

# Garbage Collection

def deleteRelations(type):
	result = session.run("MATCH ()-[r:"+type+"]-() DELETE r")
	return result

def deleteNodes(label):
	result = session.run("MATCH (n:"+label+") DELETE n")
	return result

def cleanUp(): # TODO adjust to multiple nodes
	deleteRelations("relates") # TODO adjust relation
	deleteNodes("File")

# Tests

driver = auth("bolt://localhost:7687", "neo4j", "maxmm1999")
session = getSession()

cmd = base.Command()
#result = cmd.addNode("File", "a").addNode("File", "b").addNode("File", "c").addRelation("relates", "a", "b", "r").addRelation("relates", "b", "c", "r2").execute(session)
#result = cmd.addNode("File", "a").addProperty("name", "test", "a").execute(session)

#result = cmd.addNode("File", "f1").addNode("File", "f2").addNode("File", "f3").addProperty("name", "notes.txt", "f1").addProperty("created", "2017-05-12", "f2").addProperty("name", "exercise.pdf", "f2").addProperty("name", "calculations.jpg", "f3").addRelation("relates", "f1", "f2", "r_f1_f2").addRelation("relates", "f3", "f2", "r_f3_f2").printCommand().execute(session)

cmd = cmd.addNode("File", "f1").addNode("File", "f2").addNode("File", "f3")
cmd = cmd.addProperty("name", "notes.txt", "f1").addProperty("created", "2017-05-12", "f2").addProperty("name", "exercise.pdf", "f2").addProperty("name", "calculations.jpg", "f3")
cmd = cmd.addRelation("relates", "f1", "f2 ", "r_f1_f2").addRelation("relates", "f3", "f2", "r_f3_f2").printCommand()
cmd.execute(session)
where = base.Where()
where = where.addFilter("name", "notes.txt")
#where.printFilter()

cmd = base.Command().findNode("File", where).printCommand()

result = cmd.execute(session)
print(result)

cleanUp()
disconnect()