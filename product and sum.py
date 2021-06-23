
#Given two integer numbers return their product. If the product is greater than 1000, then return their sum
a=int(input("Please enter a number:"))
b=int(input("Please enter another number:"))
product=a*b
print("Product=", product)
if product>1000:
    sum=a+b
    print("Sum=", sum)
