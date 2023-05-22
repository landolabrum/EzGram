from instagrapi import Client
from instagrapi.exceptions import ChallengeRequired
from instagrapi.types import ChallengeMethod

# account = EzGram('your_username', 'your_password').account
# inbox, account_info = account.login(enable_2fa=True)
# print("News Inbox:", inbox)
# print("Account Info:", account_info)


from instagrapi.types import InboxType

class Account:
    def __init__(self):
        self.api = None
    
    def login(self, enable_2fa=False):
        self.api = Client()
        self.api.login(self.api.username, self.api.password)
        
        if enable_2fa:
            self.two_factor(enable=True)
        
        return self.news_inbox_v1(), self.account_info()
    
    def login_info(self):
        login_info = self.api.login_info()
        return login_info
    
    def edit_profile(self, **kwargs):
        profile_info = self.api.account_edit(**kwargs)
        return profile_info
    
    def change_password(self, old_password, new_password):
        self.api.change_password(old_password, new_password)
    
    def two_factor(self, enable=False, identifier=None, method=ChallengeMethod.EMAIL):
        if enable:
            if identifier is None:
                identifier = self.api.username
            
            self.api.request_challenge_code(method, identifier=identifier)
            code = input("Enter the verification code: ")
            self.api.verify_request_challenge_code(code, identifier=identifier)
        
        else:
            self.api.disable_two_factor()
    
    def logout(self):
        self.api.logout()
        self.api = None
    
    def news_inbox_v1(self, mark_as_seen=False):
        inbox = self.api.news_inbox_v1(mark_as_seen=mark_as_seen)
        return inbox
    
    def account_info(self):
        account = self.api.account_info(self.api.authenticated_user_id)
        return account
