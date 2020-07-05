##### find whether the bracket is valid or invalid
class Check_validity:
    def baracket(self,bra):
        count=0
        for i in bra:
            if((i=='(')|(i=='{')|(i=='[')):
                count+=1
            else:
                count-=1
        if count==0:
            return "Valid"
        else:
            return "Invalid"
my_input=input('Enter brackets : ')
obj=Check_validity()
print('Output : ',obj.baracket(my_input))