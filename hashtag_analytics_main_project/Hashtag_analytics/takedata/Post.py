__author__ = 'Nehemiah'

class Post:
    """Create a Posts object to aggregate posing data for analysis"""
    def __init__(self, post_id):
        self.post_id = post_id
        self.tags = set()

    def add_hashtag(self, hashtag):
        """adds a hashtag to a post"""
        self.tags.add(hashtag)

    def get_hashtags(self):
        """Returns the hashtags in a post"""
        return self.tags

    def get_id(self):
        """Returns the hashtags in a post"""
        return self.post_id
