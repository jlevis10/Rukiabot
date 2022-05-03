# importing libraries
import tweepy
import time
import random
import os
from haiku import Haiku
from deepquote import DeepQuote
from apiclass import ApiClass
from functions import Functions
from imagedownloader import ImageDownloader
from PIL import Image, ImageFont, ImageDraw


bot_1 = ApiClass('yqQbu4r2BAeIlS2iQLMmnMEKd', 'dN23yCaP62vwQkF1P6eXwOrsrIuiOUnh4Bkc7ensbhTwLWudrh', '1510381174849482758-NEcK4AJO5YmesOCIzjseVXVfqKkGSy', 'kbxUHs3psXff1qcAGBTLrpfzAQ7BVRWzMEbcsa0kocFjr')
api = bot_1.authenticate('yqQbu4r2BAeIlS2iQLMmnMEKd', 'dN23yCaP62vwQkF1P6eXwOrsrIuiOUnh4Bkc7ensbhTwLWudrh', '1510381174849482758-NEcK4AJO5YmesOCIzjseVXVfqKkGSy', 'kbxUHs3psXff1qcAGBTLrpfzAQ7BVRWzMEbcsa0kocFjr')




#Main function
if __name__ == '__main__':
    searchterm = 'northeastern'
    hashtag = '#familyfriendly'
    tweet_text = 'Testing profound-bot'
    url = 'https://iso.500px.com/the-top-20-nature-photos-on-500px-so-far-this-year/'
    main_dir = os.getcwd()

    h = Haiku()
    q = DeepQuote()
    f = Functions(hashtag, searchterm, tweet_text, api)
    IM = ImageDownloader()
    IM.download_image(url)

#This try statement is not required, however it is simply included to show whether the authentication of the bot was successful.
    try:
        api.verify_credentials()
        print("Authentication SUCCESS")
    except:
        print("Authentication FAILED")



    while True:

        try:
            f.tweet(tweet_text, api)
        except:
            pass

        time.sleep(5)

        f.retweet(hashtag, api)

        time.sleep(5)

        f.like_reply(searchterm, 'You should check out a great course on computer engineering, EECE2140!', api)

        time.sleep(5)

        f.tweet((h.generate(main_dir)), api)

        time.sleep(5)

        q.generate(api)

        #sleeps for a time between 5 minutes and 1 hour
        time.sleep(random.randint(60, 120))




print('End of program')
exit()