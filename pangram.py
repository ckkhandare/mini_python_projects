s=input("enter sentance: ")
s1="".join(c for c in s if c.isalpha())
s1=s1.lower()
chars = "abcdefghijklmnopqrstuvwxyz"
for i in chars:
  if i not in s1:
    print('its not a pangram')
    break
else:
  print('its a panagram')