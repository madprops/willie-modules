import re
import random
import urllib2
from willie.module import commands

# if it doesn't exist, create a sqlite database 
# and create this table CREATE TABLE laters(id integer primary key, sender text, receiver text, message text, date text);

@commands('lewd')
def lewd(bot, trigger, found_match=None):
    if trigger.is_privmsg:
        return
    try:
        urls = []
        urls.append('https://danbooru.donmai.us/posts/random?tags=nipples')
        urls.append('https://danbooru.donmai.us/posts/random?tags=pussy')
        urls.append('https://danbooru.donmai.us/posts/random?tags=ass')
        urls.append('https://danbooru.donmai.us/posts/random?tags=sex')
        urls.append('https://danbooru.donmai.us/posts/random?tags=nude')
        response = urllib2.urlopen(random.choice(urls))
        url = response.geturl().split('?')[0]
        bot.say(url)
    except:
        bot.say('something went wrong, ' + str(random.randint(1,1000)) + ' children have been sacrificed')
