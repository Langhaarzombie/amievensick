#!/usr/bin/python

from neo4j.v1 import GraphDatabase, basic_auth
import commands

class Connection: # manages the connection to the database
	def __init__(self, url, username, password):
		self.url = url
		self.username = username
		self.password = password

	def getDriver(self):
		if(not hasattr(self, 'driver')):
			#default: bolt://localhost:7687, neo4j, neo4j
			self.driver = GraphDatabase.driver(self.url, auth=basic_auth(self.username, self.password))
		return self.driver

	def getSession(self):
		if(not hasattr(self, 'session')):
			self.session = self.getDriver().session()
		return self.session

	def disconnect(self):
		self.getSession().close()

class GarbageCollector: # responsible for deleting relations and nodes that were created while testing
	def __init__(self, session):
		self.session = session

	def deleteRelations(self, type):
		result = self.session.run("MATCH ()-[r:"+type+"]-() DELETE r")
		return result

	def deleteNodes(self, label):
		result = self.session.run("MATCH (n:"+label+") DELETE n")
		return result

	def cleanUp(self): # TODO adjust to multiple nodes
		self.deleteRelations("relates") # TODO adjust relation
		self.deleteNodes("File")


### old ###

# Matching

def findAllNodes(label):
	result = session.run("MATCH (n:"+label+") RETURN n.name AS name, n.path AS path")
	return result

# Printing

def printResult(result):
	for record in result:
		print("%s" % (record["name"]))

