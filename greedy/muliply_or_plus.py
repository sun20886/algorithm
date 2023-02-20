n= input()

result=0

for i in n :
  i=int(i)
  
  if i<=1 or result<=1:
    result+=i
  else:
    result*=i

print(result)