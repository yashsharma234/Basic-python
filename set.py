e=set()
print(type(e))
e={ 1,2,3,3,4,5,6,7,8,"yash"}
print(e,type(e))

#add
e.add(23)
print(e)
#remove
e.remove(3)
print(e)
#discard
e.discard(4)
print(e)
#pop
e.pop()
print(e)
#clear
e.clear()
print(e)
#union
s1={1,2,3,4,5,61,7,8,9}
s2={1,2,3,45,5}

print(s1.union(s2))
#intersection
print(s1.intersection(s2))
#difference
print(s1.difference(s2))
print(s2.difference(s1))
#symetric
print(s1.symmetric_difference(s2))
#subset
print(s1.issubset(s2))
print({1,2}.issubset(s2))
#superset
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))