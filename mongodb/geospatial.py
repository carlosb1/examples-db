from pymongo import MongoClient, GEO2D

client = MongoClient('localhost', 27017, username='testadmin', password='password')
db = client.geo_example
print db.places.create_index([("loc", GEO2D)])

result = db.places.insert_many ([{"loc": [2, 5]},
        {"loc":[30, 5]},
        {"loc":[1, 2]},
        {"loc":[4, 4]}])
print result.inserted_ids

import pprint

for doc in db.places.find({"loc": {"$near":[3,6]}}).limit(3):
    pprint.pprint(doc)

from bson.son import SON
query = {"loc": SON([("$near",[3, 6]), ("$maxDistance", 100)])}
for doc in db.places.find(query).limit(3):
    pprint.pprint(doc)

query = {"loc": {"$within": {"$center":[[0, 0], 6]}}}
for doc in db.places.find(query).sort('_id'):
    pprint.pprint(doc)

from bson.son import SON
print db.command(SON([('geoNear', 'places'),('near', [1,2])]))

