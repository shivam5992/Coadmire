from pymongo import MongoClient
import codecs

client = MongoClient()
db = client.coadmire

collection = db.testheroku
collection.drop()
q1 ={
        "_id" : 1,
        "level" : "level1",
        "question" : "What does HTML stand for ?",
        "answer"   : "Hyper Text Markup Language",
        "option1" : "Hyper Text Markup Language",
        "option3" : "Home Tool Markup Language",
        "option2" : "Hyperlinks and Text Markup Language",
        "option4" : "None of these"

}
collection.insert(q1);