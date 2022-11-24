import pymongo

mongoClient = pymongo.MongoClient('mongodb://localhost:27017/')
mongoDB=mongoClient['CentroEducativo']
print(mongoDB)

mongoCollection=mongoDB['camioneros']
for camionero in mongoCollection.find():
    print(camionero)

    mongoClient.close()