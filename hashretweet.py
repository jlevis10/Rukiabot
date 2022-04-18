import tweepy
import random
from apiclass import ApiClass

class HashRetweet:

    def __init__(self, name = 0):
        self.name = 'HashRetweet'

    def retweet(self, hashtag, api):
        tweets = api.search_tweets(q=hashtag, count=100)
        lst1 = []
        lst2 = []
        for tweet in tweets:
            id = tweet.id
            lst1.append(id)

        rand_id = lst1[random.randint(0, len(lst1) - 1)]
        try:
            if rand_id not in lst2:
                lst2.append(rand_id)
                api.retweet(rand_id)
                print('Tweet retweeted successfully')
        except:
            print('Tweet already retweeted')
