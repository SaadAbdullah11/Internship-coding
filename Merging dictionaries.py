#Question: Merge following two Python dictionaries into one
dict1={"A":"Ahmad", "B": "baseball", "C":"cat"}
dict2={"D":"Danyal","E":'ear',"F":"Fair"}
dict3={}
dict3.update(dict1)
dict3.update(dict2)
print(dict3)
