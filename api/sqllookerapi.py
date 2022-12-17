#Created by AcnSoft - Arda Çalışkan
#github.com/acnsoft
#instagram.com/acnsoft



import requests
from colorama import Fore
import urllib
import pandas as pd
from requests_html import HTML
from requests_html import HTMLSession


COLORS = {\
"black":"\u001b[30;1m",
"red": "\u001b[31;1m",
"green":"\u001b[32m",
"yellow":"\u001b[33;1m",
"blue":"\u001b[34;1m",
"magenta":"\u001b[35m",
"cyan": "\u001b[36m",
"white":"\u001b[37m",
"yellow-background":"\u001b[43m",
"black-background":"\u001b[40m",
"cyan-background":"\u001b[46;1m",
}


def colorText(text):
    for color in COLORS:
        text = text.replace("[[" + color + "]]", COLORS[color])
    return text

dort = "[[red]]Your dork type >>> [[white]]"
redd = colorText(dort)

bort = "[[red]]Your dork type >>> [[white]]"
green = colorText(bort)









def get_source(url):
   try:
     session = HTMLSession()
     response = session.get(url)
     return response
   except requests.exceptions.RequestException as e:
      print(e)


class sqllookerapi():

  def sqllooker(settarget):
    target = settarget
    dorkch = str(input(redd))

    query = urllib.parse.quote_plus(f"{dorkch} site:{target}")
 
    response = get_source("https://www.google.co.uk/search?q="+query)
 
    links = list(response.html.absolute_links)
 
    google_domains = (
      'https://www.google.',
      'https://google.',
      'https://webcache.googleusercontent.',
      'http://webcache.googleusercontent.',
      'https://policies.google.',
      'https://support.google.',
      'https://maps.google.',
      'https://translate.google.co.uk')
 
    for url in links[:]:
 
     if url.startswith(google_domains):
 
      links.remove(url)
 
    for i in links:
 
     print(i)
