from django.shortcuts import render
from django.http import HttpResponse
from takedata.views import search
from TwitterSearch import *
from collections import Counter
from takedata.Poster import Poster
import datetime
import savedata.models
from decimal import *

def list_to_dictionary(list):
    """Turns a list into a dictionary"""
    dictionary = {}
    for key in list:
        if key in dictionary:
            dictionary[key] += 1
        else:
            dictionary[key] = 1
    return dictionary

def add_tweet(tweet, users):
    #Set flag to false
    foundflag = False
    #check to see if this tweet is by a user already added. If yes, add the post to the user
    for poster in users:
        if poster.poster_id == tweet['user']['screen_name']:
            poster.add_post(tweet)
            foundflag = True
    #if no, add the user, then add the post to that user
    if foundflag == False:
        newposter = Poster(tweet['user']['screen_name'])
        newposter.add_post(tweet)
        users.append(newposter)

def count_hashtags(hashCount, uniqueHashCount, users):
    for poster in users:
        #add aggregate hashtags
        hashCount += Counter(list_to_dictionary(poster.get_hashtags()))
        #then just his unique ones
        uniqueHashCount += Counter(list_to_dictionary(poster.get_unique_hashtags()))

def save_data(keyword, hashCount, uniqueHashCount, tweets_searched, users_searched):
    searchkey = savedata.models.searchData(hashtag_searched=keyword, date_searched = datetime.date.today(),
                                           Tweets = tweets_searched)
    searchkey.save()
    hashCount.pop(keyword, None)
    uniqueHashCount.pop(keyword, None)
    for key in hashCount:
        try:
            perc = Decimal((hashCount[key]/tweets_searched)*100).quantize(Decimal('.01'), rounding=ROUND_DOWN)
        except InvalidOperation:
            pass
        try:
            perc_Post = Decimal((uniqueHashCount[key]/users_searched)*100).quantize(Decimal('.01'), rounding=ROUND_DOWN)
        except InvalidOperation:
            pass
        hash_use = savedata.models.hashtags(search = searchkey, hashtag_found = key, Count = hashCount[key],
                                            Percentage = perc, Posters = uniqueHashCount[key], Percentage_Posters =
                                            perc_Post)
        try:
            hash_use.save()
        except InvalidOperation:
            pass
    return searchkey.id

def perform_search(request):
    """Create a page that counts hashtags"""
    tag_to_search = ""
    if request.method == 'POST':
        tag_to_search = request.POST['search']
    keyword = '"#' + tag_to_search + '"'
    users = []
    postCount = 0
    hashCount = Counter()
    uniqueHashCount = Counter()

    #Now try and talk to twitter
    try:
        tso = TwitterSearchOrder()
        tso.set_keywords([keyword]) # This is the value we search for
        tso.set_include_entities(True) # This is to include entity information, like Hashtags

        # This is the actual search. Secrets and key's have to be obtained from twitter, and aren't to be shared.
        ts = TwitterSearch(
            consumer_key = 'xxx',
            consumer_secret = 'yyy',
            access_token = 'qqq',
            access_token_secret = 'rrr'
         )

        # This iterates through the found tweets
        for tweet in ts.search_tweets_iterable(tso):
            # count each tweet
            postCount += 1
            #Add the organize and record the tweets for later access
            add_tweet(tweet,users)
        #now count them
        count_hashtags(hashCount,uniqueHashCount,users)
        new_id = save_data(keyword.upper(),hashCount,uniqueHashCount,postCount,len(users))
    #catch errors
    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        return(str(e))

    #return that string
    return search(request, new_id)