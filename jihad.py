from willie.module import rule
from willie.tools import Identifier
import random

@rule(ur"^(?!\.).*?\bmemes\b.*$")
def jihad(bot, trigger, found_match=None):

	global charge

	try:
		charge
	except NameError:
		charge = 0

	charge += 10

	if charge >= 100:

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

		charge = 0


