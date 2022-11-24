import pymongo

mongoClient = pymongo.MongoClient('mongodb://10.101.30:27018/')
mongoDB=mongoClient['CentroEducativo']
mongoCollection=mongoDB['teachers']

doc={'name':'Pepe', 'email':'pepe@cebem.net'}
mongoCollection.insert_one(doc)
mongoClient.close()