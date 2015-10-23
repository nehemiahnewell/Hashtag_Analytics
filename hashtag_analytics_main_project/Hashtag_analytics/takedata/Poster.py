from takedata.Post import Post
__author__ = 'Nehemiah'

class Poster:
    """Creates a Poster object to aggregate posts by poster"""
    def __init__(self, poster_id):
        self.poster_id = poster_id
        self.posts = []

    def add_post(self, post):
        """Adds a post to a poster"""
        thisPost = Post(post['id'])
        for tag in post['entities']['hashtags']:
            thisPost.add_hashtag(tag['text'].upper())
        self.posts.append(thisPost)

    def get_hashtags(self):
        """Get all tags used by poster"""
        tags_used = []
        for tweet in self.posts:
            tags_used.extend(list(tweet.get_hashtags()))
        return tags_used

    def get_unique_hashtags(self):
        """Get unique tag usage by poster"""
        tags_used = set()
        for tweet in self.posts:
            tags_used.update(tweet.get_hashtags())
        return list(tags_used)

    def get_user_id(self):
        """get the user id"""
        return self.poster_id
