from pymongo import MongoClient
import codecs

client = MongoClient()
db = client.coadmire

collection = db.level1
collection.drop()
q01 ={
        "_id" : 1,
        "level" : "level1",
        "question" : "What does HTML stand for ?",
        "answer"   : "Hyper Text Markup Language",
        "option1" : "Hyper Text Markup Language",
        "option3" : "Home Tool Markup Language",
        "option2" : "Hyperlinks and Text Markup Language",
        "option4" : "None of these"

}
q02 ={
        "_id" : 2,
        "level" : "level1",
        "question" : "What is the HTML element to bold a text?",
        "answer"   : "<b>",
        "option1" : "<b>",
        "option3" : "<bold>",
        "option2" : "<wide>",
        "option4" : "<big>"

}
q03 ={
        "_id" : 3,
        "level" : "level1",
        "question" : "What does HTML stand for ?",
        "answer"   : "Hyper Text Markup Language",
        "option1" : "Hyper Text Markup Language",
        "option3" : "Home Tool Markup Language",
        "option2" : "Hyperlinks and Text Markup Language",
        "option4" : "None of these"

}
q04 ={
        "_id" : 4,
        "level" : "level1",
        "question" : "What is the correct HTML tag for a new paragraph?",
        "answer"   : "<p>",
        "option1" : "<para>",
        "option3" : "<paragraph>",
        "option2" : "<in>",
        "option4" : "<p>"

}
q05 ={
        "_id" : 5,
        "level" : "level1",
        "question" : "What property do you use to create spacing between HTML elements?",
        "answer"   : "margin",
        "option1" : "padding",
        "option3" : "margin",
        "option2" : "spacing",
        "option4" : "border"

}
q06 ={
        "_id" : 6,
        "level" : "level1",
        "question" : "For users that use the tab key to navigate websites, what property shows moving from one element to another using this behavior?",
        "answer"   : "a:visited",
        "option1" : "a:hover",
        "option3" : "a:visited",
        "option2" : "a:focus",
        "option4" : "a:link"

}
q07 ={
        "_id" : 7,
        "level" : "level1",
        "question" : "The acronym CSS stands for what?",
        "answer"   : "Cascading Style Sheets",
        "option1" : "Cascading Style Sheets",
        "option3" : "Carrot Sytem Style",
        "option2" : "Correlated Styling System",
        "option4" : "Canvas Styling System"

}
q08 ={
        "_id" : 8,
        "level" : "level1",
        "question" : "What property would you use to change the list style to show roman numerals instead of normal numbers?",
        "answer"   : "list-style-type:upper-roman;",
        "option1" : "list-style-type:upper-roman;",
        "option3" : "list-type:roman;",
        "option2" : "list-bullet-type:roman-numerals;",
        "option4" : "list-style:roman'"

}
q09 ={
        "_id" : 9,
        "level" : "level1",
        "question" : "What property can you use to set the spacing in between lines of text?",
        "answer"   : "line-height",
        "option1" : "line-spacing",
        "option3" : "line-height",
        "option2" : "spacing",
        "option4" : "letter-spacing"

}
q010 ={
        "_id" : 10,
        "level" : "level1",
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

collection = db.level2
collection.drop()
q01 ={
        "_id" : 1,
        "level" : "level2",
        "question" : "What does PHP stand for?",
        "answer"   : "PHP: Hypertext Preprocessor",
        "option1" : "Processor Handling Program",
        "option3" : " Program Hypertext Preprocessor",
        "option2" : "PHP: Hypertext Preprocessor",
        "option4" : "None Of These"

}
q02 ={
        "_id" : 2,
        "level" : "level2",
        "question" : "Which extension is not a correct PHP file extension?",
        "answer"   : ".php",
        "option1" : ".phtml",
        "option3" : ".php",
        "option2" : ".php3",
        "option4" : ".phpRobert"

}
q03 ={
        "_id" : 3,
        "level" : "level2",
        "question" : " Which of the following is the way to create comments in PHP?",
        "answer"   : "/* commented code here */",
        "option1" : "// commented code to end of line",
        "option3" : "/* commented code here */",
        "option2" : "# commented code to end of line",
        "option4" : "all of the above"

}
q04 ={
        "_id" : 4,
        "level" : "level2",
        "question" : "Which of the following is used to declare a constant",
        "answer"   : "const",
        "option1" : "#pragma",
        "option3" : "constant",
        "option2" : "const",
        "option4" : "define"

}
q05 ={
        "_id" : 5,
        "level" : "level2",
        "question" : "The following are components of a database except ________ .",
        "answer"   : "reports",
        "option1" : "user data",
        "option3" : "metadata",
        "option2" : "reports",
        "option4" : "indexes"

}
q06 ={
        "_id" : 6,
        "level" : "level2",
        "question" : "SQL stands for ________ .",
        "answer"   : "Structured Query Language",
        "option1" : "Sequential Query Language",
        "option3" : "Structured Question Language",
        "option2" : "Structured Query Language",
        "option4" : "Sequential Question Language"

}
q07 ={
        "_id" : 7,
        "level" : "level2",
        "question" : "The command to remove rows from a table 'CUSTOMER' is:",
        "answer"   : "'DELETE FROM CUSTOMER WHERE'",
        "option1" : "REMOVE FROM CUSTOMER",
        "option3" : "DROP FROM CUSTOMER '",
        "option2" : "'DELETE FROM CUSTOMER WHERE'",
        "option4" : "'UPDATE FROM CUSTOMER' "

}
q08 ={
        "_id" : 8,
        "level" : "level2",
        "question" : "SQL data definition commands make up a(n) ________ .",
        "answer"   : "DDL",
        "option1" : "DDM",
        "option3" : "DDL",
        "option2" : "DAL",
        "option4" : "DCL"

}
q09 ={
        "_id" : 9,
        "level" : "level2",
        "question" : "Which of the following is valid SQL for an Index?",
        "answer"   : "CREATE INDEX ID",
        "option1" : "REMOVE INDEX ID",
        "option3" : "ADD INDEX ID;",
        "option2" : "CREATE INDEX ID;",
        "option4" : "CHANGE INDEX ID"

}
q010 ={
        "_id" : 10,
        "level" : "level2",
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

collection = db.level3
collection.drop()
q01 ={
        "_id" : 1,
        "level" : "level3",
        "question" : "Which is a reserved word in the Java programming language?",
        "answer"   : "native",
        "option1" : "subclasses",
        "option3" : "native",
        "option2" : "method",
        "option4" : "reference"

}
q02 ={
        "_id" : 2,
        "level" : "level3",
        "question" : "Which is a valid keyword in java?",
        "answer"   : "interface",
        "option1" : "string",
        "option3" : "float",
        "option2" : "interface",
        "option4" : "unsigned"

}
q03 ={
        "_id" : 3,
        "level" : "level3",
        "question" : "Which one of the following will declare an array and initialize it with five numbers?",
        "answer"   : "int [] a = {23,22,21,20,19};",
        "option1" : "Array a = new Array(5);",
        "option3" : "int [] a = {23,22,21,20,19};",
        "option2" : "int a [] = new int[5];",
        "option4" : "int [5] array;"

}
q04 ={
        "_id" : 4,
        "level" : "level3",
        "question" : "What is the most restrictive access modifier that will allow members of one class to have access to members of another class in the same package?",
        "answer"   : "default access",
        "option1" : "public",
        "option3" : "protected",
        "option2" : "abstract",
        "option4" : "default access"

}
q05 ={
        "_id" : 5,
        "level" : "level3",
        "question" : "Which is the valid declarations within an interface definition?",
        "answer"   : "public double methoda();",
        "option1" : "public final double methoda();",
        "option3" : "static void methoda(double d1);",
        "option2" : "protected void methoda(double d1);",
        "option4" : "public double methoda();"

}
q06 ={
        "_id" : 6,
        "level" : "level3",
        "question" : "Which one is a valid declaration of a boolean?",
        "answer"   : "boolean b3 = false;",
        "option1" : "boolean b1 = 0;",
        "option3" : "boolean b2 = 'false';",
        "option2" : "boolean b3 = false;",
        "option4" : "boolean b4 = Boolean.false();"

}
q07 ={
        "_id" : 7,
        "level" : "level3",
        "question" : "Which is a valid declarations of a String?",
        "answer"   : "String s1 = null;",
        "option1" : "String s2 = 'null';",
        "option3" : "String s3 = (String) 'abc';",
        "option2" : "String s1 = null;",
        "option4" : "String s4 = (String) '\ufeed';"

}
q08 ={
        "_id" : 8,
        "level" : "level3",
        "question" : "What is the numerical range of a char?",
        "answer"   : "0 to 65535",
        "option1" : "-128 to 127",
        "option3" : "0 to 32767",
        "option2" : "-(215) to (215) - 1",
        "option4" : "0 to 65535"

}
q09 ={
        "_id" : 9,
        "level" : "level3",
        "question" : "You want subclasses in any package to have access to members of a superclass. Which is the most restrictive access that accomplishes this objective?",
        "answer"   : "protected",
        "option1" : "public",
        "option3" : "protected",
        "option2" : "transient",
        "option4" : "private"

}
q010 ={
        "_id" : 10,
        "level" : "level3",
        "question" : "What is the prototype of the default constructor?",
        "answer"   : "public Test( )",
        "option1" : "Test( )",
        "option3" : "public Test( )",
        "option2" : "public Test(void)",
        "option4" : "Test(void)"

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

collection = db.level4
collection.drop()
q1 ={
        "_id" : 1,
        "level" : "level4",
        "question" : "Which of the following function is more appropriate for reading in a multi-word string?",
        "answer"   : "get()",
        "option1" : "printf()",
        "option3" : "scanf()",
        "option2" : "gets()",
        "option4" : "puts()"
}

q2 ={
        "_id" : 2,
        "level" : "level4",
        "question" : "Which bitwise operator is suitable for checking whether a particular bit is on or off?",
        "answer"   : "& operator",
        "option1" : "&& operator",
        "option3" : "& operator",
        "option2" : "|| operator",
        "option4" : "! operator"
}

q3 ={
        "_id" : 3,
        "level" : "level4",
        "question" : "The keyword used to transfer control from a function back to the calling function is",
        "answer"   : "return",
        "option1" : "go back",
        "option3" : "goto",
        "option2" : "switch",
        "option4" : "return"
}

q4 ={
        "_id" : 4,
        "level" : "level4",
        "question" : "The library function used to find the last occurrence of a character in a string is",
        "answer"   : "strrchr()",
        "option1" : "strnstr()",
        "option3" : "laststr()",
        "option2" : "strrchr()",
        "option4" : "strstr()"
}

q5 ={
        "_id" : 5,
        "level" : "level4",
        "question" : "How will you free the allocated memory ?",
        "answer"   : "free(var-name)",
        "option1" : "remove(var-name)",
        "option3" : "free(var-name)",
        "option2" : "dalloc(var-name)",
        "option4" : "delete(var-name)"
}

q6 ={
        "_id" : 6,
        "level" : "level4",
        "question" : "Which one of the following provides conceptual support for function calls? ",
        "answer"   : "The system stack",
        "option1" : "The heap ",
        "option3" : "The processor's registers ",
        "option2" : "The system stack",
        "option4" : "The data segment "
}

q7 ={
        "_id" : 7,
        "level" : "level4",
        "question" : "Which one of the following is NOT a valid C identifier? ",
        "answer"   : "1___",
        "option1" : "___S",
        "option3" : "1___",
        "option2" : "___1",
        "option4" : "___ "
}

q8 ={
        "_id" : 8,
        "level" : "level4",
        "question" : " What is the advantage of #define over const?",
        "answer"   : "Data type is flexible",
        "option1" : "Data type is flexible",
        "option3" : "  Can have a pointe",
        "option2" : "Reduction in the size of the program",
        "option4" : " Both (a) and (c)"
}

q9 ={
        "_id" : 9,
        "level" : "level4",
        "question" : " Memory allocation using malloc() is done in?",
        "answer"   : "Heap area",
        "option1" : "Static area",
        "option3" : " Stack area",
        "option2" : "Heap area",
        "option4" : "Both b & c"
}

q10 ={
        "_id" : 10,
        "level" : "level4",
        "question" : " Memory allocation is done using ?",
        "answer"   : "malloc",
        "option1" : "function",
        "option3" : "array",
        "option2" : "pointer",
        "option4" : "none of these"
}

collection.insert(q1)
collection.insert(q2)
collection.insert(q3)
collection.insert(q4)
collection.insert(q5)
collection.insert(q6)
collection.insert(q7)
collection.insert(q8)
collection.insert(q9)
collection.insert(q10)

collection = db.level5xxxxxxxxxxxxx
collection.drop()

q1 ={
        "_id" : 1,
        "level" : "level5",
        "question" : "Which of the following type of class allows only one object of it to be created?",
        "answer"   : "Singleton class",
        "option1" : "Virtual class",
        "option3" : "Abstract class",
        "option2" : "Singleton class",
        "option4" : "Friend class"
}

q2 ={
        "_id" : 2,
        "level" : "level5",
        "question" : "Which of the following is not a type of constructor?",
        "answer"   : "Friend constructor",
        "option1" : "Copy constructor",
        "option3" : "Friend constructor",
        "option2" : "Default constructor",
        "option4" : "Parameterized constructor"
}

q3 ={
        "_id" : 3,
        "level" : "level5",
        "question" : "cout is a/an __________ ",
        "answer"   : "object",
        "option1" : "function",
        "option3" : "object",
        "option2" : "macro",
        "option4" : "operator"
}

q4 ={
        "_id" : 4,
        "level" : "level5",
        "question" : "Which of the following concepts of OOPS means exposing only necessary information to client?",
        "answer"   : "Data hiding",
        "option1" : "Encapsulation",
        "option3" : "Data binding",
        "option2" : "Data hiding",
        "option4" : "Abstraction"
}

q5 ={
        "_id" : 5,
        "level" : "level5",
        "question" : "Which of the following cannot be friend?",
        "answer"   : "Object",
        "option1" : "Function",
        "option3" : "Class",
        "option2" : "Object",
        "option4" : "Operator function"
}

q6 ={
        "_id" : 6,
        "level" : "level5",
        "question" : "How many instances of an abstract class can be created?",
        "answer"   : "0",
        "option1" : "1",
        "option3" : "0",
        "option2" : "5",
        "option4" : "13"
}

q7 ={
        "_id" : 7,
        "level" : "level5",
        "question" : "Which of the following term is used for a function defined inside a class?",
        "answer"   : "Member function",
        "option1" : "Member Variable",
        "option3" : "Member function",
        "option2" : "Class function",
        "option4" : "Classic function"
}

q8 ={
        "_id" : 8,
        "level" : "level5",
        "question" : "How many types of polymorphisms are supported by C++?",
        "answer"   : "2",
        "option1" : "1",
        "option3" : "2",
        "option2" : "3",
        "option4" : "4"
}

q9 ={
        "_id" : 9,
        "level" : "level5",
        "question" : "Which of the following concepts means determining at runtime what method to invoke?",
        "answer"   : "Dynamic binding",
        "option1" : "Data hiding",
        "option3" : "Dynamic Typing",
        "option2" : "Dynamic loading",
        "option4" : "Dynamic binding"
}

q10 ={
        "_id" : 10,
        "level" : "level5",
        "question" : "Which of the following is not the member of class?",
        "answer"   : "Friend function",
        "option1" : "Const function",
        "option3" : "Friend function",
        "option2" : "Static function",
        "option4" : "Virtual function"
}

collection.insert(q1)
collection.insert(q2)
collection.insert(q3)
collection.insert(q4)
collection.insert(q5)
collection.insert(q6)
collection.insert(q7)
collection.insert(q8)
collection.insert(q9)
collection.insert(q10)

collection = db.level6
collection.drop()

q1 ={
        "_id" : 1,
        "level" : "level6",
        "question" : "Interprocess communication?",
        "answer"   : "allows processes to synchronize activity",
        "option1" : "allows processes to synchronize activity",
        "option3" : "is usually done via disk drives",
        "option2" : "is required for all processes",
        "option4" : "is never necessary"

}



q2 ={
        "_id" : 2,
        "level" : "level6",
        "question" : "The part of machine level instruction, which tells the central processor what has to be done, is?",
        "answer"   : "Operation code",
        "option1" : "Locator",
        "option3" : "Flip-Flop",
        "option2" : "Address",
        "option4" : "Operation code"
}

q3 ={
        "_id" : 3,
        "level" : "level6",
        "question" : "Which of the following refers to the associative memory?",
        "answer"   : "there is no need for an address i.e. the data is used as an address",
        "option1" : "the data are accessed sequentially",
        "option3" : "there is no need for an address i.e. the data is used as an address",
        "option2" : "the address of the data is supplied by the users",
        "option4" : "the address of the data is generated by the CPU"
}

q4 ={
        "_id" : 4,
        "level" : "level6",
        "question" : "To avoid the race condition, the number of processes that may be simultaneously inside their critical section is",
        "answer"   : "1",
        "option1" : "16",
        "option3" : "0",
        "option2" : "8",
        "option4" : "1"
}

q5 ={
        "_id" : 5,
        "level" : "level6",
        "question" : "Process is",
        "answer"   : "a program in execution",
        "option1" : "a job in secondary memory",
        "option3" : "a program in execution",
        "option2" : "program in High level language kept on disk",
        "option4" : "contents of main memory"
}

q6 ={
        "_id" : 6,
        "level" : "level6",
        "question" : "Which of the following systems software does the job of merging the records from two files into one?",
        "answer"   : "Utility program",
        "option1" : "Networking software",
        "option3" : "Utility program",
        "option2" : "Security software",
        "option4" : "None of the above"
}

q7 ={
        "_id" : 7,
        "level" : "level6",
        "question" : "Fork is",
        "answer"   : "the creation of a new process",
        "option1" : "the creation of a new process",
        "option3" : "the dispatching of a task",
        "option2" : "the creation of a new job",
        "option4" : "None of the above"
}

q8 ={
        "_id" : 8,
        "level" : "level6",
        "question" : "Thrashing",
        "answer"   : "can be caused by poor paging algorithms",
        "option1" : "always occurs on large computers",
        "option3" : "can always be avoided by swapping",
        "option2" : "is a natural consequence of virtual memory systems",
        "option4" : "can be caused by poor paging algorithms"
}

q9 ={
        "_id" : 9,
        "level" : "level6",
        "question" : "Which of the following instruction steps, would be written within the diamond-shaped box, of a flowchart?",
        "answer"   : "IS A<10",
        "option1" : "S = B - C",
        "option3" : "IS A<10",
        "option2" : "PRINT A",
        "option4" : "DATA X,4Z"
}

q10 ={
        "_id" : 10,
        "level" : "level6",
        "question" : "Supervisor state is",
        "answer"   : "only allowed to the operating system",
        "option1" : "entered by programs when they enter the processor",
        "option3" : "never used",
        "option2" : "only allowed to the operating system",
        "option4" : "required to perform any I/O"
}

collection.insert(q1)
collection.insert(q2)
collection.insert(q3)
collection.insert(q4)
collection.insert(q5)
collection.insert(q6)
collection.insert(q7)
collection.insert(q8)
collection.insert(q9)
collection.insert(q10)