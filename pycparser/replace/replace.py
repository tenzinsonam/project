from pycparser import c_parser, c_ast, parse_file, c_generator
import linecache
from itertools import islice

dicto = {}
function = 'func.txt'




def replacVar(ast, par):
	for xname, x in ast.children():
		try:
			if x.name.startswith('param'):
				ind = int(x.name[5:])
				val = par[ind]
			else:
				replacVar(x, par)
		except AttributeError:
			replacVar(x, par)
		







def getFunc(lno):
	sta = lno[0]
	end = lno[2]
	lst = []
	for i in range(eval('int(sta)'), eval('int(end)+1')):
		line = (linecache.getline(function, i)).strip()
		lst.append(line)
		#print lst\
	stri = ''
	for l in lst:
		stri = stri + l
	strii = 'func(){' + stri + '}'
	temp = open('temp.c','w')
	temp.write(strii)
	temp.close()
	temmp = 'temp.c'
	ast = parse_file(temmp)
	#ast.show()
	stro = 'polowolo'
	#k = 'lo' in stro
	#print k
	#assert False
	return ast






def extract(lines):
	par = lines[0].strip()
	ide = lines[1].strip()
	lno = lines[2].strip()
	coo = lines[3].strip()
	ast = getFunc(lno)
	replacVar(ast, par)
	#par = eval('eval(nl[1])')
	#print coo
	assert False







if __name__ == '__main__':
	with open('temp.c', 'w'):
		pass
	with open('input.txt') as f:
		while True:
			lines = list(islice(f, 4))
			extract(lines)
			if not lines:
				break
