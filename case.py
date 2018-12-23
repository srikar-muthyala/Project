def dd():
  print("hi")
def d():
  print("hiii")
d={
  1:dd,
  2:d
}
n=int(input())
i=n
d[i]()
