a=[1,2,3,4,5,16,7,8,9]
b=[]
l=a
for i in range(len(a)):
    if a[i]%2==0:
        l=a[i]**3
        b.append(l)
print(b)
