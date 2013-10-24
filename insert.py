from pymongo import MongoClient
import codecs

client = MongoClient()
db = client.coadmire

collection = db.level0
collection.drop()
q01 ={
        "_id" : 1,
        "level" : "level0",
        "question" : "What does HTML stand for ?",
        "answer"   : "Hyper Text Markup Language",
        "option1" : "Hyper Text Markup Language",
        "option3" : "Home Tool Markup Language",
        "option2" : "Hyperlinks and Text Markup Language",
        "option4" : "None of these"

}
q02 ={
        "_id" : 2,
        "level" : "level0",
        "question" : "What is the HTML element to bold a text?",
        "answer"   : "<b>",
        "option1" : "<b>",
        "option3" : "<bold>",
        "option2" : "<wide>",
        "option4" : "<big>"

}
q03 ={
        "_id" : 3,
        "level" : "level0",
        "question" : "What does HTML stand for ?",
        "answer"   : "Hyper Text Markup Language",
        "option1" : "Hyper Text Markup Language",
        "option3" : "Home Tool Markup Language",
        "option2" : "Hyperlinks and Text Markup Language",
        "option4" : "None of these"

}
q04 ={
        "_id" : 4,
        "level" : "level0",
        "question" : "What is the correct HTML tag for a new paragraph?",
        "answer"   : "<p>",
        "option1" : "<para>",
        "option3" : "<paragraph>",
        "option2" : "<in>",
        "option4" : "<p>"

}
q05 ={
        "_id" : 5,
        "level" : "level0",
        "question" : "What property do you use to create spacing between HTML elements?",
        "answer"   : "margin",
        "option1" : "padding",
        "option3" : "margin",
        "option2" : "spacing",
        "option4" : "border"

}
q06 ={
        "_id" : 6,
        "level" : "level0",
        "question" : "For users that use the tab key to navigate websites, what property shows moving from one element to another using this behavior?",
        "answer"   : "a:visited",
        "option1" : "a:hover",
        "option3" : "a:visited",
        "option2" : "a:focus",
        "option4" : "a:link"

}
q07 ={
        "_id" : 7,
        "level" : "level0",
        "question" : "The acronym CSS stands for what?",
        "answer"   : "Cascading Style Sheets",
        "option1" : "Cascading Style Sheets",
        "option3" : "Carrot Sytem Style",
        "option2" : "Correlated Styling System",
        "option4" : "Canvas Styling System"

}
q08 ={
        "_id" : 8,
        "level" : "level0",
        "question" : "What property would you use to change the list style to show roman numerals instead of normal numbers?",
        "answer"   : "list-style-type:upper-roman;",
        "option1" : "list-style-type:upper-roman;",
        "option3" : "list-type:roman;",
        "option2" : "list-bullet-type:roman-numerals;",
        "option4" : "list-style:roman'"

}
q09 ={
        "_id" : 9,
        "level" : "level0",
        "question" : "What property can you use to set the spacing in between lines of text?",
        "answer"   : "line-height",
        "option1" : "line-spacing",
        "option3" : "line-height",
        "option2" : "spacing",
        "option4" : "letter-spacing"

}
q010 ={
        "_id" : 10,
        "level" : "level0",
        "question" : "What property do you use to set the background color of an image?",
        "answer"   : "background-color",
        "option1" : "color",
        "option3" : "background-color",
        "option2" : "background:color",
        "option4" : "color:background"

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

collection = db.level1
collection.drop()
q01 ={
        "_id" : 1,
        "level" : "level1",
        "question" : "What does PHP stand for?",
        "answer"   : "PHP: Hypertext Preprocessor",
        "option1" : "Processor Handling Program",
        "option3" : " Program Hypertext Preprocessor",
        "option2" : "PHP: Hypertext Preprocessor",
        "option4" : "None Of These"

}
q02 ={
        "_id" : 2,
        "level" : "level1",
        "question" : "Which extension is not a correct PHP file extension?",
        "answer"   : ".php",
        "option1" : ".phtml",
        "option3" : ".php",
        "option2" : ".php3",
        "option4" : ".phpRobert"

}
q03 ={
        "_id" : 3,
        "level" : "level1",
        "question" : " Which of the following is the way to create comments in PHP?",
        "answer"   : "/* commented code here */",
        "option1" : "// commented code to end of line",
        "option3" : "/* commented code here */",
        "option2" : "# commented code to end of line",
        "option4" : "all of the above"

}
q04 ={
        "_id" : 4,
        "level" : "level1",
        "question" : "Which of the following is used to declare a constant",
        "answer"   : "const",
        "option1" : "#pragma",
        "option3" : "constant",
        "option2" : "const",
        "option4" : "define"

}
q05 ={
        "_id" : 5,
        "level" : "level1",
        "question" : "The following are components of a database except ________ .",
        "answer"   : "reports",
        "option1" : "user data",
        "option3" : "metadata",
        "option2" : "reports",
        "option4" : "indexes"

}
q06 ={
        "_id" : 6,
        "level" : "level1",
        "question" : "SQL stands for ________ .",
        "answer"   : "Structured Query Language",
        "option1" : "Sequential Query Language",
        "option3" : "Structured Question Language",
        "option2" : "Structured Query Language",
        "option4" : "Sequential Question Language"

}
q07 ={
        "_id" : 7,
        "level" : "level1",
        "question" : "The command to remove rows from a table 'CUSTOMER' is:",
        "answer"   : "'DELETE FROM CUSTOMER WHERE'",
        "option1" : "REMOVE FROM CUSTOMER",
        "option3" : "DROP FROM CUSTOMER '",
        "option2" : "'DELETE FROM CUSTOMER WHERE'",
        "option4" : "'UPDATE FROM CUSTOMER' "

}
q08 ={
        "_id" : 8,
        "level" : "level1",
        "question" : "SQL data definition commands make up a(n) ________ .",
        "answer"   : "DDL",
        "option1" : "DDM",
        "option3" : "DDL",
        "option2" : "DAL",
        "option4" : "DCL"

}
q09 ={
        "_id" : 9,
        "level" : "level1",
        "question" : "Which of the following is valid SQL for an Index?",
        "answer"   : "CREATE INDEX ID",
        "option1" : "REMOVE INDEX ID",
        "option3" : "ADD INDEX ID;",
        "option2" : "CREATE INDEX ID;",
        "option4" : "CHANGE INDEX ID"

}
q010 ={
        "_id" : 10,
        "level" : "level1",
        "question" : "Which one of the following sorts rows in SQL?",
        "answer"   : "ORDER BY",
        "option1" : "SORT BY",
        "option3" : "ALIGN BY",
        "option2" : "ORDER BY",
        "option4" : "GROUP BY"

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