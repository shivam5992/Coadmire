from pymongo import MongoClient
import codecs

client = MongoClient()
db = client.coadtest

collection = db.level0
collection.drop()

q01 ={
	'_id' 		: 	1,
	'question' 		: 	'0 What is your age ?',
	'option1' 	: 	'21',
	'option2' 	: 	'22',
	'option3' 	: 	'23',
	'option4' 	: 	'24',
	'answer'	: 	'21',
}
q02 ={
	'_id' 		: 	2,
	'question' 		: 	'0 What is your name ?',
	'option1' 	: 	'af',
	'option2' 	: 	'bd',
	'option3' 	: 	'ca',
	'option4' 	: 	'dq',
	'answer'	: 	'bd',
}

q03 ={
	'_id' 		: 	3,
	'question' 		: 	'0 What is your class ?',
	'option1' 	: 	'12',
	'option2' 	: 	'11',
	'option3' 	: 	'10',
	'option4' 	: 	'9',
	'answer'	: 	'11',
}

q04 ={
	'_id' 		: 	4,
	'question' 		: 	'0 What is your profession ?',
	'option1' 	: 	'doc',
	'option2' 	: 	'paint',
	'option3' 	: 	'eng',
	'option4' 	: 	'web',
	'answer'	: 	'doc',
}

q05 ={
	'_id' 		: 	5,
	'question' 		: 	'0 What is your color ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
	'answer'	: 	'red',
}

q06 ={
	'_id' 		: 	6,
	'question' 		: 	'0 ques 6 ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
	'answer'	: 	'red',
}

q07 ={
	'_id' 		: 	7,
	'question' 		: 	'0 ques 7 ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
	'answer'	: 	'red',
}

q08 ={
	'_id' 		: 	8,
	'question' 		: 	'0 ques 8 ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
	'answer'	: 	'red',
}

q09 ={
	'_id' 		: 	9,
	'question' 		: 	'0 ques 9 ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
	'answer'	: 	'red',
}

q010 ={
	'_id' 		: 	10,
	'question' 		: 	'0 ques 10 ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
	'answer'	: 	'red',
}

collection.insert(q01)
collection.insert(q02)
collection.insert(q03)
collection.insert(q04)
collection.insert(q05)
collection.insert(q06)
collection.insert(q07)
collection.insert(q08)
collection.insert(q09)
collection.insert(q010)

collection1 = db.level1

collection1.drop()

q11 ={
	'_id' 		: 	1,
	'question' 		: 	'1 What is your age ?',
	'option1' 	: 	'21',
	'option2' 	: 	'22',
	'option3' 	: 	'23',
	'option4' 	: 	'24',
	'answer'	: 	'21',
}
q12 ={
	'_id' 		: 	2,
	'question' 		: 	'1 What is your name ?',
	'option1' 	: 	'af',
	'option2' 	: 	'bd',
	'option3' 	: 	'ca',
	'option4' 	: 	'dq',
	'answer'	: 	'bd',
}

q13 ={
	'_id' 		: 	3,
	'question' 		: 	'1 What is your class ?',
	'option1' 	: 	'12',
	'option2' 	: 	'11',
	'option3' 	: 	'10',
	'option4' 	: 	'9',
	'answer'	: 	'11',
}

q14 ={
	'_id' 		: 	4,
	'question' 		: 	'1 What is your profession ?',
	'option1' 	: 	'doc',
	'option2' 	: 	'paint',
	'option3' 	: 	'eng',
	'option4' 	: 	'web',
	'answer'	: 	'doc',
}

q15 ={
	'_id' 		: 	5,
	'question' 		: 	'1 What is your color ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
	'answer'	: 	'red',
}

collection1.insert(q11)
collection1.insert(q12)
collection1.insert(q13)
collection1.insert(q14)
collection1.insert(q15)

collection2 = db.level2 

collection2.drop()

q21 ={
	'_id' 		: 	1,
	'question' 		: 	' 2 What is your age ?',
	'option1' 	: 	'21',
	'option2' 	: 	'22',
	'option3' 	: 	'23',
	'option4' 	: 	'24',
	'answer'	: 	'21',
}
q22 ={
	'_id' 		: 	2,
	'question' 		: 	'2 What is your name ?',
	'option1' 	: 	'af',
	'option2' 	: 	'bd',
	'option3' 	: 	'ca',
	'option4' 	: 	'dq',
	'answer'	: 	'bd',
}

q23 ={
	'_id' 		: 	3,
	'question' 		: 	'2 What is your class ?',
	'option1' 	: 	'12',
	'option2' 	: 	'11',
	'option3' 	: 	'10',
	'option4' 	: 	'9',
	'answer'	: 	'11',
}

q24 ={
	'_id' 		: 	4,
	'question' 		: 	'2 What is your profession ?',
	'option1' 	: 	'doc',
	'option2' 	: 	'paint',
	'option3' 	: 	'eng',
	'option4' 	: 	'web',
	'answer'	: 	'doc',
}

q25 ={
	'_id' 		: 	5,
	'question' 		: 	'2 What is your color ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
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
	'option1' 	: 	'21',
	'option2' 	: 	'22',
	'option3' 	: 	'23',
	'option4' 	: 	'24',
	'answer'	: 	'21',
}
q32 ={
	'_id' 		: 	2,
	'question' 		: 	'3 What is your name ?',
	'option1' 	: 	'af',
	'option2' 	: 	'bd',
	'option3' 	: 	'ca',
	'option4' 	: 	'dq',
	'answer'	: 	'bd',
}

q33 ={
	'_id' 		: 	3,
	'question' 		: 	'3 What is your class ?',
	'option1' 	: 	'12',
	'option2' 	: 	'11',
	'option3' 	: 	'10',
	'option4' 	: 	'9',
	'answer'	: 	'11',
}

q34 ={
	'_id' 		: 	4,
	'question' 		: 	'3 What is your profession ?',
	'option1' 	: 	'doc',
	'option2' 	: 	'paint',
	'option3' 	: 	'eng',
	'option4' 	: 	'web',
	'answer'	: 	'doc',
}

q35 ={
	'_id' 		: 	5,
	'question' 		: 	'3 What is your color ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
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
	'option1' 	: 	'21',
	'option2' 	: 	'22',
	'option3' 	: 	'23',
	'option4' 	: 	'24',
	'answer'	: 	'21',
}
q42 ={
	'_id' 		: 	2,
	'question' 		: 	'4 What is your name ?',
	'option1' 	: 	'af',
	'option2' 	: 	'bd',
	'option3' 	: 	'ca',
	'option4' 	: 	'dq',
	'answer'	: 	'bd',
}

q43 ={
	'_id' 		: 	3,
	'question' 		: 	'4 What is your class ?',
	'option1' 	: 	'12',
	'option2' 	: 	'11',
	'option3' 	: 	'10',
	'option4' 	: 	'9',
	'answer'	: 	'11',
}

q44 ={
	'_id' 		: 	4,
	'question' 		: 	'4 What is your profession ?',
	'option1' 	: 	'doc',
	'option2' 	: 	'paint',
	'option3' 	: 	'eng',
	'option4' 	: 	'web',
	'answer'	: 	'doc',
}

q45 ={
	'_id' 		: 	5,
	'question' 		: 	'4 What is your color ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
	'answer'	: 	'red',
}

collection4.insert(q41)
collection4.insert(q42)
collection4.insert(q43)
collection4.insert(q44)
collection4.insert(q45)

collection5 = db.level5 
collection5.drop()

q51 ={
	'_id' 		: 	1,
	'question' 		: 	'5 What is your age ?',
	'option1' 	: 	'21',
	'option2' 	: 	'22',
	'option3' 	: 	'23',
	'option4' 	: 	'24',
	'answer'	: 	'21',
}
q52 ={
	'_id' 		: 	2,
	'question' 		: 	'5 What is your name ?',
	'option1' 	: 	'af',
	'option2' 	: 	'bd',
	'option3' 	: 	'ca',
	'option4' 	: 	'dq',
	'answer'	: 	'bd',
}

q53 ={
	'_id' 		: 	3,
	'question' 		: 	'5 What is your class ?',
	'option1' 	: 	'12',
	'option2' 	: 	'11',
	'option3' 	: 	'10',
	'option4' 	: 	'9',
	'answer'	: 	'11',
}

q54 ={
	'_id' 		: 	4,
	'question' 		: 	'5 What is your profession ?',
	'option1' 	: 	'doc',
	'option2' 	: 	'paint',
	'option3' 	: 	'eng',
	'option4' 	: 	'web',
	'answer'	: 	'doc',
}

q55 ={
	'_id' 		: 	5,
	'question' 		: 	'5 What is your color ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
	'answer'	: 	'red',
}

collection5.insert(q51)
collection5.insert(q52)
collection5.insert(q53)
collection5.insert(q54)
collection5.insert(q55)

collection6 = db.level6 
collection6.drop()

q61 ={
	'_id' 		: 	1,
	'question' 		: 	'6 What is your age ?',
	'option1' 	: 	'21',
	'option2' 	: 	'22',
	'option3' 	: 	'23',
	'option4' 	: 	'24',
	'answer'	: 	'21',
}
q62 ={
	'_id' 		: 	2,
	'question' 		: 	'6 What is your name ?',
	'option1' 	: 	'af',
	'option2' 	: 	'bd',
	'option3' 	: 	'ca',
	'option4' 	: 	'dq',
	'answer'	: 	'bd',
}

q63 ={
	'_id' 		: 	3,
	'question' 		: 	'6 What is your class ?',
	'option1' 	: 	'12',
	'option2' 	: 	'11',
	'option3' 	: 	'10',
	'option4' 	: 	'9',
	'answer'	: 	'11',
}

q64 ={
	'_id' 		: 	4,
	'question' 		: 	'6 What is your profession ?',
	'option1' 	: 	'doc',
	'option2' 	: 	'paint',
	'option3' 	: 	'eng',
	'option4' 	: 	'web',
	'answer'	: 	'doc',
}

q65 ={
	'_id' 		: 	5,
	'question' 		: 	'6 What is your color ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
	'answer'	: 	'red',
}

collection6.insert(q61)
collection6.insert(q62)
collection6.insert(q63)
collection6.insert(q64)
collection6.insert(q65)

collection7 = db.level7 
collection7.drop()

q71 ={
	'_id' 		: 	1,
	'question' 		: 	'7 What is your age ?',
	'option1' 	: 	'21',
	'option2' 	: 	'22',
	'option3' 	: 	'23',
	'option4' 	: 	'24',
	'answer'	: 	'21',
}
q72 ={
	'_id' 		: 	2,
	'question' 		: 	'7 What is your name ?',
	'option1' 	: 	'af',
	'option2' 	: 	'bd',
	'option3' 	: 	'ca',
	'option4' 	: 	'dq',
	'answer'	: 	'bd',
}

q73 ={
	'_id' 		: 	3,
	'question' 		: 	'7 What is your class ?',
	'option1' 	: 	'12',
	'option2' 	: 	'11',
	'option3' 	: 	'10',
	'option4' 	: 	'9',
	'answer'	: 	'11',
}

q74 ={
	'_id' 		: 	4,
	'question' 		: 	'7 What is your profession ?',
	'option1' 	: 	'doc',
	'option2' 	: 	'paint',
	'option3' 	: 	'eng',
	'option4' 	: 	'web',
	'answer'	: 	'doc',
}

q75 ={
	'_id' 		: 	5,
	'question' 		: 	'7 What is your color ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
	'answer'	: 	'red',
}

collection7.insert(q71)
collection7.insert(q72)
collection7.insert(q73)
collection7.insert(q74)
collection7.insert(q75)

collection8 = db.level8

collection8.drop()

q81 ={
	'_id' 		: 	1,
	'question' 		: 	'8 What is your age ?',
	'option1' 	: 	'21',
	'option2' 	: 	'22',
	'option3' 	: 	'23',
	'option4' 	: 	'24',
	'answer'	: 	'21',
}
q82 ={
	'_id' 		: 	2,
	'question' 		: 	'8 What is your name ?',
	'option1' 	: 	'af',
	'option2' 	: 	'bd',
	'option3' 	: 	'ca',
	'option4' 	: 	'dq',
	'answer'	: 	'bd',
}

q83 ={
	'_id' 		: 	3,
	'question' 		: 	'8 What is your class ?',
	'option1' 	: 	'12',
	'option2' 	: 	'11',
	'option3' 	: 	'10',
	'option4' 	: 	'9',
	'answer'	: 	'11',
}

q84 ={
	'_id' 		: 	4,
	'question' 		: 	'8 What is your profession ?',
	'option1' 	: 	'doc',
	'option2' 	: 	'paint',
	'option3' 	: 	'eng',
	'option4' 	: 	'web',
	'answer'	: 	'doc',
}

q85 ={
	'_id' 		: 	5,
	'question' 		: 	'8 What is your color ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
	'answer'	: 	'red',
}

collection8.insert(q81)
collection8.insert(q82)
collection8.insert(q83)
collection8.insert(q84)
collection8.insert(q85)

collection9 = db.level9

collection9.drop()

q91 ={
	'_id' 		: 	1,
	'question' 		: 	'9 What is your age ?',
	'option1' 	: 	'21',
	'option2' 	: 	'22',
	'option3' 	: 	'23',
	'option4' 	: 	'24',
	'answer'	: 	'21',
}
q92 ={
	'_id' 		: 	2,
	'question' 		: 	'9 What is your name ?',
	'option1' 	: 	'af',
	'option2' 	: 	'bd',
	'option3' 	: 	'ca',
	'option4' 	: 	'dq',
	'answer'	: 	'bd',
}

q93 ={
	'_id' 		: 	3,
	'question' 		: 	'9 What is your class ?',
	'option1' 	: 	'12',
	'option2' 	: 	'11',
	'option3' 	: 	'10',
	'option4' 	: 	'9',
	'answer'	: 	'11',
}

q94 ={
	'_id' 		: 	4,
	'question' 		: 	'9 What is your profession ?',
	'option1' 	: 	'doc',
	'option2' 	: 	'paint',
	'option3' 	: 	'eng',
	'option4' 	: 	'web',
	'answer'	: 	'doc',
}

q95 ={
	'_id' 		: 	5,
	'question' 		: 	'9 What is your color ?',
	'option1' 	: 	'red',
	'option2' 	: 	'green',
	'option3' 	: 	'blue',
	'option4' 	: 	'pink',
	'answer'	: 	'red',
}

collection9.insert(q91)
collection9.insert(q92)
collection9.insert(q93)
collection9.insert(q94)
collection9.insert(q95)

