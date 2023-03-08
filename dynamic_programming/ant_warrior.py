N=int(input())
array=list(map(int, input().split()))

results=[0]*N
results[0]=array[0]
results[1]=array[1]

for i in range(2, N):
  if i==2:
    results[i]=array[i]+array[0]
  elif results[i-2]>= results[i-3]:
    results[i]=array[i]+results[i-2]
  else:
    results[i]=array[i]+results[i-3]

print(results[N-1])