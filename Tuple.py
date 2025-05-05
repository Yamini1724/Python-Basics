a=()
print(type(a))

b=(1,)
print(b)

#Indexing
c=(1,2,3,4,5)
print(c[3])
print(c[-3])

#Slicing
print(c[0:3])
print(c[-4:-1])


#----Tuple Methods----

#Index()
d=("red","black","white","brown")
print(d.index("brown"))

#count()
print(d.count("red"))


#----Tuple Operators----

m=("Yam")
n=("venu")

#Concatenation
print(m+n)

#Repetition
print(m*5)
print(n*3)

#Iteration
for i in c:
    print(i)

#Length
print(len(c))

#Membership
print(1 in c)
print(5 not in c)


#----Tuple Built-in Operators----

x=(7,8,9)

#sum
print(sum(x))

#maximum
print(max(x))

#minmum
print(min(x))

#Sequence
L="PYTHON"
print(tuple(L))






