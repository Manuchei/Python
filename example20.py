import pymongo

mongoClient = pymongo.MongoClient('mongodb://10.101.11.30:27018/')
mongoDB=mongoClient['animals']
print(mongoDB)

mongoCollection=mongoDB['animals']
for animal in mongoCollection.find():
    print(animal)

    mongoClient.close()