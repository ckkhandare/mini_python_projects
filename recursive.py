def main(x):
  if x<=1:
    return x
  else:
    return sum(x)
    
def sum(x):
  return x + main(x - 1)

x=int(input("enter number: "))
print(main(x))