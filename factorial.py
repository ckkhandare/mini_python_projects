factor=int(input("enter a number: "))
num = 1
if factor >= 1:
  for i in range (1,factor+1):
    num = num * i
    print(i,num)