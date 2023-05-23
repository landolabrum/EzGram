from EzGram.user import User
from EzGram.account import Account
from EzGram.media import Media
from .messages import DirectMessages
from instagrapi import Client

class EzGram(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.api = Client()
    
    @property
    def user(self):
        return User(self)
    
    @property
    def account(self):
        return Account(self)
    
    @property
    def media(self):
        return Media(self)
    
    @property
    def direct_messages(self):
        return DirectMessages(self)
    

