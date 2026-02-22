username={"name":"uwimana","age":30, "location":"Kigali"}
# to get the values
print(username["name"])
username["age"]=20
print(username)
# what we do when the key is not the part of the dictionary and you are trying to access it?
# we will get an error
print(username["id"])