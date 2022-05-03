import random
import tweepy

class Functions:
    def __init__(self, hashtag, searchterm, tweet_text, api):
        self.hashtag = hashtag
        self.searchterm = searchterm
        self.tweet_text = tweet_text
        self.api = api


    def tweet(self, tweet_text, api):
        api.update_status(tweet_text)
        print('Tweeted: ' + tweet_text)



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



    def like_reply(self, searchterm, tweet_text, api):
        tweets = api.search_tweets(q=searchterm, count=3)
        lst = []
        for tweet in tweets:
            id = tweet.id
            status = api.get_status(id)
            try:
                if id not in lst:
                    lst.append(id)
                    api.create_favorite(id)
                    api.update_status(status=tweet_text, in_reply_to_status_id=id, auto_populate_reply_metadata=True)
                    print('Liked and Replied to: ' + status.text)
            except:
                print('Already Replied to: ' + status.text)



    def delete_all_tweets(self, api):
        for status in tweepy.Cursor(api.user_timeline).items():
            try:
                api.destroy_status(status.id)
            except:
                pass


