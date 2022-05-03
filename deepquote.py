import tweepy
import random
import os
from PIL import Image, ImageFont, ImageDraw

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
            index3 = text.find('@')
            if (index == -1):
                if (index2 == -1):
                    if index3 == -1:
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

        quote = quote.split()
        for i in range (len(quote)):
            if i != 0:
                if (i % 8 == 0):
                    quote[0] = ' ' + quote[0]
                    quote[i] = quote[i] + '\n'
        quote = ' '.join(quote)


        n = random.randint(1, 28)
        str1 = '0' * n
        dir = os.getcwd()
        image = Image.open(dir + '\\images' + '\\' + str1 + '.jpg')
        font = ImageFont.truetype('AlexBrush-Regular.ttf', 50)
        text = quote
        draw = ImageDraw.Draw(image)
        draw.text((20, 250), text, (255, 255, 255), font=font)
        image.save('quotepicture.jpg')
        try:
            media = api.media_upload('quotepicture.jpg')
            api.update_status(media_ids=[media.media_id], status='Quote of the day:')
            print('Uploaded quote of the day')
        except:
            print("Error uploading image")
        os.remove('quotepicture.jpg')