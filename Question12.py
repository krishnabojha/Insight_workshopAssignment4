##### check whether the string is palindrome or not
name=input('Enter a string : ')
def is_palindrome():
    if name==name[::-1]:
        print('The string is palindrome')
    else:
        print('The string is not palindrome')

is_palindrome()