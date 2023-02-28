from collections import deque

def bfs(x,y):
  queue=deque()
  queue.append((x,y))
  maze[x][y]+=1
  
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]

      if nx<0 or nx>=N or ny<0 or ny>=M:
        continue 
      if maze[nx][ny]==0:
        continue
      if maze[nx][ny]==1:
        maze[nx][ny]=maze[x][y]+1
        queue.append((nx,ny))
  return maze[N-1][M-1]-1

N, M=map(int,input().split())

maze=[]
for i in range(N):
  maze.append(list(map(int,input())))

dx=[0,0,-1,1]
dy=[1,-1,0,0]

result=bfs(0,0)
print(result)
