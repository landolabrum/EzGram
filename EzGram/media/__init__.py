from instagrapi import Client
from instagrapi.types import MediaTypes

class Media:
    def __init__(self, ez):
        self.ez = ez
    
    def upload_photo(self, path, caption=None):
        media_id = self.ez.api.photo_upload(path, caption=caption)
        return media_id
    
    def upload_video(self, path, caption=None):
        media_id = self.ez.api.video_upload(path, caption=caption)
        return media_id
    
    def upload_album(self, media_paths, caption=None):
        media_ids = self.ez.api.album_upload(media_paths, caption=caption)
        return media_ids
    
    def upload_igtv(self, path, title=None, caption=None, thumbnail=None):
        media_id = self.ez.api.igtv_upload(path, title=title, caption=caption, thumbnail=thumbnail)
        return media_id
    
    def upload_reel(self, path, caption=None, mention_user_ids=None, hashtags=None):
        media_id = self.ez.api.reel_upload(path, caption=caption, mention_user_ids=mention_user_ids, hashtags=hashtags)
        return media_id
    
    def delete(self, media_id):
        self.ez.api.media_delete(media_id)
    
    def info(self, media_id):
        media_info = self.ez.api.media_info(media_id)
        return media_info
    
    def comment(self, media_id, text):
        comment_id = self.ez.api.media_comment(media_id, text)
        return comment_id
    
    def delete_comment(self, media_id, comment_id):
        self.ez.api.media_comment_delete(media_id, comment_id)
    
    def like(self, media_id):
        self.ez.api.media_like(media_id)
    
    def unlike(self, media_id):
        self.ez.api.media_unlike(media_id)
    
    def save(self, media_id):
        self.ez.api.media_save(media_id)
    
    def unsave(self, media_id):
        self.ez.api.media_unsave(media_id)
