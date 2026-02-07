'''find maximum of the array'''
a=[1,5,4,7,3]
big=a[1]
n=len(a)
i=1
for i in range(i,n):
    if(a[i] > big):
        big=a[i]
print(big)
