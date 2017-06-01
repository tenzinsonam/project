from pycparser import c_parser, c_ast, parse_file, c_generator

filename = "sample.c"
ast = parse_file(filename)
ast.show()
