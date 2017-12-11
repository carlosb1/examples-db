from pymongo import MongoClient
import gridfs

client = MongoClient('localhost', 27017, username='testadmin', password='password')
db = client.gridfs.example
fs = gridfs.GridFS(db)
a = fs.put(b"hello world")
print fs.get(a).read()

b = fs.put(fs.get(a), filename="a", bar="bar")
out = fs.get(b)
print out.read()
print out.bar
print out.upload_date
