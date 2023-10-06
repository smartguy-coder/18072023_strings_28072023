import pymongo

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
#     {'_id': 10, 'title': 'Super mop3', 'price': 18},
#     {'title': 'Super mop4', 'price': 22, 'features': ['speed', 'power']},
# ]
# mops_coll.insert_many(mops)

# GET DATA *************************************************