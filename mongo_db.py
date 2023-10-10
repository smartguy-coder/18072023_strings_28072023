import pymongo
from bson import Decimal128

from config import USER, PASSWORD

url = f'mongodb+srv://{USER}:{PASSWORD}' \
      '@cluster0.vebb4r3.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url)

db = client.testDB
mops_coll = db.mops
vacuum_cleaners_coll = db.vacuum_cleaners

# add single document ##########################################
# mops_coll.insert_one(
#       {'title': 'Super mop', 'price': 15}
# )
#
# vacuum_cleaners_coll.insert_one(
#       {'title': 'vacuum cleaner', 'price': 150,
#        'power': 2000}
# )

# mops_coll.insert_one(
#       {'_id': 2, 'title': 'Super mop', 'price': 15}
# )

# add many documents ##########################################
# mops = [
#     {'_id': 65656, 'title': 'fffffffff mop3', 'price': 1228},
#     {'title': 'Super mop4', 'price': 22, 'features': ['speed', 'power']},
# ]
# mops_coll.insert_many(mops)

# GET DATA *************************************************
# first
# result = mops_coll.find_one()
# result = mops_coll.find_one({'_id': 10})  # by field
# result = mops_coll.find_one({'price': 18})  # by field
# print(result)

# all data
# result = mops_coll.find()
# print(result)
# for doc in result:
#       print(doc)

# looking for the specific field
# query = {'price': 22}
# query = {'price': {'$gt': 15}}
# query = {'title': {'$regex': 'Su*'}}
# query = {'title': {'$regex': r'er22\b'}}
# query = {'title': {'$regex': r'er\b'}, 'price': {'$gte': 15}}
# query = {'title': {'$regex': r'er\b'}, 'price': {'$lte': 15}}

# result = mops_coll.find(query)
# result = mops_coll.find(query).limit(2)
# result = mops_coll.find(query).sort('price').limit(2)
# result = mops_coll.find(query).sort('price', -1).limit(25)
# for doc in result:
#       print(doc)

# UPDATE
#  use $set
# current = {'title': 'Super2 mop'}
# new_data = {'$set': {'brand': 'Samsung2'}}
# data = mops_coll.update_one(current, new_data)
# print(data.raw_result)

# current = {'title': 'Super mop3'}
# new_data = {'$set': {'battery_capacity': 10000}}
# data = mops_coll.update_many(current, new_data)
# print(data.raw_result)

# current = {}
# new_data = {'$set': {'warranty': 3}}
# data = mops_coll.update_many(current, new_data)
# print(data.raw_result)


# multiplication
query = {}
# operation = {'$mul': {'price': 1.1}}  # bad idea
operation = {'$mul': {'price': 1.1}}
data = mops_coll.update_many(query, operation)
print(data.raw_result)












