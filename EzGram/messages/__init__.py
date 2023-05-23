from instagrapi import Client

class DirectMessages(object):
    def __init__(self, api):
        self.api = api

    def send(self, user_id, message):
        return self.api.direct_send(message, user_id)
    
    def thread(self, thread_id):
        return self.api.direct_thread(thread_id)
    
    def inbox(self):
        return self.api.direct_inbox()
    
    def mark_item_as_seen(self, thread_id, item_id):
        return self.api.direct_thread_item_seen(thread_id, item_id)
