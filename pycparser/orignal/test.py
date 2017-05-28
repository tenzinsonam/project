from pycparser import c_parser, c_ast, parse_file, c_generator


ast = parse_file("test.c")
ast.show()
