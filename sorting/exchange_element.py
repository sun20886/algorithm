N, K= map(int, input().split())

matrix_A=list(map(int,input().split()))
matrix_B=list(map(int,input().split()))

matrix_A.sort()
matrix_B.sort(reverse=True)

for i in range(K):
  if matrix_A[i]<matrix_B[i]:
    matrix_A[i], matrix_B[i]=matrix_B[i], matrix_A[i]
  else:
    break
print(sum(matrix_A))