user={"id":1,"age":30,"work":"google"}
# looping we are gonna need the .items first
# this will only get the keys not the values
  # the GOOD way
for key,values in user.items():
    print(key,values)

    #add , Remove, Update 
user["name"]="john"
user["age"]=12
print(user)
# to be able to update the multiple things
# will chnage what is there and what is not it will create
user.update({"age":40,"city":"paris"})
print(user)
# to remove we also use the key so the pop return the items that is removed
new_dictionary=user.pop("age")
# to avoid the errors when we have used the pop we have to use
age=user.pop("salary","not found")
print(age)
# pop on the dictionary have always to remove something
print(new_dictionary)
print(user)
# this is used to remove our last item to mean our last pairs
print(user.popitem())
print(user)