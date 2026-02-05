#in python two diffrent variables can be compared
a=4
b="ammar"
print(a==b)
#But it will show error when we used '>' "<".It is is strict rule in python that we will not compared  two diffrent variables in python
#print(a<b)
#if statemennt
age=8
if(age>=18):
    print("you can drive")
elif(age<18):
    print("you cannot drive")
    if(age<=9):
        print("you are child now")
else:
    print("you can drive")
#Ternary operator
age=8
print("you can drive") if age >=18 else print("you cannot drive")