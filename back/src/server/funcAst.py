#!/usr/bin/env python3
import ast, json, sys

class FuncLister(ast.NodeVisitor):
	def visit_FunctionDef(self, node):
		args = []
		for arg in node.args.args:
			args.append(arg.arg)
		print(json.dumps({'Name':node.name, 'Params':args}, indent=4))
		self.generic_visit(node) # guarantee child nodes visited

def topLevel(tree, Url, Filename):
	funcs = []
	classes = []
	for node in tree.body:
		if isinstance(node, ast.FunctionDef):
			args = []
			for arg in node.args.args:
				args.append({'Name':arg.arg, 'Type':None})
			funcs.append({'Name':node.name, 'Params':args})
		elif isinstance(node, ast.ClassDef):
			classes.append({'Name':node.name, 'TypeStr':''})
	print(json.dumps({'Url':Url, 'Filename':Filename, 'ExportedFuncs':funcs, 'ExportedTypes':classes}, indent=4))

# FuncLister().visit(tree)

Url, Filename = sys.argv[1], sys.argv[2]

s = ''
for line in sys.stdin:
	s += line

tree = ast.parse(s)
topLevel(tree, Url, Filename)
