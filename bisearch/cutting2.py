N,M=map(int, input().split())
list=list(map(int, input().split()))

def bisearch(list, M, start, end):
  
  mid=(start+end)//2
  temp=[x-mid for x in list if x-mid>=0]
  if sum(temp)==M:
    return mid
  elif sum(temp)<M:
    return bisearch(list, M, start, mid)
  else:
    return bisearch(list, M, mid, end )

print(bisearch(list, M, 0, max(list)))