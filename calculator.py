a=int(input("Enter first no. "))
b=int(input("Enter second no. "))
print("Enter + for addintion")
print("Enter - for subtraction")
print("Enter * for multiplication")
print("Enter / for Division")
c=str(input("Enter the operation: "))
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    print(a/b)
else:
    print("Enter the correct operation code")
