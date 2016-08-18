from willie.module import commands
from willie.tools import Identifier
import random

@commands('fmk')
def fmk(bot, trigger, found_match=None):

	nicks = trigger[5:].split(',')

	if trigger[5:].strip() == '':
		nicks = bot.privileges[Identifier(trigger.sender)].keys()
	else:
		if len(nicks) != 3:
			bot.say('you must pick 3 things separated by commas')
			return

	random.shuffle(nicks)

	if nicks[0].strip() == nicks[1].strip() and nicks[0].strip() == nicks[2].strip():
		s = 'fuck you, marry your mom, kill yourself'
	else:
		s = 'fuck ' + nicks[0].strip() + ', marry ' + nicks[1].strip() + ', kill ' + nicks[2].strip()

	bot.say(s)


