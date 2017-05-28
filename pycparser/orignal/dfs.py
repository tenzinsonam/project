from pycparser import c_parser, c_ast, parse_file


dict = {'FuncCall': '4,7'}



def dfs(node):
	for xname, x in node.children():
		#print(x)
		if eval('type(x).__name__') in dict:
			print("done")

		dfs(x)





if __name__ == "__main__":
	#filenmae = "sample.c"
	filename = "sample.c"
	#ast = parse_file(filenmae)
	ast = parse_file(filename)
	#ast.show()
	dfs(ast)
	#nos = ast.ext[0].body
	#func(nos,bst)
