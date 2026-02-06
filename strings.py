text="python is amazing"
s="python ,is ,amazing"
print(f"the text is {text}")
#slicing
b=text[:6]
print(b)
c=text[0:17:3]
print(c)
#string methods
print(text.lower())
print(f"text in upper case {text.upper()}")
print(f"python is  {text.replace('amazing','powerfull')}")
c=s.split(",")
print(c)
d=text.split("\n")
print(len(d[0]))

