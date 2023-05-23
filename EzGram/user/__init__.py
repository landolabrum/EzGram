class User(object):
    def info(self, user_id):
        user_info = self.api.user_info(user_id)
        return user_info

    def medias(self, user_id, amount=20):
        medias = self.api.user_medias(user_id, amount=amount)
        return medias

    def locations(self, user_id, amount=10):
        locations = self.api.user_locations(user_id, amount=amount)
        return locations

    def tagged(self, user_id, amount=10):
        tagged = self.api.user_tagged(user_id, amount=amount)
        return tagged

    def highlights(self, user_id):
        highlights = self.api.user_highlights(user_id)
        return highlights

    def search(self, query, amount=10):
        users = self.api.user_search(query, amount=amount)
        return users

    def followers(self, user_id, amount=0):
        followers = self.api.user_followers(user_id, amount=amount)
        return followers

    def following(self, user_id, amount=0):
        following = self.api.user_following(user_id, amount=amount)
        return following

    def search_followers(self, user_id, query):
        search_result = self.api.search_followers(user_id, query)
        return search_result

    def search_following(self, user_id, query):
        search_result = self.api.search_following(user_id, query)
        return search_result

    def user_info(self, user_id):
        user_info = self.api.user_info(user_id)
        return user_info

    def user_info_by_username(self, username):
        user_info = self.api.user_info_by_username(username)
        return user_info

    def user_follow(self, user_id):
        result = self.api.user_follow(user_id)
        return result

    def user_unfollow(self, user_id):
        result = self.api.user_unfollow(user_id)
        return result

    def user_id_from_username(self, username):
        user_id = self.api.user_id_from_username(username)
        return user_id

    def username_from_user_id(self, user_id):
        username = self.api.username_from_user_id(user_id)
        return username

    def user_remove_follower(self, user_id):
        result = self.api.user_remove_follower(user_id)
        return result

    def mute_posts_from_follow(self, user_id):
        result = self.api.mute_posts_from_follow(user_id)
        return result

    def unmute_posts_from_follow(self, user_id):
        result = self.api.unmute_posts_from_follow(user_id)
        return result

    def mute_stories_from_follow(self, user_id):
        result = self.api.mute_stories_from_follow(user_id)
        return result

    def enable_posts_notifications(self, user_id):
        result = self.api.enable_posts_notifications(user_id)
        return result

    def disable_posts_notifications(self, user_id):
        result = self.api.disable_posts_notifications(user_id)
        return result

    def enable_videos_notifications(self, user_id):
        result = self.api.enable_videos_notifications(user_id)
        return result

    def disable_videos_notifications(self, user_id):
        result = self.api.disable_videos_notifications(user_id)
        return result

    def enable_reels_notifications(self, user_id):
        result = self.api.enable_reels_notifications(user_id)
        return result

    def disable_reels_notifications(self, user_id):
        result = self.api.disable_reels_notifications(user_id)
        return result

    def enable_stories_notifications(self, user_id):
        result = self.api.enable_stories_notifications(user_id)
        return result

    def disable_stories_notifications(self, user_id):
        result = self.api.disable_stories_notifications(user_id)
        return result

    def close_friend_add(self, user_id):
        result = self.api.close_friend_add(user_id)
        return result

    def close_friend_remove(self, user_id):
        result = self.api.close_friend_remove(user_id)
        return result
