def overlapping(lst1, lst2):
    lst= list(set(lst1) & set(lst2))
    if lst!=[]:
      return True
    else:
      return False
  
lst1 = [int(item) for item in input("Enter numbers space separated : ").split()]
lst2 = [int(item) for item in input("Enter numbers space separated : ").split()]
print(overlapping(lst1, lst2))