from pycparser import c_parser, c_ast, parse_file


def strcpy_func():
	print("hello")



class FuncVisitor(c_ast.NodeVisitor):
	def __init__(self):
		self.value = 0
		
		
	def visit_FuncCall(self, node):
		with open("sample.txt") as f:
			for line in f:
				line = line.strip()
				#print(node.name.name)
				#print(line)
				if str(node.name.name) == line:
					funcstr = node.name.name + "_func"
					#print(funcstr)
					eval('eval(funcstr)()')
					


if __name__ == "__main__":
	filename = "sample.c"
	ast = parse_file(filename)
	#ast.show()
	cv = FuncVisitor()
	cv.visit(ast)
