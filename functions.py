def factorial():
  a=1
  n=int(input("enter a number "))
  for i in range (1,n+1):
    a=a*i
  print("factorial of ",n,"is",a)
def fibonacci():
  a=0
  b=1
  n=int(input())
  for i in range (0,n):
    print(a)
    c=a+b
    a=b
    b=c
dic={
  1:factorial,
  2:fibonacci
}
n=int(input("1.factorial 2.fibonacci "))
dic[n]()
