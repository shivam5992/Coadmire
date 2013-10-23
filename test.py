from pymongo import MongoClient
import codecs

client = MongoClient()
db = client.coadmire

admin_level = "level4"
admin_collection = db[admin_level]


ida = admin_collection.count()
print (ida+1)

'''
db.seqs.insert({
    'collection': admin_collection,
    'id': 0
})

def insert_doc(x,doc):
    doc['_id'] = str(db.seqs.find_and_modify(
        query={'collection': x},
        update={'$inc': {'id': 1}},
        fields={'id': 1, '_id': 0},
        new=True 
    ).get('id'))

    try:
        x.insert(doc)

    except pymongo.errors.DuplicateKeyError as e:
        insert_doc(x,doc)


admin_doc ={
        'question'  :   "admin_quesion",
        'option1'   :   "admin_option1",
        'option2'   :   "admin_option2",
        'option3'   :   "admin_option3",
        'option4'   :   "admin_option4",
        'answer'    :   "admin_answer",
        'level'     :   "admin_level",
        }


x = admin_collection
insert_doc(x,admin_doc)
'''