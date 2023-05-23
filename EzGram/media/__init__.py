from instagrapi.exceptions import ClientError

class Media:
    def __init__(self, api):
        self.api = api
    
    def get_media_info(self, media_id):
        try:
            media_info = self.api.media_info(media_id)
            return media_info
        except ClientError as e:
            print(f"Error: {e}")
    
    def get_media_comments(self, media_id):
        try:
            comments = self.api.media_comments(media_id)
            return comments
        except ClientError as e:
            print(f"Error: {e}")
    
    def get_media_likers(self, media_id):
        try:
            likers = self.api.media_likers(media_id)
            return likers
        except ClientError as e:
            print(f"Error: {e}")
    
    def get_media_saved(self, media_id):
        try:
            saved_users = self.api.media_saved(media_id)
            return saved_users
        except ClientError as e:
            print(f"Error: {e}")
    
    def like_media(self, media_id):
        try:
            self.api.media_like(media_id)
        except ClientError as e:
            print(f"Error: {e}")
    
    def unlike_media(self, media_id):
        try:
            self.api.media_unlike(media_id)
        except ClientError as e:
            print(f"Error: {e}")
    
    def get_user_tags(self, media_id):
        try:
            user_tags = self.api.media_user_tags(media_id)
            return user_tags
        except ClientError as e:
            print(f"Error: {e}")
    
    def get_location(self, media_id):
        try:
            location = self.api.media_location(media_id)
            return location
        except ClientError as e:
            print(f"Error: {e}")
    
    def get_user_clips(self, user_id):
        try:
            clips = self.api.user_clips_v1(user_id)
            return clips
        except ClientError as e:
            print(f"Error: {e}")

class ViewingAndEditingPublication(Media):
    def __init__(self, api):
        super().__init__(api)
    
    def get_media_info(self, media_id):
        return super().get_media_info(media_id)
    
    def get_media_comments(self, media_id):
        return super().get_media_comments(media_id)
    
    def get_media_likers(self, media_id):
        return super().get_media_likers(media_id)
    
    def get_media_saved(self, media_id):
        return super().get_media_saved(media_id)
    
    def like_media(self, media_id):
        super().like_media(media_id)
    
    def unlike_media(self, media_id):
        super().unlike_media(media_id)
    
    def get_user_tags(self, media_id):
        return super().get_user_tags(media_id)
    
    def get_location(self, media_id):
        return super().get_location(media_id)
    
    def get_user_clips(self, user_id):
        return super().get_user_clips(user_id)

class DownloadMedia(Media):
    def __init__(self, api):
        super().__init__(api)
    
    def download_media(self, media_id, path):
        try:
            self.api.media_download(media_id, path)
            print("Media downloaded successfully.")
        except ClientError as e:
            print(f"Error: {e}")
    
    def get_user_tags(self, media_id):
        return super().get_user_tags(media_id)
    
    def get_location(self, media_id):
        return super().get_location(media_id)
    
    def get_user_clips(self, user_id):
        return super().get_user_clips(user_id)

class UploadMedia(Media):
    def __init__(self, api):
        super().__init__(api)
    
    def upload_photo(self, path, caption=None):
        try:
            media_id = self.api.photo_upload(path, caption=caption)
            return media_id
        except ClientError as e:
            print(f"Error: {e}")
    
    def upload_video(self, path, caption=None):
        try:
            media_id = self.api.video_upload(path, caption=caption)
            return media_id
        except ClientError as e:
            print(f"Error: {e}")
    
    def upload_album(self, media_paths, caption=None):
        try:
            media_ids = self.api.album_upload(media_paths, caption=caption)
            return media_ids
        except ClientError as e:
            print(f"Error: {e}")
    
    def upload_igtv(self, path, title=None, caption=None, thumbnail=None):
        try:
            media_id = self.api.igtv_upload(path, title=title, caption=caption, thumbnail=thumbnail)
            return media_id
        except ClientError as e:
            print(f"Error: {e}")
    
    def upload_reel(self, path, caption=None, mention_user_ids=None, hashtags=None):
        try:
            media_id = self.api.reel_upload(path, caption=caption, mention_user_ids=mention_user_ids, hashtags=hashtags)
            return media_id
        except ClientError as e:
            print(f"Error: {e}")
    
    def delete_media(self, media_id):
        try:
            self.api.media_delete(media_id)
        except ClientError as e:
            print(f"Error: {e}")
    
    def comment_media(self, media_id, text):
        try:
            comment_id = self.api.media_comment(media_id, text)
            return comment_id
        except ClientError as e:
            print(f"Error: {e}")
    
    def delete_comment(self, media_id, comment_id):
        try:
            self.api.media_comment_delete(media_id, comment_id)
        except ClientError as e:
            print(f"Error: {e}")
    
    def get_extra_data(self, media_id):
        return super().get_extra_data(media_id)
