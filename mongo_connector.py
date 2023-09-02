from pymongo import MongoClient
import os


class MongoConnector:
    
    def connect(self):
        USERNAME = os.environ.get("USERNAME", None)
        PASSWORD = os.environ.get("PASSWORD", None)

        if USERNAME is None:
            MONGO_URL = open("url.txt", "r").read()        # FOR LOCAL DEVELOPMENT
        url = f"mongodb+srv://{USERNAME}:{PASSWORD}@ssssomp.pbugdaw.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient("MONGO_URL")
        return client
    
    def get_database(self, db):
        client = self.connect() 
        return client[db]   
    
    def get_collection(self, db, collection):
        client = self.connect() 
        return client[db][collection]  
    