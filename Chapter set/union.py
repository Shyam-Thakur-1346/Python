s1={23,45,8,3,35,67}
s2={3,8,35,4}

print(s1.union(s2))
print(s1.intersection(s2))

print({23,45}.issubset(s1))

print(s1.issuperset({23,89}))

print(s1.difference(s2))