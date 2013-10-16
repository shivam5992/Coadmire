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

collection2 = db.level2 

collection2.drop()

q21 ={
	'_id' 		: 	1,
	'question' 		: 	' 2 What is your age ?',
	'optiona' 	: 	'21',
	'optionb' 	: 	'22',
	'optionc' 	: 	'23',
	'optiond' 	: 	'24',
	'answer'	: 	'21',
}
q22 ={
	'_id' 		: 	2,
	'question' 		: 	'2 What is your name ?',
	'optiona' 	: 	'af',
	'optionb' 	: 	'bd',
	'optionc' 	: 	'ca',
	'optiond' 	: 	'dq',
	'answer'	: 	'bd',
}

q23 ={
	'_id' 		: 	3,
	'question' 		: 	'2 What is your class ?',
	'optiona' 	: 	'12',
	'optionb' 	: 	'11',
	'optionc' 	: 	'10',
	'optiond' 	: 	'9',
	'answer'	: 	'11',
}

q24 ={
	'_id' 		: 	4,
	'question' 		: 	'2 What is your profession ?',
	'optiona' 	: 	'doc',
	'optionb' 	: 	'paint',
	'optionc' 	: 	'eng',
	'optiond' 	: 	'web',
	'answer'	: 	'doc',
}

q25 ={
	'_id' 		: 	5,
	'question' 		: 	'2 What is your color ?',
	'optiona' 	: 	'red',
	'optionb' 	: 	'green',
	'optionc' 	: 	'blue',
	'optiond' 	: 	'pink',
	'answer'	: 	'red',
}

collection2.insert(q21)
collection2.insert(q22)
collection2.insert(q23)
collection2.insert(q24)
collection2.insert(q25)

collection3 = db.level3 

collection3.drop()

q31 ={
	'_id' 		: 	1,
	'question' 		: 	'3 What is your age ?',
	'optiona' 	: 	'21',
	'optionb' 	: 	'22',
	'optionc' 	: 	'23',
	'optiond' 	: 	'24',
	'answer'	: 	'21',
}
q32 ={
	'_id' 		: 	2,
	'question' 		: 	'3 What is your name ?',
	'optiona' 	: 	'af',
	'optionb' 	: 	'bd',
	'optionc' 	: 	'ca',
	'optiond' 	: 	'dq',
	'answer'	: 	'bd',
}

q33 ={
	'_id' 		: 	3,
	'question' 		: 	'3 What is your class ?',
	'optiona' 	: 	'12',
	'optionb' 	: 	'11',
	'optionc' 	: 	'10',
	'optiond' 	: 	'9',
	'answer'	: 	'11',
}

q34 ={
	'_id' 		: 	4,
	'question' 		: 	'3 What is your profession ?',
	'optiona' 	: 	'doc',
	'optionb' 	: 	'paint',
	'optionc' 	: 	'eng',
	'optiond' 	: 	'web',
	'answer'	: 	'doc',
}

q35 ={
	'_id' 		: 	5,
	'question' 		: 	'3 What is your color ?',
	'optiona' 	: 	'red',
	'optionb' 	: 	'green',
	'optionc' 	: 	'blue',
	'optiond' 	: 	'pink',
	'answer'	: 	'red',
}

collection3.insert(q31)
collection3.insert(q32)
collection3.insert(q33)
collection3.insert(q34)
collection3.insert(q35)

collection4 = db.level4 

collection4.drop()

q41 ={
	'_id' 		: 	1,
	'question' 		: 	'4 What is your age ?',
	'optiona' 	: 	'21',
	'optionb' 	: 	'22',
	'optionc' 	: 	'23',
	'optiond' 	: 	'24',
	'answer'	: 	'21',
}
q42 ={
	'_id' 		: 	2,
	'question' 		: 	'4 What is your name ?',
	'optiona' 	: 	'af',
	'optionb' 	: 	'bd',
	'optionc' 	: 	'ca',
	'optiond' 	: 	'dq',
	'answer'	: 	'bd',
}

q43 ={
	'_id' 		: 	3,
	'question' 		: 	'4 What is your class ?',
	'optiona' 	: 	'12',
	'optionb' 	: 	'11',
	'optionc' 	: 	'10',
	'optiond' 	: 	'9',
	'answer'	: 	'11',
}

q44 ={
	'_id' 		: 	4,
	'question' 		: 	'4 What is your profession ?',
	'optiona' 	: 	'doc',
	'optionb' 	: 	'paint',
	'optionc' 	: 	'eng',
	'optiond' 	: 	'web',
	'answer'	: 	'doc',
}

q45 ={
	'_id' 		: 	5,
	'question' 		: 	'4 What is your color ?',
	'optiona' 	: 	'red',
	'optionb' 	: 	'green',
	'optionc' 	: 	'blue',
	'optiond' 	: 	'pink',
	'answer'	: 	'red',
}

collection4.insert(q41)
collection4.insert(q42)
collection4.insert(q43)
collection4.insert(q44)
collection4.insert(q45)