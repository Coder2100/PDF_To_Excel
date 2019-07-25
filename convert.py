import camelot

tables = camelot.read_pdf('foo.pdf')

tables

#print(tables[0].parse_report)
tables.export('foo.csv', f='csv', compress=True) # json, excel, htm
#tables.export('foo.csv', f='csv', c)
tables[0]
tables[0].parsing_report

tables[0].to_csv('foo.csv')
tables[0].df 
