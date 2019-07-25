


#f = open('excel_demo.xlsx', 'r')

files = open('foo.csv', 'r')
for file in files:
    f = open('excel_demo.xlsx', 'a')
    f.write(file)
    f.close()
files.close()
