from instagrapi import Client
from instagrapi.types import Location, MediaTypes

class User:
    def __init__(self, ez):
        self.ez = ez
    
    def info(self, username=None, user_id=None):
        if username is None and user_id is None:
            if self.ez.username is None:
                raise ValueError("Either 'username' or 'user_id' must be provided.")
            username = self.ez.username

        user_info = self.ez.api.user_info(username)
        return user_info

    def medias(self, username=None, user_id=None, amount=20):
        if username is None and user_id is None:
            if self.ez.username is None:
                raise ValueError("Either 'username' or 'user_id' must be provided.")
            username = self.ez.username

        medias = self.ez.api.user_medias(username, amount=amount)
        return medias

    def locations(self, username=None, user_id=None, amount=10):
        if username is None and user_id is None:
            if self.ez.username is None:
                raise ValueError("Either 'username' or 'user_id' must be provided.")
            username = self.ez.username

        locations = self.ez.api.user_locations(username, amount=amount)
        return locations

    def tagged(self, username=None, user_id=None, amount=10):
        if username is None and user_id is None:
            if self.ez.username is None:
                raise ValueError("Either 'username' or 'user_id' must be provided.")
            username = self.ez.username

        tagged = self.ez.api.user_tagged(username, amount=amount)
        return tagged

    def highlights(self, username=None, user_id=None):
        if username is None and user_id is None:
            if self.ez.username is None:
                raise ValueError("Either 'username' or 'user_id' must be provided.")
            username = self.ez.username

        highlights = self.ez.api.user_highlights(username)
        return highlights

    def search(self, query, amount=10):
        users = self.ez.api.user_search(query, amount=amount)
        return users
