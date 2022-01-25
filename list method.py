#list
a=["apple","ball","apple","cat","dog"]
a.append("orange")
print(a)
#clear
a=["apple","ball","apple","cat","dog"]
a.clear()
print(a)
# coppy
a = ["apple","ball","apple","cat","dog"]
x = a.copy()
print(x)
#count
a=["apple","ball","apple","cat","dog"]
x=a.count("apple")
print(x)
#exend
a=["apple","ball","apple","cat","dog"]
b=["orange"]
a.extend(b)
print(a)
#index
a=["apple","ball","apple","cat","dog"]
x=a.index("cat")
print (x)
#insert
a=["apple","ball","apple","cat","dog"]
a.insert(1,"monkey")
print(a)
#pop
a=["apple","ball","apple","cat","dog"]
a.pop(1)
print(a)
# remove
a=["apple","ball","apple","cat","dog"]
a.remove("apple")
print(a)
#reverse
a=["apple","ball","apple","cat","dog"]
a.reverse()
print(a)
#sort
a=["apple","ball","apple","cat","dog"]
a.sort()
print(a)