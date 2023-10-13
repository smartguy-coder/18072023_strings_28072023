import pymongo
from pprint import pprint
from datetime import datetime, timedelta

from config import USER, PASSWORD

url = f'mongodb+srv://{USER}:{PASSWORD}' \
      '@cluster0.vebb4r3.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url)

db = client.testDB
collection_products = db.products

# products = [
#     {
#         'title': 'bread2 time',
#         'price': 452,
#         'remains': 1002,
#         'comment': 'no sugar',
#         'contain_gluten': True,
#       'data': datetime.now() - timedelta(hours=5)
#     },
#     {
#         'title': 'soft drink2 time',
#         'price': 252,
#         'remains': 1002,
#         'comment': 'no sugar',
#         'contain_gluten': False,
#           'data': datetime.now() + timedelta(hours=5)
#     },
#     {
#         'title': 'milk2',
#         'price': 152,
#         'remains': 12,
#         'comment': 'no sugar',
#         'contain_gluten': True,
#     },
#     {
#         'title': 'vinegar2',
#         'price': 252,
#         'remains': 102,
#         'comment': 'no sugar',
#         'contain_gluten': False,
#     },
# ]
#
# collection_products.insert_many(products)

# analog find
# query = []
# response = collection_products.aggregate(query)
# for doc in response:
#     print(doc)
# print(list(response))


# $match stage
# query = [{'$match': {'contain_gluten': False}}]
# response = collection_products.aggregate(query)
# print(list(response))

# query = [{'$match': {'$and': [  # $or
#       {'contain_gluten': False},
#       {'price': {'$gte': 50}},
# ]}}]
# response = collection_products.aggregate(query)
# print(list(response))


# $group stage
# query = [
#       {
#             '$group': {'_id': '$contain_gluten'}
#       }
# ]
# response = collection_products.aggregate(query)
# print(list(response))

# query = [
#       {
#             '$group': {'_id': {'gluten': '$contain_gluten', 'price': '$price'}}
#       }
# ]
# response = collection_products.aggregate(query)
# print(list(response))


# $sum stage
# query = [
#       {
#             '$group': {'_id': '$contain_gluten', 'count': {'$sum': '$remains'}}
#       }
# ]
# response = collection_products.aggregate(query)
# print(list(response))

# query = [
#       {
#             '$group': {'_id': '$contain_gluten', 'count': {'$sum': '$remains'}}
#       }
# ]
# response = collection_products.aggregate(query)
# print(list(response))


# query = [
#       {
#             '$group': {
#                   '_id': '$contain_gluten',
#                   'count_remains': {'$sum': '$remains'},
#                   'naming_counter': {'$sum': 1}
#             }
#       }
# ]
# response = collection_products.aggregate(query)
# pprint(list(response))


# $project stage
# query = [
#       {
#             '$project': {
#                   '_id': 0,
#                   'contain_gluten': 1,
#                   'item_description': {'$concat': ['$title', ' - ', '$comment']},
#             }
#       }
# ]
# response = collection_products.aggregate(query)
# pprint(list(response))


#  COOL AGGREGATION

query = [
    {'$match': {'price': {'$gt': 12}}},

    {'$project': {
        'contain_gluten': 1,
        'data': 1,
        '_id': 0,
        'this_product_cost': {'$multiply': ['$price', '$remains']}}
    },

    {
        '$group': {
            '_id': '$contain_gluten',
            'total': {'$sum': '$this_product_cost'}
        }
    },
    {'$match': {'total': {'$gt': 500}}},
]

response = collection_products.aggregate(query)
pprint(list(response))
