import requests
from bs4 import BeautifulSoup
import os
from PIL import Image

class ImageDownloader:
    def __init__(self, name = 0):
        self.name = 'ImageDownloader'

    def download_image(self, url):
        try:
            os.mkdir(os.path.join(os.getcwd(), 'images'))
        except FileExistsError:
            pass

        os.chdir(os.path.join(os.getcwd(), 'images'))
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')

        img_tags = soup.find_all('img')

        img_tags.remove(img_tags[0])
        img_tags.remove(img_tags[0])

        n = '0'
        for img in img_tags:
            name = n
            src = img['src']
            with open(name + '.jpg', 'wb') as f:
                f.write(requests.get(src).content)
            n += '0'
