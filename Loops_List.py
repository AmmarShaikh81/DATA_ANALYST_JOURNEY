a=[4,"roy",4.5,'6']
print(a)
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[3]))
#for loop
'''syntax of range 
range(start,stop,step)
for i in range(0,len(a)):
    print(a[i])
for i in range(len(a)-1,-1,-1):
    print(a[i])'''
#while loop
i=0
length=len(a)
while i<length:
    print(a[i])
    i=i+1
