n, k = map(int, input().split())

count=0

while True :
  
  if n<k:
    count+=(n-1)
    break;
 
  count+=(n%k+1)
  n=n//k
  
print(f'count {count}')