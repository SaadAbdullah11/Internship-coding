a=int(input("Please tell how many one letter strings do u want to enter:"))
list=[]
for x in range(a):
    b=input("Please enter a string:")
    list.append(b)
if "a" in list:
    print("a is present")
else:
    print('a is not present')

