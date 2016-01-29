import random
from willie.module import commands

@commands('nk')
def nk(bot, trigger, found_match=None):
	afile = open('/home/willie/nk')
	line = next(afile)
	for num, aline in enumerate(afile):
		if random.randrange(num + 2): continue
		line = aline
	bot.say(line)

