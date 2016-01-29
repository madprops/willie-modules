import time
import json
import urllib
from willie.module import commands

@commands('bible')
def bible(bot, trigger, found_match=None):
	url = "http://labs.bible.org/api/?passage=random"
	response = urllib.urlopen(url)
	content = response.read()
	content = content.replace('<b>', '')
	content = content.replace('</b>', '')
	bot.say(content)
	return
