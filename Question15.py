############# bank customer form 
attribute=[{'id':0,'customer_name':'krishna ojha','account_no':213212165312,'address':'pepsi','contact_no':9811111111,'balance':11545121},
           {'id':1,'customer_name':'Binod Rai','account_no':213212165312,'address':'baneshwor','contact_no':9822222222,'balance':11545121},
           {'id':2,'customer_name':'Ganga Magar','account_no':213212165312,'address':'ratnapark','contact_no':9833333333,'balance':11545121}
          ]
class Customer:
    
#     def __init__(self,name):
#         self.name=name
    @staticmethod
    def authenticate():
        _c_pass=int(input('Enter your password(pass:1234) : '))
        if _c_pass==1234:
            return True
        else:
            return False
        
    def name(self):
        return attribute[c_id]['customer_name']
    def account_no(self):
        return attribute[c_id]['account_no']
    def withdraw(self):
        print('you are in withdraw method.')
    def balance_inquiry(self):
        return 'Your balance is {}'.format(attribute[c_id]['balance'])
    def change_password(self):
        print('you are in change password block.')
    def details(self):
        print('Your Detail : ')
        print('name : ',attribute[c_id]['customer_name'])
        print('account number : ',attribute[c_id]['account_no'])
        print('address : ',attribute[c_id]['address'])
        print('contact : ',attribute[c_id]['contact_no'])
    def exit(self):
        print('Thank you !!!')
print('\n3 STAR BANK\nWELCOME!!!')
c_id=int(input('Enter your id number(0 to 2) : '))
obj=Customer()
try:
    response=obj.authenticate()
except:
    print('oops!!!')
if response==True:
    print("\nHello ",obj.name())
    print('What can i help you?\n')
    print('\nPress key:\n')
    print('1 for account number : ')
    print('2 for withdraw : ')
    print('3 for balance_inquiry : ')
    print('4 for change password : ')
    print('5 for your information : ')
    print('6 for exit : ')
    func_code=int(input())
    
    if func_code==1:
        print('Your account number : ',obj.account_no())
    elif func_code==2:
        obj.withdraw()
    elif func_code==3:
        print(obj.balance_inquiry())
    elif func_code==4:
        obj.change_password()
    elif func_code==5:
        obj.details()
    else:
        obj.exit()
else:
    print('You entered wrong Password !!!')