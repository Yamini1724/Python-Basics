# -----How to access list elements-----

List=[1,2,3,4]

#List Indexing
print(List[2])

#Negative Indexing
print(List[-3])

#List Slicing
L=[1,2,3,4,5,6]
print(L[0:4]) #No step size
print(L[0:6:2])
print(L[:5:2])#No start element
print(L[2::2])#No stop element
print(L[-6:-1])


# -----List Operators-----

L1=[1,2,3]
L2=[4,5,6]

#Concatenation
print(L1+L2)

#Repetition
print(L1*3)
print(L2*2)

#Membership
print(2 in L1)
print(3 in L2)

#Iteration
for i in L1:
    print(i)

for i in L2:
    print(i)

#Length
L3=[7,8,9,6,5,4]
print(len(L3))


# -----List Built-In Functions-----

L4=[9,8,7]
L5=[6,5,4]

#Sum(sum()):
print(sum(L4))

#Maximum --- max(list)
print(max(L5))

#Minimum --- min(list)
print(min(L5))

#Sequence --- (list(seq))
a="PYTHON"
print(list(a))

#----Nested List----
L6=[[1,2],[3,4],[5,6]]
print(L6[0],[0])
print(L6[1],[0])
print(L6[1],[2])


#  ----- List Methods -----

V=["black","blue","brown","pink","red"]

#append()
V.append("Yellow")
print(V)

#Insert()
V.insert(2,"White")
print(V)

#Extend()
y=["Violet","Purple"]
V.extend(y)
print(V)

#Remove()
V.remove("pink")
print(V)

#pop()
V.pop(4)
print(V)

#Index()
V.index("Purple")
print(V)

#Count()
V.count("red")

#Sort()
V.sort()
print(V)

#Reverse()
V.reverse()
print(V)

#Copy()
y=V.copy()
print(y)


