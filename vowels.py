v=0
c=0
b=0
s=input()
for i in s:
  if(i=="a" or i=='e' or i=='o' or i=='i' or i=='u'):
    v=v+1
  elif(i==' '):
    b=b+1
  else:
    c=c+1
print("vowels: ",v)
print("consonants: ",c)
print("spaces: ",b)
