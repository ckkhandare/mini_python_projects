s=input("enter sentance: ")
s1="".join(c for c in s if c.isalpha())
s1=s1.lower()
s2=s1[::-1]
if s1==s2:
  print("It is a palindrome")
else:
  print("It is not a palindrome")