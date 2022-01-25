
print(" select a operator")
print("1.Add")
print("2.subration")
print("3.multiplication")
print("4.division")
a=int(input("enter your value"))
b=int(input("enter your value"))
choice=input("enter your operator")
if(choice=="1"):
    b=a+b
    print("added value is",b)
elif(choice=="2"):
    c=a-b
    print("subrated value is",c)
elif(choice=="3"):
    d=a*b
    print("muliplyed value is",d)
elif(choice=="4"):
    e=a/b
    print("divided value is",e)
else:
    print("please choose from operator")