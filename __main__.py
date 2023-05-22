from instagrapi import Client

class EzGram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.api = None

    def login(self):
        self.api = Client()
        self.api.login(self.username, self.password)

    def get_user_followers(self, username=None, user_id=None):
        if username is None and user_id is None:
            if self.username is None:
                raise ValueError("Either 'username' or 'user_id' must be provided.")
            user_id = self.api.user_id_from_username(self.username)
        followers = self.api.user_followers(user_id)
        return followers

    def get_user_following(self, username=None, user_id=None):
        if username is None and user_id is None:
            if self.username is None:
                raise ValueError("Either 'username' or 'user_id' must be provided.")
            user_id = self.api.user_id_from_username(self.username)
        following = self.api.user_following(user_id)
        return following

    def get_user_posts(self, username=None, user_id=None):
        if username is None and user_id is None:
            if self.username is None:
                raise ValueError("Either 'username' or 'user_id' must be provided.")
            user_id = self.api.user_id_from_username(self.username)
        posts = self.api.user_feed(user_id)
        return posts

    def logout(self):
        if self.api is not None:
            self.api.logout()

# Example usage:
ez_gram = EzGram('your_username', 'your_password')
ez_gram.login()

followers = ez_gram.get_user_followers(username='target_username')
print("User Followers:", followers)

following = ez_gram.get_user_following(username='target_username')
print("User Following:", following)

posts = ez_gram.get_user_posts(username='target_username')
print("User Posts:", posts)

ez_gram.logout()
