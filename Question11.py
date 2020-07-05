####### extract only filename
firstname=input('Enter file name with extension : ')
if '.' in firstname:
    x=slice(0,firstname.index('.'))
    print(firstname[x])
else:
    print(firstname)
print('This code works for any filenames of arbitrary length.')