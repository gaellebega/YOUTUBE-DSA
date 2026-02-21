add_1=lambda x:x+1
result=add_1(1)
print(result)

make_double =lambda arr:list(map(lambda x:x*2,arr))
newarray=make_double([1,2,3,3])
print(newarray)

add = lambda a,b:a+b
print(add(2,3))

# LAMBDA WITH DIFFERENT SCENARIOS

# lamda with one parameter

make_multiply=lambda x:x*x
print(make_multiply(2))

# lamda with multiple parameters
make_substraction=lambda a,b:a-b
print(make_substraction(7,2))




# lambda with the lists and the for loop
double_list=lambda arr:[x*2 for x in arr]
print(double_list([1,2,3,4]))


# we can also use the lamda witht he map or filter when we have the list
nums=[1,2,3]
result=list(map(lambda x:x*2, nums))
print(result)

nums2=[3,4,5]
# filter returns where the condition is equal to true
my_unique=list(filter(lambda n:n-1==0,nums2))
print(my_unique)

lisst=["hen","goat","chicken","elephant"]
zoo= list(filter(lambda w:len(w)>3,lisst))
print(zoo)

# lamda with the  tuples
# sorting basing on the key
values=[(1,"b","okay"),(2,"a","world"),(3,"d","nice")]

# this is same as using the reverse
sorted_val=sorted(values,key=lambda x:x[-1])
# using the key function to sort using the lamda
sorted_value=sorted(values,key=lambda x:x[0])
sorted_values=sorted(values,key=lambda x:x[1]+x[1])
print(list(sorted_val))
print(list(sorted_value))
print(list(sorted_values))
# here when we have a tie it is gonna sort the secod string
sorted_values=sorted(values,key=lambda x:x[1]+x[2])