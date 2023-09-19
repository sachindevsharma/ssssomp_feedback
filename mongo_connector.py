from pymongo import MongoClient
import os
import json


class MongoConnector:
    
    def connect(self):
        MONGO_URL = self._get_mongo_url() 
        try:       
            client = MongoClient(MONGO_URL)
        except:
            print("connecting local version")
            client = MongoClient("mongodb://localhost:27017/")

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        return client
    
    def get_database(self, db):
        client = self.connect() 
        return client[db]   
    
    def get_collection(self, db, collection):
        client = self.connect() 
        return client[db][collection]  
    
    def _get_mongo_url(self):
        USERNAME = os.environ.get("USERNAME", None)
        PASSWORD = os.environ.get("PASSWORD", None)

        if USERNAME is None or PASSWORD is None:
            secrets = json.load(open("url.txt", "r"))      # FOR LOCAL DEVELOPMENT
            USERNAME = secrets.get("USERNAME")
            PASSWORD = secrets.get("PASSWORD")

        MONGO_URL = f"mongodb+srv://{USERNAME}:{PASSWORD}"
        MONGO_URL += "@ssssomp.pbugdaw.mongodb.net/"
        MONGO_URL += "?retryWrites=true&w=majority"

        return MONGO_URL
    