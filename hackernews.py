import json
import random
import urllib
import url
from willie.module import commands

@commands('hn')
def hn(bot, trigger, found_match=None):


	# url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
	# response = urllib.urlopen(url)
	# content = response.read()
	# json_data = json.loads(content.decode('utf8'))
	# id = json_data
	# root = random.choice(json_data)
	# bot.say('https://news.ycombinator.com/item?id=' + str(id))

	bot.say('asdf')

	trigger.raw = unicode.join(trigger.raw, ' http://memes.com')

	return url.title_auto(bot, trigger2)