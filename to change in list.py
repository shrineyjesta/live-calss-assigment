# to chnge item in list
a=["dog","cat","monkey","cow","lion"]
a[2]="tiger"
print(a)
a=["dog","cat","monkey","cow","lion"]
a[1:3]=["donkey","lepord"]
print(a)
#to insert
a=["dog","cat","monkey","cow","lion"]
a.insert(0,"tiger")
print(a)
#to join
a=["dog","cat","monkey"]
b=["cow","lion"]
a.extend(b)
print(a)
a=["dog","cat","monkey"]
b=("cow","lion")
a.extend(b)
print(a)