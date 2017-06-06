import re, linecache


sample = 'sample.txt'
code = 'sample.c'






def parStk(lst):
	i = 1
	fl = open(code,'r')
	stk = 0
	while i < lst[0]:			##try fixing
		line = fl.readlines()
	while i <= lst[2]:
		line = fl.readlines()
		if '{' in line:
			k = line.count('{')
			stk =+ k
		if '}' in line:
			k = line.count('{')
			stk =- k
		if stk == 0:
			wst = []
			for ind,cha in enumerate(line):
				if cha == '}':
					ws.append(ind)
			return wst[-1]





def checkParn(lst):
	l1 = lst[0]
	lne = (linecache.getine(code,l1)).strip()
	if '{' in lne:
		return True
	else:
		return False




if __name__ == '__main__':
	line = ((linecache.getline(sample,4)).strip()).split(',')
	while(line != ''):
		chk = checkParn(line)
		if chk:
			col = parStk(line)
		else:
			
		'''
		l1 = line[0]
		c1 = line[1]
		l2 = line[2]
		c2 = line[3]
		stri = 'this{ string has {'
		wst = []
		for i,c in enumerate(stri):
			if c == '{':
				wst.append(i)
		print wst[-1]
		'''
		lne = (linecache.getline(code,l2)).strip()
		#c11 = re.match()
		assert False


