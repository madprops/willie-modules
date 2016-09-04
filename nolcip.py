import re
import random
from willie.module import commands

@commands('nolcip')
def nolcip(bot, trigger, found_match=None):

	argument = trigger[8:].strip()

	if argument == '':

		afile = open('/home/willie/nolcipquotes.txt')
		line = next(afile)
		for num, aline in enumerate(afile):
			if random.randrange(num + 2): continue
			line = aline
		bot.say(line)

	else:

		try:

			with open('/home/willie/nolcipquotes.txt', 'r') as f:
				coms = f.read()

			p = re.compile(ur"(.*\b" + argument + ur"\b.*)", re.MULTILINE | re.IGNORECASE)

			results = re.findall(p, coms)

			bot.say(random.choice(results))

		except:

			bot.say("no quote found")

