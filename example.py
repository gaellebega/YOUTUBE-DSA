my_list=list(map(int,input().split()))
# 1 2 3 1 2 3 5 6
freq={}
for i in my_list:
  freq[i]=freq.get(i,0)+1
print(freq)