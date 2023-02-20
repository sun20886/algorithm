string=input()

alphabet=[]
number=0

for i in string:
  if int(ord(i))>=int(ord('A')):
    alphabet.append(i)
  else:
    number+=int(i)

# result=''
# for i in sorted(alphabet):
#   result+=i

print(alphabet)
# result=''.join(sorted(alphabet))
result=''.join(alphabet)
print(result)
  
print(result+str(number))
