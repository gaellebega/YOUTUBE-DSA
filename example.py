my_list=[1,2,3,1,2,2,1]
# 1 2 3 1 2 3 5 6
freq={}
for i in my_list:
  freq[i]=freq.get(i,0)+1
print(freq)
# does 5 exist in my_dictionary?
print(5 in freq)
if 2 not in freq:
  print("I am busy")

  # when you want to get key  or values or both at the same time
print(freq.keys())
print(freq.values())
# this will come in the tuple
# it is very easy to loop to unpack and do more transformations
print(freq.items())
for f in freq:
  # alone is the key when they are combined is value inside the key
  print(f,freq[f])

 #to make it easy

for key,values in freq.items():
  print(key,values)
# how to change the dictionary
# update the dictionary by adding on the new element
freq.update({"age":20,"city":"kigali"})
print(freq)
# when you wanna remove something but then you can not found it it is better to do like this
removed=freq.pop("salary","Not found")
print(removed)
print(freq)
# 
removewithpop=freq.popitem()
print(removewithpop)


# when we want to give the deafault values we use the method called fromkeys
# 

  
