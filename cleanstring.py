def cleanstr(test_str):
  strn = " ".join(test_str.split())
  strn=strn.replace('.', '. ', strn.count('.')).replace(',', ', ', strn.count(','))
  return strn

strn=input("enter string: ")
print(cleanstr(strn))