import tweepy

class ApiClass:
    def __init__(self, API_key, API_key_secret, access_token, access_token_secret):
        self.API_key = API_key
        self.API_key_secret = API_key_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def authenticate(self, API_key, API_key_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(API_key, API_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        return api
