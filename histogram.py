numbers=input("enter numbers space separated: ")
num=numbers.split()
for i in num:
  n = int(i)
  star=""
  while(n>0):
    star+="*"
    n = n-1
  print(star)