# Get the database using the method we defined in pymongo_test_insert file
from mongodbcreate import get_database

dbname = get_database()
collection_name = dbname["user_1_items"]

item_1 = {
    "_id": "U1IT00001",
    "item_name": "Blender",
    "max_discount": "10%",
    "batch_number": "RR450020FRG",
    "price": 340,
    "category": "kitchen appliance"
}

item_2 = {
    "_id": "U1IT00002",
    "item_name": "Egg",
    "category": "food",
    "quantity": 12,
    "price": 36,
    "item_description": "brown country eggs"
}

collection_name.insert_many([item_1, item_2])

from dateutil import parser

expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
item_3 = {
    "item_name": "Bread",
    "quantity": 2,
    "ingredients": "all-purpose flour",
    "expiry_date": expiry
}
collection_name.insert_one(item_3)

item_4 = {
    "id": "U1ITtest1",
    "item_name": "Blender",
    "max_discount": "10%",
    "batch_number": "RR450020FRG",
    "price": 340,
    "category": "kitchen appliance",
    "bebas": "bebas"
}
collection_name.insert_one(item_4)
