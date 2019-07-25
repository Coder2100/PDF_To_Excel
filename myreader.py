# readind files

tables = open('foo.csv', 'r')
for table in tables:
    print(table)
table.close()
