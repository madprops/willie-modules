import time
import json
import random
import urllib
from willie.module import commands

@commands('til')
def til(bot, trigger, found_match=None):

	tries = 0

	while tries < 4:

		n = random.randint(0, 17)

		url = "http://www.reddit.com/r/todayilearned/top/.json?limit=18"

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