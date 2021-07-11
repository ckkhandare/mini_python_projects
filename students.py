people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
count=0
print("1. no. of people in dict")
for i in people:
	count = count+1
print("Answer:",count)
print("")

print("2. Change Lisa’s favourite colour")
print("Answer:",people['Lisa'])
print('')

print("3. Remove 'Jenny' and her favourite colour")
people.pop('Jenny')
print(people)
print('')
print("4. Sort and print students and their favourite colours alphabetically by name")
for i in sorted(people):
   people[i]=people[i]
print("Answer:",people)