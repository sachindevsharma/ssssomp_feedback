import os
import json


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
    def COLLECTION_NAME(self):
        if self.is_local:
            return self._get_secrets().get("COLLECTION_NAME")
        else:
            return os.environ.get("COLLECTION_NAME")
