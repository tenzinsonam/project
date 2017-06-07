import sys





def search(ln,cl):
	global lst
	fd = open('sample.txt','r')
	lst = fd.readlines()
	for nu, lin in enumerate(lst):
		#print lin
		#assert False
		if nu % 2 == 1:
			lin = (lin.split('\n')[0]).split(',')
			if lin[0] == lin[2]:			
				if lin[0] == ln and lin[1] <= cl and lin[3] >= cl:
					return nu
			else:
				if lin[0] == ln and lin[1] <= cl:
					return nu
				if lin[2] == ln and lin[3] >= cl:
					return nu
				if lin[0] < ln and lin[2] > ln:
					return nu
	return None



if __name__ == '__main__':
	ln = sys.argv[1]
	cl = sys.argv[2]
	#lst = []
	val = search(ln, cl)
	if val == None:
		assert False
	else:
		lin = ((lst[val]).split('\n')[0]).split(',')
		print lin
		l1 = lin[0]
		c1 = lin[1]
		l1 = lin[2]
		c2 = lin[3]
	
	'''
	fd = open('sample.txt','r')
	lst = fd.readlines()
	if 'ccc\n' in lst:
		ind = lst.index('ccc\n')
		lst[ind] = 'cc\n'
	fd.close()
	fd = open('sample.txt','w')
	fd.write(''.join(lst))
	#print lst
	'''
