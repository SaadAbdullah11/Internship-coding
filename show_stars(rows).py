#Function called show_stars(rows). If rows is 5, it should print the following:
#*
#**
#***
#****
#*****
rows=int(input("Please enter the number of rows:"))
def show_stars(rows):
    if rows==5:
        count=1
        for i in range(5):
            print('*'*count)
            count+=1
show_stars(rows)
