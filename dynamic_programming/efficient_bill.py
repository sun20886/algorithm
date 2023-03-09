N, M= map(int, input().split())
bills=[]
array=[-1]*10001

for i in range(N):
  bills.append(int(input()))

for i in range(1,M+1):
  if i in bills:
    array[i]=1

  else:
    temp=[array[i-x] for x in bills if i-x>0 and array[i-x]!=-1]
    if len(temp)==0:
      array[i]=-1
    else:
      array[i]=min(temp)+1
  
print(array[M])