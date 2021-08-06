L1 = []
for i in range(3):
    a = input("Enter a number: ")
    L1.append(a)
print('List 1 is',L1)
L2 = []
for j in range(3):
    a = input("Enter a number: ")
    L2.append(a)
print('List 2 is',L2)
s1 = set(L1)
s2 = set(L2)
t = s1.intersection(s2)
q = s1.union(s2)
print("Overlap is ",list(t))
print("Join is ",sorted(list(q)))
