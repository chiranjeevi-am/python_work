a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]



c=[]
while len(a)>0 and len(b)>0:
    if a[0]<b[0]:
        c.append(a.pop(0))
    else:
        c.append(b.pop(0))

if len(a)>0:
    c = c + a
if len(b)>0:
    c = c + b

print(c)