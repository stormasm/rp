import sys
import dis

filename = sys.argv[1]

with open(filename, "r") as f:
    source = f.read()

co = compile(source, filename, "exec")
dis.dis(co)
