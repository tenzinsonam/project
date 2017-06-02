from pycparser import c_parser, c_ast, parse_file, c_generator
import linecache
from itertools import islice

dicto = {}
function = 'func.txt'
tempc = 'temp.c'
global cou




def changeIdentifier(node, lst):	#change identifier type
	for xname, x in node.children():
		if type(x).__name__ == 'IdentifierType':
			x.names[0] = lst[int(cou)+1]
		changeIdentifier(x, lst)







def addPointer(node, val):		#adds the pointer as per the value of val
	#print 'hello'
	ori = node
	#sub = node.type
	val = int(val)
	for i in xrange(val):
		ori.type = c_ast.PtrDecl([],None)
		ori = ori.type
		#print(ori)
	#node.show()
	#assert False
	return ori




def delPointer(node):			#delete instances of PteDecl
	x = node.type
	y = node.type
	if type(x).__name__ == 'PtrDecl':
		y = delPointer(x)
	return y




def pointerAssign(ast, ide):		#main PtrDecl handlin function
	for xname, x in ast.children():
		if type(x).__name__ == 'PtrDecl':
			sub = delPointer(ast)
			#ast.type = sub
			#ast.show()
			#print ide[cou]
			upw = addPointer(ast, ide[cou])
			#sub.type.names[0] = ide[int(cou)+1]
			#sub.show()
			#assert False
			changeIdentifier(sub, ide)
			upw.type = sub
			global cou
			cou = cou + 2
			#sub.show()
			#ast.show()
		else:
			pointerAssign(x, ide)



def printChange(node, lno):		# prints the final output in a list
	#sta = lno[0]
	#end = lno[2]
	ran = int(lno[2])- int(lno[0]) + 1
	lst = []
	generator = c_generator.CGenerator()
	stri = generator.visit(node)
	temp = open('temp.c','r+')
	temp.write(stri)
	temp.close()
	for i in range(3, 3+ran):
		line = (linecache.getline(tempc, i)).strip()
		lst.append(line)
	return lst
	#assert False



def replacVar(ast, par):		#replaces variable with the values given
	for xname, x in ast.children():
		try:
			if x.name.startswith('param'):
				ind = int(x.name[5:])
				val = par[ind]
				#print val
				x.name = val
			replacVar(x, par)
		except AttributeError:
			replacVar(x, par)
		







def getFunc(lno):			#generates ast for the replacement function
	sta = lno[0]
	end = lno[2]
	lst = []
	for i in range(eval('int(sta)'), eval('int(end)+1')):
		line = (linecache.getline(function, i)).strip()
		lst.append(line)	
	stri = ''
	for l in lst:
		stri = stri + l
	strii = 'func(){' + stri + '}'
	#print strii
	temp = open('temp.c','w')
	temp.write(strii)
	temp.close()
	temmp = 'temp.c'
	ast = parse_file(temmp)
	#ast.show()
	#stro = 'polowolo'
	#k = 'lo' in stro
	#print k
	#assert False
	return ast






def extract(lines):			#extract the information from the set of four lines
	
	if lines == [] or lines == '\n':
		return
	#print lines
	para = lines[0].strip()
	par = eval(para)
	idee = lines[1].strip()
	ide = eval(idee)
	lno = lines[2].strip()
	coo = lines[3].strip()
	global cou 
	cou = 0
	ast = getFunc(lno)
	#print ide[1]
	#assert False
	replacVar(ast, par)
	if ide!=[]:
		#print 'hello'
		pointerAssign(ast, ide)
	#par = eval('eval(nl[1])')
	out = printChange(ast, lno)
	print out
	assert False







if __name__ == '__main__':
	with open('temp.c', 'w'):
		pass
	with open('input.txt') as f:
		while True:
			lines = list(islice(f, 4))
			#print lines
			extract(lines)
			if not lines:
				break
