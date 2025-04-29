Money=int(input("Enter Money "))
Time=int(input("Enter Time "))

if Money > 200 and Time < 7:
   print("Go To Theme Park")
else:
    print("Go Home")
    
if Money < 200 and Time > 7:
    print("Go To Ice Cream Parlour")
else:
    print("Go To Beach")
    