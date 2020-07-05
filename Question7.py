######### find older and younger friend
friend_list=[('binod','rai',25),('suman','adhikari',24),('jeevan','ojha',20),('rajad','shakya',None)]
age_sum=0
for i in range(len(friend_list)):
    if friend_list[i][2]==None:
        friend_list.remove(friend_list[i])
    else:
        age_sum+=friend_list[i][2]
age_avg=age_sum/len(friend_list)
print('The friends are : ')
for i in range(len(friend_list)):
    if friend_list[i][2]>age_avg:
        print('old {} {}'.format(friend_list[i][0],friend_list[i][1]))
    else:
        print('young {} {}'.format(friend_list[i][0],friend_list[i][1]))