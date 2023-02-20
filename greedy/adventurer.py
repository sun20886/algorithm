n = input()
temp = input().split()
array = [int(i) for i in temp]

array.sort()
result=0

for i in array:
  if len(array)<i or sum(array[:i])>i*i:
    break;
  result+=1
  array=array[i:]

print(result)