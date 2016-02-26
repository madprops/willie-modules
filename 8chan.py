import json
import random
import urllib2
from bs4 import BeautifulSoup
from willie.module import commands

@commands('8chan', '8ch', 'news')
def random_8chan_comment(bot, trigger, found_match=None):

    if trigger.is_privmsg:
        return

    tries = 0
    keep_going = True

    while(keep_going):

        try: 
            tries += 1
            bot.say(get_comment(bot, trigger))
            return True

        except:
            if tries > 10:
                keep_going = False
            else:
                continue

def get_comment(bot, trigger):

    if trigger == '.news':
        base_url = 'https://8ch.net/n/'
    else:
        urls = []
        urls.append('https://8ch.net/tech/')
        urls.append('https://8ch.net/kind/')
        urls.append('https://8ch.net/pol/')
        urls.append('https://8ch.net/vg/')
        urls.append('https://8ch.net/leftypol/')
        urls.append('https://8ch.net/n/')
        base_url = random.choice(urls)
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers= {'User-Agent':user_agent,} 

    request = urllib2.Request(base_url + 'threads.json', None, headers) 
    response = json.load(urllib2.urlopen(request))
    page = random.choice(response)
    thread_number = random.choice(page['threads'])['no']

    url = base_url + 'res/' + str(thread_number) + '.json'
    request = urllib2.Request(url, None, headers) 
    response = json.load(urllib2.urlopen(request))

    post = response['posts'][0]
    post_url = base_url + 'res/' + str(thread_number) + '.html'
    soup = BeautifulSoup(post['com'])
    comment = u' '.join(soup.findAll(text=True))[:300]
    msg = comment + ' ' + post_url
    return msg
