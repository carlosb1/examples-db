import happybase
connection = happybase.Connection('hostname')
table = connection.table('table-name')
table.put(b'row-key', {b'family:qual1',b'value1', b'family:qual2',b'value2'})
row = table.row(b'row-key')
print(row[b'family:qual1'])
for key, data in table.rows(['bow-key-1', b'row-key-2']):
    print(key,data)

for key, data in table.scan(row_prefix=b'row'):
    print (key, data)

row = table.delete(b'row-key')


