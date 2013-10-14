from pymongo import MongoClient
import codecs

client = MongoClient()
db = client.coadtest
collection = db.level1 

collection.drop()

new_entry ={
	'_id' 		: 	1,
	'question' 		: 	' What is your age ?',
	'optiona' 	: 	'21',
	'optionb' 	: 	'22',
	'optionc' 	: 	'23',
	'optiond' 	: 	'24',
	'answer'	: 	'21',
}

collection.insert(new_entry)