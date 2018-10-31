# This is the backend system for *Am I Even Sick*
In the following text will explain its capabilities and show you how to use it.

## Creating stuff
### Creating a Symptom
URL pattern (POST): 
~~~~
url/symptom
~~~~
Example for request body: 
~~~~
{"symptom": {"name": "Fever"}}
~~~~
### Creating a Sickness
URL pattern (POST): 
~~~~
url/sickness
~~~~
Example for request body: 
~~~~
{"sickness": {"name": "Flue", "requires_medication": False, "location": "Around the globe", "prevelance": "Common"}}
~~~~
### Creating an Indicates (relation between Symptom and Sickness)
URL pattern (POST): 
~~~~
url/indicates
~~~~
Example for request body:
~~~~
{"indicates": {"severity": "Major", "from": "Fever", "to": "Flue"}}
~~~~

## Getting stuff

### Getting all Symptoms
URL pattern (GET): 
~~~~
url/symptom
~~~~
### Getting all Sicknesses
URL pattern (GET): 
~~~~
url/sickness
~~~~
### Getting a Symptom by its name
URL pattern (GET): 
~~~~
url/symptom/<nameOfSymptom>
~~~~
### Getting a Sickness by its name
URL pattern (GET): 
~~~~
url/sickness/<nameOfSickness>
~~~~
### Getting a Indicates by the name of a Symptom and a Sickness
URL pattern (GET): 
~~~~
url/indicates/<nameOfSymptom>/<nameOfSickness>
~~~~
### Getting all Sicknesses that realte to certain Symptoms
URL patter (POST):
~~~~
url/sbs
~~~~
Example for request body:
~~~~
{"symptoms": [{"name": "Headache"},{"name": "Fever"}]}
~~~~
