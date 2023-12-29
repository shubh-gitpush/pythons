#sets are in {}, unchangable value only comes 1 time in sets,concepts of 11th will be used here
a={1,2,"carlos0",2,4,1,"carlos0"}
print(a)
b={1,2,3,4,5,6,"carlos0"}
print(a.union(b))
print(a.intersection(b))
print(a.symmetric_difference(b))#not common
print(a.isdisjoint(b))#wheather it is disjoint or not
print(b.issuperset(a))# part of it or not
b.add("mentos")#also can be removed using (remove)or(discard)
print(b)
#del a(delete the set)
if 1 in b:
         print("true")
else:
    print("false")