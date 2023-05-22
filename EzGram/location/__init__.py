from instagrapi import Client

class Location:
    def __init__(self, api):
        self.api = api
    
    def search_location(self, query):
        locations = self.api.location_search(query)
        return locations
    
    def get_location_feed(self, location_id):
        feed = self.api.location_feed(location_id)
        return feed
    
    def get_location_info(self, location_id):
        info = self.api.location_info(location_id)
        return info
    
    def get_location_stories(self, location_id):
        stories = self.api.location_stories(location_id)
        return stories
    
    def get_location_media(self, location_id):
        media = self.api.location_medias(location_id)
        return media
