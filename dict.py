# dictionary manual creation
my_home={
  "name":"inzu",
  "location":"karuruma",
  "height":"2000m"
}
print(my_home["name"])
# here we have to use the brackets and the get method when we know that is not included
print(my_home.get("size","sorry size not found"))

# COUNTING FREQUENCY
nums=list(map(int,input().split()))

freq={}
for num in nums:
  # when the element not found then add 1
  # without zero it will be the hkey error cz you are tyring to assign something thst doesnot exist
  # this is for building and updating the dictionary
  freq[num]=freq.get(num,0)+1
print(freq)