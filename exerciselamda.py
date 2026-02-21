nlist=[1,2,3,4,5,6,7]

new=list(filter(lambda x: x%2!=0,nlist))
print(new)

total=sum(nlist)
size=total/len(nlist)
greater_avg=list(filter(lambda x:x>size(x for x in nlist )))
print(greater_avg)

make_another=lambda x,y:x+y
result=make_another(3,8)
print(result)