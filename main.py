# import tuna
# import random
# tuna.fish()
# x= random.randrange(1, 1000)
# print(x)

import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,100)
    full_name = str(name)+ ".jpg"
    urllib.request.urlretrieve(url, full_name)
download_web_image('http://farm1.staticflickr.com/55/126255672_a3932a1831_o.jpg')