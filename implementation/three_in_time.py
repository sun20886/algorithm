N=int(input())

total=0 #3이 포함되는 모든 경우의 수

#0에서 59까지의 수 중에서 3을 포함하는 수
three_in_sixty=[i for i in range(60) if '3' in str(i)] 

#0에서 59까지 3을 포함하는 수의 개수
three_count_in_sixty=len(three_in_sixty)

#시간에서 3을 포함하지 않는 한 시간동안 분 또는 초에 3을 포함하는 숫자의 개수
three_not_in_hour=three_count_in_sixty*60+(60-three_count_in_sixty)*three_count_in_sixty

for i in range(N+1):
  print(i)
  if '3' in str(i): #시간에 3을 포함할 때 3을 포함하는 숫자의 개수 : 60*60
    total+=3600
  else :
    total+=three_not_in_hour

print(total)