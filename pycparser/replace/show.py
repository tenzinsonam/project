from pycparser import c_parser, c_ast, parse_file, c_generator




def iterate(node):
	






filename = "temp.c"
ast = parse_file(filename)
ast.show()
