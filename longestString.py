def find_longest_word(lst):  
  max_count=-1
  for i in lst:
    if len(i)>max_count:
      max_count=len(i)
      word=i
  return word

lst = [item for item in input("Enter the list items : ").split()]
print(find_longest_word(lst))