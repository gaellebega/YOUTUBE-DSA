user={"id":1,"name":"John","age":20,"city":"Berlin"}
# key,values=string :name,city

# COMPREHENSION on dictionary we use {}
new_strings={key:values.upper()  for key,values in user.items() if isinstance(values,str)}
print(new_strings)
for key,values in user.items():
  if isinstance(values,str):
# this will not print the key pairs
   print(f'"{key.upper()}":"{values.lower()}"')

  