import re
import random
from willie.module import commands

def dots():
	s = ''
	n = random.randint(2, 5)
	for x in range(1, n):
		s += '.'
	return s

@commands('jew')
def jew(bot, trigger, found_match=None):

	argument = trigger[5:].strip()

	if argument == '':

		afile = open('/home/willie/jews')
		line = next(afile)
		for num, aline in enumerate(afile):
			if random.randrange(num + 2): continue
			line = aline
		bot.say(line)

	else:

		try:

			with open('/home/willie/jews', 'r') as f:
				coms = f.read()

			p = re.compile(ur"(.*\b" + argument + ur"\b.*)", re.MULTILINE | re.IGNORECASE)

			results = re.findall(p, coms)

			bot.say(random.choice(results))

		except:

			bot.say("the jews don't care about " + argument + dots())

