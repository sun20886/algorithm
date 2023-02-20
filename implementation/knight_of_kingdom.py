place=input()

count=0

match(place[0]):
  case 'a':
    y=1
  case 'b':
    y=2
  case 'c':
    y=3
  case 'd':
    y=4
  case 'e':
    y=5
  case 'f':
    y=6
  case 'g':
    y=7
  case 'h':
    y=8

x=int(place[1])
    
dx=[1,-1,1,-1, 2, -2, 2,-2] #수직 이동
dy=[2, -2,-2, 2, 1,-1, -1,1] #수평 이동

print(x, y)
for i in range(8):
  nx=x
  ny=y
  
  nx+=dx[i]
  ny+=dy[i]
  
  if 1<=nx<=8  and 1<=ny<=8 :
    count+=1
    
print(count)
  
  