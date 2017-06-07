import random

stri = ''
for i in range(10):
	if i%2 == 0:
		stri += str(random.randint(0,9)) + '\n'
	if i %2 == 1:
		stri += str(random.randint(0,9))+","+str(random.randint(0,9))+","+str(random.randint(0,9))+","+str(random.randint(0,9))+"\n"
fs = open('sample.txt','w')
fs.write(stri)
fs.close()
