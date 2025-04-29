#num=24
#if num % 2 == 0:
 #  print("even")
#else:
 #  print("odd")


count = 0
n=int(input("Enter number"))
for i in range(1,n+1):
    if n % i == 0:
        count+=1
if count==2:
    print("prime")
else:
    print("not a prime")

