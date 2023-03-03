N,M=map(int, input().split())
list=list(map(int, input().split()))

H=0

for i in range(max(list)-1, 0, -1):
  temp=[x-i for x in list if x-i>0]
  if sum(temp)>=M:
    H=i
    break

print(H)
