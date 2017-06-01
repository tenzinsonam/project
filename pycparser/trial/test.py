from pycparser import c_parser, c_ast, parse_file, c_generator
import linecache


dicto = {'FuncCall': '2,99','Assignment': '8,99'}
#intr = ['call_ID']
filename = 'sample.c'
pattern = 'sample.txt'
list1 = []
list2 = []
#bfs = []


#bst refer to the node in pattern
#ast refers to the node in ast orignal

##########################


def print_FuncCall(ast):
	name = print_ID(ast.name)
	param = ''
	args = []
	wst = ast.args.exprs
	#print wst
	#assert False
	for x in wst:
		cls = type(x).__name__
		args.append(eval("eval('print_' + cls)(eval('x'))"))
	for x in args:
		param = param + x + ','
	param = param[:-1]
	stri = name + '(' + param + ')'
	#print(args)
	return stri
	






def print_ID(ast):
	return ast.name











#################################### type defined is that of bst and these functions call the print 
#################################### functions as per thetype of ast




def call_ID(ast, bst, lst):
	#print lst
	if bst.name in lst:
		cls = 'print_' + type(ast).__name__
		stri = eval("eval(cls)(eval('ast'))")
		return stri
	else:
		return 'NULL'



def call_FuncCall(ast, bst, lst):
	return 'NULL'
	
	

def call_ExprList(ast, bst, lst):
	return 'NULL'
	
	
	
def call_Assignment(ast, bst, lst):
	return 'NULL'



def call_Cast(ast, bst, lst):
	return 'NULL'



def call_Typename(ast, bst, lst):
	return 'NULL'




def call_PtrDecl(ast, bst, lst):
	return 'NULL'



def call_TypeDecl(ast, bst, lst):
	return 'NULL'



def call_IdentifierType(ast, bst, lst):
	if bst.names[0] in lst:
		#print('hello')
		return bst.names[0]
		
	#print(type(bst.names).__name__)
	#assert False
	else:
		return 'NULL'



def call_BinaryOp(ast, bst, lst):
	#print list2
	return 'NULL'



def call_UnaryOp(ast, bst, lst):
	return 'NULL'






############################################ main funcion for type mentioned in dicto. checks the 
############################################ defining conditions in sample.txt



def func_FuncCall(node):
	#print(node)
	rnge = dicto['FuncCall']
	rnge = rnge.split(',')
	cls = type(node).__name__
	#print(rnge)
	for i in rnge:
		line = (linecache.getline(pattern, int(i))).strip()
		#print(line)
		if node.name.name == line:
			p_line = int(i)+1
			args = (linecache.getline(pattern, int(i)+2)).strip()
			lst = eval(args)
			#print(lst['v0'])
			bst = pattern_ast(p_line,cls)
			#print(cls)
			#assert False
			list1.append(node)
			list2.append(bst)
			dfs_check(node, bst, lst)
			global list1, list2
			list1 = []
			list2 = []
			return lst
	
			


def func_Assignment(node):
	rnge = dicto['Assignment']
	rnge = rnge.split(',')
	cls = type(node).__name__
	temp = []
	getList(temp, node)
	intr = getNode(temp, 'FuncCall')
	#if(type(intr).__name__ == 'NoneType'):
		#return
		
	for i in rnge:
		line = (linecache.getline(pattern, int(i))).strip()
		#print line
		try:
			if intr.name.name == line :
				p_line = int(i) + 1
				args = (linecache.getline(pattern, int(i)+2)).strip()
				lst = eval(args)
				bst = pattern_ast(p_line,cls)
				#print node
				list1.append(node)
				list2.append(bst)
				dfs_check(node, bst, lst)
				global list1, list2
				list1 = []
				list2 = []
				return lst
		except AttributeError:
			return
	



def func_Decl(node):
	rnge = dicto['Assignment']
	rnge = rnge.split(',')
	cls = type(node).__name__
	temp = []
	getList(temp, node)
	intr = getNode(temp, 'FuncCall')
	for i in rnge:
		line = (linecache.getline(pattern, int(i))).strip()
		#print line
		try:
			if intr.name.name == line :
				p_line = int(i) + 1
				args = (linecache.getline(pattern, int(i)+2)).strip()
				lst = eval(args)
				bst = pattern_ast(p_line,cls)
				#print node
				list1.append(node)
				list2.append(bst)
				dfs_check(node, bst, lst)
				global list1, list2
				list1 = []
				list2 = []
				return lst
		except AttributeError:
			return
				
	










########################################### creates the list of types to go through and updates the 
########################################### individual dictionaries of the types



def dfs_check(ast, bst, lst):
	del list1[0]
	del list2[0]
	cls = 'call_' + type(bst).__name__
	#print(cls)
	val = eval("eval(cls)(eval('ast'),eval('bst'),eval('lst'))")
	#print(val)
	if val=='NULL':
		for xname, x in ast.children():
			list1.append(x)
		for yname, y in bst.children():
			list2.append(y)
		#if(type(ast).__name__=='BinaryOp'):
			#print list1[-1]
	else:
		try:							#### important
			lst[bst.names[0]] = val
		except AttributeError:
			lst[bst.name] = val
		
		
		#print lst
	if list1 != [] and list2 != []:
	
		dfs_check(list1[0], list2[0], lst)	
	






def getNode(bfs, cls):
	for x in bfs:
		if type(x).__name__ == cls:
			return x
	
		
	

def getList(bfs, bst):
	for xname, x in bst.children():
		bfs.append(x)
		getList(bfs, x)





def pattern_ast(lnum, cls):
	line = (linecache.getline(pattern, lnum)).strip()
	#print(line)
	bfs = []
	line = "func(){" + line + "}"
	temp = open("temp.c","w")
	temp.write(line)
	temp.close()
	temp = "temp.c"
	bst = parse_file(temp)
	bfs.append(bst)
	getList(bfs, bst)
	node = getNode(bfs, cls)
	#print nope
	
	#print(bst)
	#nope = getNode(bfs, cls)
	#node = bst.ext[0].body.block_items[0]
	#print(node)
	#assert False
	return node






def dfs(node):
	for xname, x in node.children():
		cls = type(x).__name__
		#print x
		if cls in dicto:
			func_cls = "func_" + cls
			lst = eval("eval(func_cls)(eval('x'))")
			#print()
			if type(lst).__name__ != 'NoneType':
				print lst
			
			
		dfs(x)

	







if __name__ == '__main__':
	ast = parse_file(filename)
	dfs(ast)
