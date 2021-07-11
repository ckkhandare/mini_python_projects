weekdays=7
days = int(input('Enter days in the month :'))
first_day = int(input('Enter start day mon=0,tue=1,wed=2,thurs=3,fri=4,sat=5,sun=6 : '))
counter = 0
print('mon   tue   wed   thur  fri   sat   sun')
print( end=' '* 6 *first_day)
for i in range(1, days + 1):
    if i >= 10:
        print(i, end='    ')
    else:
        print(i, end='     ')
    counter = counter + 1
    if (counter - (weekdays - first_day)) % 7 == 0:
        print('\n')
