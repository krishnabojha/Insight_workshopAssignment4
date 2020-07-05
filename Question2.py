###### check the year is leap year or not
year=int(input('Enter year : '))

def leap_year(func):
    
    def inner(entered_year):
        print(func(entered_year))
    return inner
  
@leap_year
def calculate_leap_year(year):
    difference=abs(2012-year)
    if difference%4==0:
        return 'This is leap year.'
    else:
        return 'This is not leap year.'
calculate_leap_year(year)