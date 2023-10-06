import pymongo

from config import USER, PASSWORD

url = f'mongodb+srv://{USER}:{PASSWORD}' \
      '@cluster0.vebb4r3.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url)

db = client.testDB
mops_coll = db.mops
vacuum_cleaners_coll = db.vacuum_cleaners

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