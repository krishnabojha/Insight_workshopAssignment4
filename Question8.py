######### find prime number
def is_prime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
if __name__=='__main__':
    number=abs(int(input('Enter positive number : ')))
    print(is_prime(number))