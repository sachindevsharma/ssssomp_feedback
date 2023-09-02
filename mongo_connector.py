from pymongo import MongoClient
import os
import json


class MongoConnector:
    
    def connect(self):
        USERNAME = os.environ.get("USERNAME", None)
        PASSWORD = os.environ.get("PASSWORD", None)

        if USERNAME is None or PASSWORD is None:
            secrets = json.load(open("url.txt", "r"))      # FOR LOCAL DEVELOPMENT
            USERNAME = secrets.get("USERNAME")
            PASSWORD = secrets.get("PASSWORD")

        MONGO_URL = f"mongodb+srv://{USERNAME}:{PASSWORD}"
        MONGO_URL += "@ssssomp.pbugdaw.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(MONGO_URL)
        return client
    
    def get_database(self, db):
        client = self.connect() 
        return client[db]   
    
    def get_collection(self, db, collection):
        client = self.connect() 
        return client[db][collection]  
    