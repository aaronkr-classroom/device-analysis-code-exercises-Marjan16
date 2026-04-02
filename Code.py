#data_tyoes.py
a = 10      # int
b = 3.14    # float
c = "Hello" # str
d = True    # bool

print(f"{a} ia a {type(a)}")
print(f"{b} ia a {type(b)}")
print(f"{c} ia a {type(c)}")
print(f"{d} ia a {type(d)}")

#str
e = 'Mim'
f = "Mahbuba Sultana"
name = e + " " + f

g = name + " said, \"it's a beautiful day!"
h = '"How \'ya doin\' today?"\n\t"Good!"'
print(g, "\n", h)

# Bool - only false or 0 or "" is False
i = True
j = False
k = bool(-1)
l = bool(a)
m = bool("")
n = bool(0)
o = bool(g)

print(i,j,k,l,m,n,o)