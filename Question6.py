####### find friend
def find_friend(frn='John'):
    for friend in friend_list:
        if friend==frn:
            return "found"
    return 'not found'

if __name__=='__main__':
    friend_list=['krishna','jeevan','binod','yogesh']
    print('Friend list : ',friend_list)
    frn=input('Enter your friend name : ')
    print(find_friend(frn))