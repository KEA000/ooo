import numpy as np
n = int(input('Enter number of unknowns: '))
a = np.zeros((n,n+1))
x = np.zeros(n)



print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n+1):
        a[i][j] = float(input( 'a['+str(i)+']['+
str(j)+']='))


for i in range(0,n):
    if a[i][i] == 0.0:
        for h in range(i+1, n):
            if a[h][i]!=0:
                for k in range(i,n+1):
                    tmp = a[h][k]
                    a[h][k] = a[h-1][k]
                    a[h-1][k] = tmp 
    for j in range(i+1, n):
        if a[i][i]==0:
            ratio =0
        else:
            ratio = a[j][i]/a[i][i]
    for k in range(i,n+1):
        a[j][k] = a[j][k]-(ratio * a[i][k])
p =np.delete(a,n,1)
r=np.linalg.matrix_rank(p)


flag=1
if r<n:
    for i in range(r,n):
        if a[i][n]!=0:
            flag=0
            break
if flag==0:
    print('\n no solution exists') 
elif flag==1:
    if r!=n:
        print('\n infinite solution exist')
    else:
        x[n-1] = a[n-1][n]/a[n-1][n-1]
        for i in range(n-2,-1,-1):
            x[i] = a[i][n] 
            for j in range(i+1,n):
                x[i] = x[i] - a[i][j]*x[j]
            x[i] = x[i]/a[i][i]
        print('\nsolution is: ')
    for i in range(n):
        print('X%d = %0.2f' %(i,x[i]))
