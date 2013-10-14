from pymongo import MongoClient
import codecs

client = MongoClient()
db = client.coadtest
collection = db.level1 

collection.drop()

q1 ={
	'_id' 		: 	1,
	'question' 		: 	' What is your age ?',
	'optiona' 	: 	'21',
	'optionb' 	: 	'22',
	'optionc' 	: 	'23',
	'optiond' 	: 	'24',
	'answer'	: 	'21',
}
q2 ={
	'_id' 		: 	2,
	'question' 		: 	' What is your name ?',
	'optiona' 	: 	'af',
	'optionb' 	: 	'bd',
	'optionc' 	: 	'ca',
	'optiond' 	: 	'dq',
	'answer'	: 	'bd',
}

q3 ={
	'_id' 		: 	3,
	'question' 		: 	' What is your class ?',
	'optiona' 	: 	'12',
	'optionb' 	: 	'11',
	'optionc' 	: 	'10',
	'optiond' 	: 	'9',
	'answer'	: 	'11',
}

q4 ={
	'_id' 		: 	4,
	'question' 		: 	' What is your profession ?',
	'optiona' 	: 	'doc',
	'optionb' 	: 	'paint',
	'optionc' 	: 	'eng',
	'optiond' 	: 	'web',
	'answer'	: 	'doc',
}

q5 ={
	'_id' 		: 	5,
	'question' 		: 	' What is your color ?',
	'optiona' 	: 	'red',
	'optionb' 	: 	'green',
	'optionc' 	: 	'blue',
	'optiond' 	: 	'pink',
	'answer'	: 	'red',
}

collection.insert(q1)
collection.insert(q2)
collection.insert(q3)
collection.insert(q4)
collection.insert(q5)
