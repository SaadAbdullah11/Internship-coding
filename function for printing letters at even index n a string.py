#Function which takes a string, and displays only those characters which are present at an even index number.
a=input("Please enter a string:")
def index_char(a):
        count=0
        while count<len(a):
            print(a[count])
            count+=2
index_char(a)
