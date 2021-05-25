import ast
import sys
import symtable
import dis

from astutil import print_node, print_table

filename = sys.argv[1]
#print("Crawling file:", filename)

with open(filename, "r") as f:
    source = f.read()

t = ast.parse(source)
#print(t)

print_node(t)

table = symtable.symtable(source, "a", "exec")
print_table(table)

co = compile(source, filename, "exec")
dis.dis(co)
