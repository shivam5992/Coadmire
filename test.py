from pymongo import MongoClient

client = MongoClient()
db = client.coadtest


level = "level" + str(3)	
prevcollection = db[level]
prevdoc = prevcollection.find_one({ '_id' : 5 })
print (prevdoc['question'])

	

