from willie.module import commands
from willie.tools import Identifier
import random

@commands('fmk')
def fmk(bot, trigger, found_match=None):

	nicks = trigger[5:].split(',')

	if len(nicks) == 0:
		nicks = bot.privileges[Identifier(trigger.sender)].keys()
	else:
		if len(nicks) != 3:
			bot.say('you must pick 3 persons')
			return

	random.shuffle(nicks)

	s = 'fuck ' + nicks[0].strip() + ', marry ' + nicks[1].strip() + ', kill ' + nicks[2].strip()

	bot.say(s)


