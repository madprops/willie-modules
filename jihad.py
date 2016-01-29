from willie.module import commands
from willie.tools import Identifier
import random

@commands('jihad')
def jihad(bot, trigger, found_match=None):

	nicks = bot.privileges[Identifier(trigger.sender)].keys()

	random.shuffle(nicks)

	n = random.randint(1, len(nicks))

	nicks = nicks[0:n]

	s = ''

	for x in range(0, len(nicks)):
		s += nicks[x]
		if len(nicks) > 1:
			if x == len(nicks) - 2:
				s += ' and '
			elif x < len(nicks) - 2:
				s += ', '

	bot.say('a bomb exploded. ' + s + ' died.')

