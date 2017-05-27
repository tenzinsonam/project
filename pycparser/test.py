from pycparser import c_parser, c_ast, parse_file, c_generator

filename = "sample.c"
ast = parse_file(filename)
#print(ast.ext[0].body.block_items[1].args.exprs)
ast.show()
