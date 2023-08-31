from pymongo import MongoClient
import os


class MongoConnector:
    
    def connect(self):
        if "MONGO_URL" in os.environ:
            MONGO_URL = os.environ.get("MONGO_URL")
        else:
            MONGO_URL = open("url.txt", "r").read()         # FOR LOCAL DEVELOPMENT
        client = MongoClient(MONGO_URL)
        return client
    
    def get_database(self, db):
        client = self.connect() 
        return client[db]   
    
    def get_collection(self, db, collection):
        client = self.connect() 
        return client[db][collection]  
    