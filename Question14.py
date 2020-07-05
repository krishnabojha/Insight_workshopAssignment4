############# write data dictionary to file
import csv

header=['name', 'address', 'age']
data = [{'name': 'George', 'address': '4312 Abbey Road', 'age': 22},
        {'name':'John', 'address': '54 Love Ave', 'age': 21}]
filename='Detail.csv'
def store_data(file_name,rows):
    file=open(file_name,'w')
    filewriter=csv.DictWriter(file,fieldnames=header)
    filewriter.writeheader()
    filewriter.writerows(rows)
    file.close()
store_data(filename,data)
print('Input data : ',data)
print('your data is stored to ',filename,' file.')
