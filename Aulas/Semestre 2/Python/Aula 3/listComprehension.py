l = []
for i in range(10):
    if i%2 == 0:
        l.append(i)
print(l)

#list comprehesion

l1 = [i for i in range(10) if i%2==0]
print(l1)

l2 = [0 for i in range(10)]
print(l2)