from neo4chain import dbmanager, commands
import os

# connection = dbmanager.Connection("bolt://localhost:7687", "neo4j", "maxmm1999")
url = os.environ.get("GRAPHENEDB_BOLT_URL")
print(url)
url = "bolt://hobby-jllldejmojekgbkedincghpl.dbs.graphenedb.com:24786"
user = os.environ.get("GRAPHENEDB_BOLT_USER")
print(user)
user = "app68154701-70rEaA"
password = os.environ.get("GRAPHENEDB_BOLT_PASSWORD")
print(password)
password = "b.dZtmji6RST3j.cv4W3npw2fjUywVe"
conn = dbmanager.Connector(url, user, password)

def insert():
	cmd = commands.Command().addNode("symptom", "sym1").setProperty("name", "Coughing", "sym1")
	cmd = cmd.addNode("sickness", "sick1").setProperty("name", "Flue", "sick1").setProperty("requires_medication", "False", "sick1").setProperty("prevalence", "Common", "sick1").setProperty("location", "Around the globe", "sick1")
	cmd = cmd.addNode("symptom", "sym2").setProperty("name", "Headache", "sym2")
	cmd = cmd.addNode("sickness", "sick2").setProperty("name", "Migraine", "sick2").setProperty("requires_medication", "False", "sick2").setProperty("prevalence", "Common", "sick2").setProperty("location", "Around the globe", "sick2")
	cmd = cmd.addRelation("indicates", "sym1", "sick1", "in1").setProperty("severity", "Casual", "in1")
	cmd = cmd.addRelation("indicates", "sym2", "sick1", "in2").setProperty("severity", "Casual", "in2")
	cmd = cmd.addRelation("indicates", "sym2", "sick2", "in3").setProperty("severity", "Major", "in3")
	cmd.printCommand().execute(conn.connection.getSession())

	conn.connection.disconnect()