# ----- STRING -----

a='yam'
b="venu"
c='''veni'''
#print(type(a),type(b),type(c))

# ------ STRING METHODS ------

# UPPER()
v='yamu'
print(a.upper())

#LOWER()
y='VENU'
print(y.lower())

#endswith()
x="yamu venu"
print(x.endswith("venu"))

#startswith()
z="yamu venu"
print(z.startswith("yamu"))

#Replace
u="yamu venu veni"
print(u.replace("veni", "munnu"))

#Split
t=z.split()
print(t)

#Count
e="guava"
print(e.count("a"))

#Index
f="hello world"
g=f.index("o")
print(g)

#Find
i=f.find("o", 5)
print(i)

#Strip
j=" YAMINI "
k=j.strip()
print(j)

#Removeprefix
l="PreHelloWorld"
o=l.removeprefix("Pre")
print(o)

#Removesuffix
p="HelloWorldEnd"
q=p.removesuffix("End")
print(q)