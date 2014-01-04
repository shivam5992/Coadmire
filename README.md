CoadMire
========

**About**

Coadmire is an online test platform developed and designed espically to give a better experince to both users and admins.
It supports the feature of adaptability ie. dynamic level transitions while the test is in progress.
It adapts according to the examinee's ability level. 
It selects questions for the purpose of maximizing the precision of the exam based on what is known about the examinee 
from previous questions. 
From the examinee's perspective, the difficulty of the exam seems to tailor itself to his or her level of ability
Current levels are displayed interactivly on the test screen.

**Backend**

Codemire test starts from basic level and progress according to the responses submitted by the user.
With every correct response, level increases by one and with every wrong a answer, level decreases by one.
All the responses are smartly captured in the database.

**Instructions to initiate the project**

1. Install pymongo using command: 
	
	pip install pymongo

2. Before runnig the script, create a local server of mongoDb on your PC.
	
	mongod --dbpath /path/

3. Run the script question_data.py to laod the mongodb database with 100 documents of questions, answers and options.

	python question_data.py

4. Run the router.py script and check out the page in web browser.
	
	python router.py