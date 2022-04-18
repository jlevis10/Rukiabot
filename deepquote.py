import tweepy
import random

class DeepQuote():

    def __init__(self, name = 0):
        self.name = 'DeepQuote'

    def generate(self, api):

        lst1 = []
        tweets = api.user_timeline(screen_name='inspowerminds', count=100, include_rts=False, tweet_mode='extended')
        for tweet in tweets:
            # filters out tweets/rewteets that are promotional material
            text = tweet.full_text
            index = text.find("https")
            index2 = text.find('\'')
            if (index == -1):
                if (index2 == -1):
                    lst1.append(text)

        lst2 = []
        for x in lst1:
            # remove authors of the quotes
            index = x.find("-")
            if (index != -1):
                lst2.append(x[:index + 1])
            else:
                lst2.append(x + ' -')


        lst_authors = ["Ken Kaneki", "Eren Yeager", "Gojo Satoru", "Megumi Fushiguro", "Rukia Kuchiki", "Monkey D. Luffy", "Roronoa Zoro", "Naruto Uzumaki", "Kakashi Hatake", "Shouto Todoroki"]
        quote_index1 = random.randint(0, len(lst2) - 1)
        quote_index2 = random.randint(0, len(lst_authors) - 1)
        quote = lst2[quote_index1] + " " + lst_authors[quote_index2]
        return quote

