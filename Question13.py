########## create file and append the name, address and age
import csv

header=['Full name', 'Address', 'Age']
data = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
filename='friend.csv'
def store_data(file_name,rows):
    file=open(file_name,'w')
    row_writer=csv.writer(file)
    filewriter=csv.DictWriter(file,fieldnames=header)
    filewriter.writeheader()
    row_writer.writerows(rows)
    file.close()
store_data(filename,data)
print('Input data : ',data)
print('your data is stored to ',filename,' file.')
