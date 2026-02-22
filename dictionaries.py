my_dict={
  "a":10,
  "b":20,
  "c":30
}
# dictionaries are ordered
# dicitonaries when keys have duplicates pythin will show the last one
# dictionaries when the values have the duplicates  it allows it
# dictionaires are not indexed means you can not access them using the index
# we use the keys to access the values
# mutability
print(my_dict["c"])
# to change the values
my_dict["a"]=100
print(my_dict)


# DICTIONARIES METHODS
# what we do when the key is not the part of the dictionary and you are trying to access it?
# instead of using the normal way we can just use get to get what we want and error become none instead of key error
print(my_dict.get("id"))
# get allow us to return the value and none when no value found oalso you can get the default value by passing it into innit
print(my_dict.get("id","unkown"))
# to test if the key is inside the dictionary to return true or false
print("age" in my_dict)
print("age" not in my_dict)

# VIEW OBJECTS
# give you the live view of the dictionary's keys,values aor key value pairs
# to get all the keys
print(my_dict.keys())
print(my_dict.values())
# it contain the combination of the tupleas which will be needed when you need the key and value together for looping transforming sata building new dict and comparing and more
print(my_dict.items())

