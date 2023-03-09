X=int(input())

array=[0]*30001
array[2]=1

for i in range(3,X+1):
  temp=[array[i-1]]
  if i%5==0:
    temp.append(array[i//5])
  if i%3==0:
    temp.append(array[i//3])
  if i%2==0:
    temp.append(array[i//2])
    
  array[i]=min(temp)+1

print(array[X])