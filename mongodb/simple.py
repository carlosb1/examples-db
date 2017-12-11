from pymongo import MongoClient
import pprint
import datetime
client = MongoClient('localhost', 27017, username='testadmin', 
                password='password')

db = client.test_database
collection = db.test_collection


post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }

posts = db.posts

post_id = posts.insert_one(post).inserted_id

print post_id

print db.collection_names(include_system_collections=False)


pprint.pprint(posts.find_one())

print posts.find_one({'_id': str(post_id)})

new_posts = [{"author": "Mike", "text": "Another post!"}, {"author": "Eliot", "text": "Another post 2!"}]

result  = posts.insert_many(new_posts)

print result.inserted_ids


for post in posts.find():
    pprint.pprint(post)


for post in posts.find({"author": "Mike"}):
    pprint.pprint(post)


print posts.count()

print posts.find({"author": "Mike"}).count()

d = datetime.datetime(2009,11,12,12)

for post in posts.find({"date": {"$lt" : d}}).sort("author"):
    pprint.pprint(post)






 
