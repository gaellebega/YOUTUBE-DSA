from functools import reduce
numbers=[1,2,3,4,5]

# allow to make the sum of the elements without initializer
# acc is gonna be 1 and then the x is gonna be 2
# then 3 is gonna becone the new accumulator that we have currwntly
# the next acc will be alway the new sum that we have
sum_of_numbers=reduce(lambda acc,x:acc+x,numbers)
# the accumulator is the first elemnt then the next value is the x
print(sum_of_numbers)


# return the acc value if the acc value is greater than x
max_value=reduce(lambda acc,x:acc if acc>x else x,numbers)
print(max_value)
fancy_map={x:(lambda x:x*x)(x) for x in range(5)}
print(fancy_map)
