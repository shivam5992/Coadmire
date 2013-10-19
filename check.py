import random

A = []
Ques_id = random.randrange(1,5)
while Ques_id not in A:
	Ques_id = random.randrange(1,5)
	print(Ques_id)
	A.append(Ques_id)
print (A)