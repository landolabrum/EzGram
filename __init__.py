from EzGram.user import User
from EzGram.account import Account
from EzGram.media import Media

class EzGram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.ez = None
    
    @property
    def user(self):
        return User(self)
    
    @property
    def account(self):
        return Account(self)
    
    @property
    def media(self):
        return Media(self)