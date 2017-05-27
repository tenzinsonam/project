import linecache

file = "real.c"
line = linecache.getline(file, 4)
print (line.strip())
