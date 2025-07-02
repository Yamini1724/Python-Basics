# # num = int(input("Enter a Number"))
# # if num % 2 == 0:
# #     print("Even Number")
# # else:
# #     print("Odd Number")


# a="venugopalmurala"
# print(a[0:15:2])
# print(len(a))

# a=50
# b="10"
# print(a+int(b))


# for i in range(1,11):
#     print(i)
#     if  i % 2 == 0:
#        print(i)
    
count = 0
num=int(input("Enter a Number "))
for i in range(1,num+1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")