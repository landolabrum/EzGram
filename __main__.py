from instagram_private_api import Client, ClientCompatPatch
from datetime import datetime, timedelta

class EzGram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.api = None

    def login(self):
        self.api = Client(self.username, self.password)
        self.api.login()
        ClientCompatPatch.api(self.api)

    def get_saved_media(self, media_type=None, start_date=None, end_date=None, username=None, caption=None, location=None, hashtags=None, users_tagged=None, likers=None, tagged=None, comments=None, likes=None, link_url=None):
        if start_date is not None and end_date is not None:
            start_date = datetime.now() - timedelta(seconds=start_date)
            end_date = datetime.now() - timedelta(seconds=end_date)

        user_id = self.api.username_id(username) if username else self.api.authenticated_user_id
        saved_media = self.api.user_saved_feed(user_id)

        filtered_media = []
        for media in saved_media:
            media_time = datetime.fromtimestamp(media['taken_at'])
            if media_type is None or media_type.lower() == media.get('media_type', '').lower():
                if start_date is None or start_date <= media_time <= end_date:
                    if caption and caption.lower() not in media.get('caption', '').lower():
                        continue
                    if location and location.lower() not in media.get('location', '').lower():
                        continue
                    if hashtags:
                        media_hashtags = [tag['name'].lower() for tag in media.get('tags', [])]
                        if not set(hashtags).issubset(set(media_hashtags)):
                            continue
                    if users_tagged:
                        media_users_tagged = [tagged_user['user']['username'].lower() for tagged_user in media.get('usertags', [])]
                        if not set(users_tagged).issubset(set(media_users_tagged)):
                            continue
                    if likers:
                        media_likers = [liker['username'].lower() for liker in media.get('likers', [])]
                        if not set(likers).issubset(set(media_likers)):
                            continue
                    if tagged:
                        media_tagged = [tag['user']['username'].lower() for tag in media.get('usertags', [])]
                        if not set(tagged).issubset(set(media_tagged)):
                            continue
                    if comments is not None and media.get('comment_count', 0) != comments:
                        continue
                    if likes is not None and media.get('like_count', 0) != likes:
                        continue
                    if link_url and link_url not in media.get('link', ''):
                        continue

                    filtered_media.append(media)

        return filtered_media

    # Function for getting user posts
    def get_user_posts(self, username=None, user_id=None, caption=None, location=None, hashtags=None, users_tagged=None, likers=None, tagged=None, comments=None, likes=None, link_url=None):
        if username is None and user_id is None:
            if self.username is None:
                raise ValueError("Either 'username' or 'user_id' must be provided.")
            user_id = self.api.username_info(self.username)['user']['pk']
        
        user_posts = self.api.user_feed(user_id)

        filtered_posts = []
        for post in user_posts:
            if caption and caption.lower() not in post.get('caption', '').lower():
                continue
            if location and location.lower() not in post.get('location', '').lower():
                continue
            if hashtags:
                post_hashtags = [tag['name'].lower() for tag in post.get('tags', [])]
            if not set(hashtags).issubset(set(post_hashtags)):
                continue
            if users_tagged:
                post_users_tagged = [tagged_user['user']['username'].lower() for tagged_user in post.get('usertags', [])]
            if not set(users_tagged).issubset(set(post_users_tagged)):
                continue
            if likers:
                post_likers = [liker['username'].lower() for liker in post.get('likers', [])]
            if not set(likers).issubset(set(post_likers)):
                continue
            if tagged:
                post_tagged = [tag['user']['username'].lower() for tag in post.get('usertags', [])]
            if not set(tagged).issubset(set(post_tagged)):
                continue
            if comments is not None and post.get('comment_count', 0) != comments:
                continue
            if likes is not None and post.get('like_count', 0) != likes:
                continue
            if link_url and link_url not in post.get('link', ''):
                continue
        filtered_posts.append(post)

        return filtered_posts

    # Function for getting user stories
    def get_user_stories(self, username=None, user_id=None, location=None, hashtags=None, users_tagged=None, link_url=None):
        if username is None and user_id is None:
            if self.username is None:
                raise ValueError("Either 'username' or 'user_id' must be provided.")
            user_id = self.api.username_info(self.username)['user']['pk']

        user_stories = self.api.user_story_feed(user_id)

        filtered_stories = []
        for story in user_stories.get('reel', []):
            if location and location.lower() not in story.get('location', '').lower():
                continue
            if hashtags:
                story_hashtags = [tag['name'].lower() for tag in story.get('tags', [])]
                if not set(hashtags).issubset(set(story_hashtags)):
                    continue
            if users_tagged:
                story_users_tagged = [tagged_user['user']['username'].lower() for tagged_user in story.get('user_tags', [])]
                if not set(users_tagged).issubset(set(story_users_tagged)):
                    continue
            if link_url and link_url not in story.get('link', ''):
                continue

            filtered_stories.append(story)

        return filtered_stories

    # Function for getting user reels
    def get_users_reels(self, usernames, location=None, hashtags=None, users_tagged=None, link_url=None):
        reels = []
        for username in usernames:
            user_reels = self.api.user_reel_media(self.api.username_id(username))

            filtered_reels = []
            for reel in user_reels.get('reel', []):
                if location and location.lower() not in reel.get('location', '').lower():
                    continue
                if hashtags:
                    reel_hashtags = [tag['name'].lower() for tag in reel.get('tags', [])]
                    if not set(hashtags).issubset(set(reel_hashtags)):
                        continue
                if users_tagged:
                    reel_users_tagged = [tagged_user['user']['username'].lower() for tagged_user in reel.get('user_tags', [])]
                if not set(users_tagged).issubset(set(reel_users_tagged)):
                    continue
                if link_url and link_url not in reel.get('link', ''):
                    continue


            filtered_reels.append(reel)

        reels.append(filtered_reels)

        return reels

    # Function for getting user direct messages
    def get_users_direct_messages(self):
        direct_messages = self.api.direct_v2_inbox()
        return direct_messages
    
    def logout(self):
        if self.api is not None:
            self.api.logout()


ez_gram = EzGram('your_username', 'your_password')
ez_gram.login()

# Get filtered user posts
filtered_posts = ez_gram.get_user_posts(username='target_username', location='New York', hashtags=['summer', 'vacation'])
print("Filtered User Posts:", filtered_posts)

# Get filtered user stories
filtered_stories = ez_gram.get_user_stories(username='target_username', location='Los Angeles', users_tagged=['friend1', 'friend2'])
print("Filtered User Stories:", filtered_stories)

# Get filtered users' reels
usernames = ['user1', 'user2', 'user3']
filtered_reels = ez_gram.get_users_reels(usernames, location='London', link_url='https://example.com')
for username, reels in zip(usernames, filtered_reels):
    print(f"{username}'s Filtered Reels:", reels)

ez_gram.logout()
