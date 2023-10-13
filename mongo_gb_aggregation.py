import pymongo

from config import USER, PASSWORD

url = f'mongodb+srv://{USER}:{PASSWORD}' \
      '@cluster0.vebb4r3.mongodb.net/?retryWrites=true&w=majority'

client = pymongo.MongoClient(url)

db = client.testDB

collection_products = db.products

products = [
    {
        'title': 'bread',
        'price': 45,
        'remains': 10,
        'comment': 'no sugar',
        'contain_gluten': True,
    },
    {
        'title': 'soft drink',
        'price': 25,
        'remains': 100,
        'comment': 'no sugar',
        'contain_gluten': False,
    },
    {
        'title': 'milk',
        'price': 15,
        'remains': 1,
        'comment': 'no sugar',
        'contain_gluten': True,
    },
    {
        'title': 'vinegar',
        'price': 25,
        'remains': 10,
        'comment': 'no sugar',
        'contain_gluten': False,
    },
]

collection_products.insert_many(products)
