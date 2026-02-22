username={"name":"uwimana","age":30, "location":"Kigali"}
# to get the values
print(username["name"])
username["age"]=20
print(username)
# what we do when the key is not the part of the dictionary and you are trying to access it?
# we will get an error
# print(username["id"])

new_dictionary={"id":1,"name":"John","age":30,"city":"Berlin"}
# Dictionary COMPREHENSION
# It have 3 components key value expression,a loop and optional condition
# we are gonna use the filter cs we only need the string values than eafter we gonna convert them to the uppercase
user_string={
  # expression
  key.lower():values.upper()
  # loop
  for key,values in new_dictionary.items()
    # filter
  if isinstance(values,str)
}
print(user_string)

