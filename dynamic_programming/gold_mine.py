T=int(input())
result=[]

for t in range(T):

  n, m=map(int, input().split())
  temp=list(map(int, input().split()))

  array=[]
  for i in range(n):
    array.append(temp[i*m: (i+1)*m])
  
  dp=[[0 for j in range(m)] for i in range(n)]

  for j in range(m):
    for i in range(n):
      if j==0 :
        dp[i][j]=array[i][j]
      else:
        dps=[dp[i][j-1]]
        if i-1>=0:
          dps.append(dp[i-1][j-1])
        if i+1<n:
          dps.append(dp[i+1][j-1])
        dp[i][j]=max(dps)+array[i][j]
        
  result.append(max([dp[i][m-1] for i in range(n)]))

for i in result:
  print(i)