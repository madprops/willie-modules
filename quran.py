import json
import urllib
from willie.module import commands

@commands('quran')
def quran(bot, trigger, found_match=None):
	url = "http://quranapi.azurewebsites.net/api/verse/?lang=en"
	response = urllib.urlopen(url)
	content = response.read()
	json_data = json.loads(content.decode('utf8'))
	verse = json_data['Text']
	bot.say(verse)
