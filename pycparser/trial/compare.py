from pycparser import c_parser, c_ast, parse_file, c_generator
import linecache, pdb, os


pattern = 'sample.txt'
filename = "sample.c"
output = 'output.txt'
list1 = []
list2 = []
list3 = []
#paraml = []
dict = {'FuncCall': '2,4','Assignment': '9,99'}                        #update on change in sample.txt
						    #create output.txt file


#######################
'''



"((((((((()))))))))
'''


######################




def pattern_ast(lnum):
	line = (linecache.getline(pattern, lnum)).strip()
	line = "func(){" + line + "}"
	temp = open("temp.c","w")
	temp.write(line)
	temp.close()
	temp = "temp.c"
	bst = parse_file(temp)
	node = bst.ext[0].body.block_items[0]   #work
	#print(node)
	
	#assert False
	return node





def dfs_check(node,patt):
	for xname, x in node.children():
		list1.append(x)
	for yname, y in patt.children():
		list2.append(y)
	cls = "check__" + type(patt).__name__
	#print(cls)
	check = eval("eval(cls)(eval('node'),eval('patt'))")
	if check:
		del list1[0]
		del list2[0]
		if len(list1) != 0 and len(list2) != 0:
			val = dfs_check(list1[0],list2[0])
			#print(val)
			return val
		else:
			#print("h")
			return True
		
	else:
		return False
	
	'''
	
	if type(node).__name__ == type(patt).__name__ :
		#print(list1)
		cls = "check__" + type(node).__name__
		check = eval("eval(cls)(eval('node'),eval('patt'))")
		#print(cls)
		if check:
			del list1[0]
			del list2[0]
			#print (list1[1])
			#assert False
			if len(list1) != 0 and len(list2) != 0:
				val = dfs_check(list1[0],list2[0])
				return val
			else:
				return True
		else:
			False
	else:
		return False
	
	'''



def under_FuncCall(node):
	rnge = dict['Assignment']
	rnge = rnge.split(',')
	#print(rnge)
	for i in rnge:
		line = (linecache.getline(pattern, int(i))).strip()
		#print(node.name.name)
		if node.name.name == line:
			p_line = int(i)+1
			bst = pattern_ast(p_line)
			
			list1.append(node)
			list2.append(bst)
			val = dfs_check(node,bst)
			global list1, list2
			list1 = []
			list2 = []
			#print("The ans is "+ str(val))
			if val:
				stri = print_FuncCall(node)
				strin = str(i) + ":" + stri 
				#temp = open("output.txt","a")
				#temp.write(strin)
				#temp.close()
				#print(strin)
				#print(node.coord.line)
				return strin
			#else:
				#return 
	return "not"




#################################    print string


def print_FuncCall(node):
	name = print_ID(node.name)
	args = []
	param = ''
	for x in node.args.exprs:
		cls = type(x).__name__
		args.append(eval("eval('print_' + cls)(eval('x'))"))
	for x in args:
		param = param + x + ','
	param = param[:-1]
	stri = name + '(' + param + ')'
	#print(args)
	return stri





def print_ID(node):
	#print(node.name)
	return node.name




def print_BinaryOp(node):
	opr = node.op
	cls = type(node.left).__name__
	left = eval("eval('print_' + cls)(eval('node.left'))")
	cls = type(node.right).__name__
	right = eval("eval('print_' + cls)(eval('node.right'))")
	stri = str(left) + str(opr) + str(right)
	return stri
	
	
	
	
def print_UnaryOp(node):
	opr = node.op
	cls = type(node.expr).__name__
	#print(cls)
	typ = eval("eval('print_' + cls)(eval('node.expr'))")
	left = opr + '(' + typ + ')'
	return left
	#print(left)
	#assert False
	




def print_Typename(node):
	cls = type(node.type).__name__
	typ = eval("eval('print_' + cls)(eval('node.type'))")
	return typ
	
	
	

	
def print_TypeDecl(node):
	cls = type(node.type).__name__
	typ = eval("eval('print_' + cls)(eval('node.type'))")
	return typ
	
	
	
	
def print_IdentifierType(node):
	#cls = type(node.type).__name__
	typ = node.names
	return typ[0]


















###################################    check if matches

def check__FuncCall(node, patt):
	return True
	
	
	
def check__ID(node, patt):
	#print(list1)
	#print(patt.name)
	#if type(node).__name__ != FuncCall
	try:
		if node.name == patt.name or patt.name == "var":
			return True
		else:
			return False
	except:
		#print("nibba")
		if patt.name == "var":
			return True
		else:	
			
			return False
		
	
	''''
	if node.name == patt.name or patt.name == 'var':
		return True
	else: 
		return False
	'''


def check__ExprList(node, patt):
	if len(node.exprs) == len(patt.exprs):
		return True
	else: 
		return False
	
	'''
	
	#print(len(patt.exprs))
	if len(node.exprs) == len(patt.exprs):
		#print("ok")
		global list1, list2
		list1 = list1[0:1]
		list2 = list2[0:1]
		#print(list1)
		return True
	else:
		return False
	
	'''


def check__BinaryOp(node, patt):
	#print(node.op)
	#print(patt)
	if node.op == patt.op:
		return True
	else:
		return False
	


def check__UnaryOp(node, patt):
	if node.op == patt.op:
		return True
	else:
		return False




#################################       generate bst


def func_ExprList(node):
	return





def func_FuncCall(node):
	rnge = dict['FuncCall']
	rnge = rnge.split(',')
	#print(rnge)
	for i in rnge:
		line = (linecache.getline(pattern, int(i))).strip()
		#print(line)
		if node.name.name == line:
			p_line = int(i)+1
			bst = pattern_ast(p_line)
		###############	
			list1.append(node)
			list2.append(bst)
			val = dfs_check(node,bst)
			global list1, list2
			list1 = []
			list2 = []
			#print("The ans is "+ str(val))
			if val:
				stri = print_FuncCall(node)
				strin = str(node.coord.line) + ":" + str(i) + ":" + stri + ";\n"
				temp = open("output.txt","a")
				temp.write(strin)
				temp.close()
				#print(strin)
				#print(node.coord.line)
				
		
	return





def func_Assignment(node):
	vari = node.lvalue.name
	#print(node.lvalue.to_type)
	if type(node.rvalue).__name__ == 'Cast':
		typ = node.rvalue.to_type.type.type.type.names[0]
		#print('typ')
		if type(node.rvalue.expr).__name__ == 'FuncCall':
			stri = under_FuncCall(node.rvalue.expr)
			#print(stri)
			if stri != 'not':
				lst = stri.split(':')
				lne = lst[0]
				strii = lst[1]
				#print(stri)
				strin = str(node.coord.line) + ":" + lne + ':' + vari + "=(" + typ +"*)" + strii + ";\n"
				#print(strin)
				temp = open("output.txt","a")
				temp.write(strin)
				temp.close()		
			
	return





def func_BinaryOp(node):
	return






def func_If(node):
	return





def func_Compound(node):
	return





def func_IdentifierType(node):
	return





def func_TypeDecl(node):
	return





def func_ID(node):
	return





def func_ParamList(node):
	return





def func_FuncDecl(node):
	return




def func_Decl(node):
	return




def func_FuncDef(node):
	return

########################


def dfs(node):
	
	for xname, x in node.children():
		cls = type(x).__name__
		if cls in dict:
			func_cls = "func_" + cls
			eval("eval(func_cls)(eval('x'))")
			#print(cls)
		dfs(x)





if __name__ == "__main__":
	ast = parse_file(filename)
	#os.remove('output.txt')
	#ast.show()
	with open("output.txt","w"):
		pass

	dfs(ast)
