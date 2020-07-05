########## sorting the list of tuple
info_tuple=('krishna','ojha',1)
more_tuple=(('jeevan','rai',2),('hari','magar',3),('bikash','khanal',4),('binod','gauli',5))
people=[]
dictionary={0:'first name',1:'last name',2:'age'}
people.append(info_tuple)
for i in more_tuple:
    people.append(i)
people.sort()
for num in range(len(dictionary)):
    print('Enter {} to sort by {}  , '.format(num,dictionary[num]))

a=int(input())
people.sort(key=lambda x:x[a])
print('The sorted tuple by ',dictionary[a],' : \n')
for tup in range(len(people)):
    print(people[tup])