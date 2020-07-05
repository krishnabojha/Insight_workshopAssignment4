####### make a list, sort a list and check the id of list
friend_list=[]
before=id(friend_list)
print('id before append : ',before)
a=input("Enter your friend's name : ").split()
for name in a:
    friend_list.append(name)
after=id(friend_list)
print('id after append : ',after)
if before==after:
    print('id is not changed.')
a.sort()
print('sorted list : ',a)
print('first item : ',a[0])
print('second item : ',a[1])