n=int(input())
plans=input().split()

x,y=1,1

for i in plans:
  match(i):
    case 'L':
      if y-1<1:
        continue
      y-=1
    case 'R':
      if y+1>n:
        continue
      y+=1
    case 'U':
      if x-1<1:
        continue
      x-=1
    case 'D':
      if x+1>n:
        continue
      x+=1
    
print(x, y)