def find_longest_word(lst,n):
  word=[]  
  for i in lst:
    if len(i)>n:      
      word.append(i)
  return word

lst = [item for item in input("Enter words space separated : ").split()]
n=int(input('enter a number: '))
print(find_longest_word(lst,n))