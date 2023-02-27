
def dfs(x, y):
  if x<0 or x>=n or y<0 or y>=m:
    return False
    
  if matrix[x][y]==0:
    matrix[x][y]=1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    return True
  return False


n, m =map(int, input().split())

matrix=[]
for i in range(n):
  matrix.append(list(map(int,input())))
  
result=0

for i in range(n):
  for j in range(m):
    if dfs(i,j)==True:
      result+=1

print(result)
