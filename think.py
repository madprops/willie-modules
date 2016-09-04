import time
import json
import random
import urllib
from willie.module import commands

@commands('think')
def think(bot, trigger, found_match=None):

	subject = None
	if ' about ' in trigger:
		subject = trigger.replace('.think about ', '')
		subject = subject.replace(' ', ',') 
		subject = subject.replace(' and ', ',') 
		if subject[-1] == ',':
			subject = subject[:-1]

	tries = 0

	while tries < 3:

		n = random.randint(0, 17)

		if n > 8:
			if subject:
				url = "https://www.reddit.com/r/showerthoughts/search.json?q=" + subject + "&limit=18&sort=top&restrict_sr=true"
			else:
				url = "http://www.reddit.com/r/showerthoughts/top/.json?limit=18"
		else:
			if subject:
				url = "https://www.reddit.com/r/showerthoughts/search.json?q=" + subject + "&limit=18&sort=new&restrict_sr=true"
			else:
				url = "http://www.reddit.com/r/showerthoughts/new/.json?limit=18"

		try:
			response = urllib.urlopen(url)
			content = response.read()
			json_data = json.loads(content.decode('utf8'))
			children = json_data['data']['children']
			root = random.choice(children)['data']
			title = root['title']
			bot.say(title)
			return

		except:
			time.sleep(2)
			tries += 1
			pass

	bot.say('I have no thoughts on that awful subject.')