new_user={"id":None,
          "name":None,
          "age":None,
          "city":None}
print(new_user)

# from keys is used to build a new dictionary where all keys gt the same default values
new_user=dict.fromkeys(["id","name","age","city"],20)
print(new_user)