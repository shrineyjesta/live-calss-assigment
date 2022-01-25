#capitalize
a="dora"
x=a.capitalize()
print(x)
#casefold
a="DORA"
x=a.casefold()
print(x)
#center
a="dora"
x=a.center(100)
print(x)
#count to count how many
a= "My name is Stale"
x=a.count("my")
print(x)
#encode
a= "My name is Stale"
x=a.encode()
print(x)
#endswith
a= "My name is Stale."
x=a.endswith(".")
print(x)
#expandtabs
a="H\te\tl\tl\to"
x=a.expandtabs(10)
print(x)
#find
a="My name is Stale."
x=a.find("is")
print(x)
#format
a="My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print(a)
#index
a="My name is Stale."
x=a.index("is")
print(x)
#isalnum()
a="apple12"
x=a.isalnum()
print(x)
#isalpha
a="apple"
x=a.isalpha()
print(x)
#isdecimal to check all numbers
a="123"
x=a.isdecimal()
print(x)
#isdight
a="123a"
x=a.isdigit()
print(x)