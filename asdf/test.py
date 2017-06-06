import random
f = open('nibba.txt','w')
strx=''
for i in xrange(5):
    strx+=str(random.randint(1,9))+","+str(random.randint(1,9))+","+str(random.randint(1,9))+","+str(random.randint(1,9))+"\n"
f.write(strx)
f.close()
