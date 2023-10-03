import os
import json

# url.txt will contain data as below
# {"USERNAME": "username", 
#  "PASSWORD": "password", 
#  "DATABASE_NAME": "db",
#  "FEEDBACK_COLLECTION": "col1",
#  "QUESTIONS_COLLECTION": "col2"}

class Config:

    def _get_secrets(self):
        secrets = json.load(open("url.txt", "r"))  # FOR LOCAL DEVELOPMENT
        return secrets
    
    @property
    def is_local(self):
        if "PASSWORD" in os.environ.keys() and "DATABASE_NAME" in os.environ.keys():
            return False
        else:
            return True

    @property
    def USERNAME(self):
        if self.is_local:
            return self._get_secrets().get("USERNAME")
        else:
            return os.environ.get("USERNAME")
    
    @property
    def PASSWORD(self):
        if self.is_local:
            return self._get_secrets().get("PASSWORD")
        else:
            return os.environ.get("PASSWORD")
    
    @property
    def DATABASE_NAME(self):
        if self.is_local:
            return self._get_secrets().get("DATABASE_NAME")
        else:
            return os.environ.get("DATABASE_NAME")
    
    @property
    def FEEDBACK_COLLECTION(self):
        if self.is_local:
            return self._get_secrets().get("FEEDBACK_COLLECTION")
        else:
            return os.environ.get("FEEDBACK_COLLECTION")
        
    @property
    def QUESTIONS_COLLECTION(self):
        if self.is_local:
            return self._get_secrets().get("QUESTIONS_COLLECTION")
        else:
            return os.environ.get("QUESTIONS_COLLECTION")
