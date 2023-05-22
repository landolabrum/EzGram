from instagrapi import Client

class Account:
    def __init__(self, ez):
        self.ez = ez
    
    def login_info(self):
        login_info = self.ez.api.login_info()
        return login_info
    
    def edit_profile(self, **kwargs):
        profile_info = self.ez.api.account_edit(**kwargs)
        return profile_info
    
    def change_password(self, old_password, new_password):
        self.ez.api.change_password(old_password, new_password)
    
    def two_factor(self, enable=False, identifier=None):
        if enable:
            totp = self.ez.api.get_totp(identifier)
            self.ez.api.enable_two_factor(totp)
        else:
            self.ez.api.disable_two_factor()
    
    def logout(self):
        self.ez.logout()
