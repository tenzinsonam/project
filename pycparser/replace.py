from pycparser import c_parser, c_ast, parse_file, c_generator
import linecache, compare, os


output = "output.txt"				
sample = "sample.txt"
replace = "samplereplace.txt"


# create output2.txt
# sample.txt and samplereplace.txt should be similar


def pattern_ast(stri):
	#line = (linecache.getline(pattern, lnum)).strip()
	line = "func(){" + stri + "}"
	temp = open("temp.c","w")
	temp.write(line)
	temp.close()
	temp = "temp.c"
	bst = parse_file(temp)
	#node = bst.ext[0].body.block_items[0]   #work
	#print(node)
	
	#assert False
	return bst




def printFile(stri):
	temp = open("output2.txt","a")
	temp.write(stri)
	temp.close






####################################


def func_strcpy(node):
	fcall = node.ext[0].body.block_items[0]
	fcall.name.name = 'strncpy'
	newparam = c_ast.ID('??',fcall.coord)
	fcall.args.exprs.append(newparam)
	stri = compare.print_FuncCall(fcall)
	strin = stri + "\n"
	printFile(strin)
	
	


def func_nomnom(node):
	fcall = node.ext[0].body.block_items[0]
	fcall.name.name = 'nomnomnom'
	#newparam = c_ast.ID('??',fcall.coord)
	#fcall.args.exprs.append(newparam)
	stri = compare.print_FuncCall(fcall)
	strin = stri + "\n"
	printFile(strin)
	
	
	
	
def func_malloc(node):
	assert False





















####################################




def line_check():
	with open("output.txt") as f:
		lines = f.readlines()
	for line in lines:
		info = line.split(":")
		funct = linecache.getline(replace,int(info[1])).strip()
		stri = info[2][:-1]
		node = pattern_ast(stri)
		eval("eval(funct)(eval('node'))")
		print(funct)










if __name__ == "__main__":
	os.remove('output2.txt')
	line_check()
	

