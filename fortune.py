# coding: utf-8

import random
import linecache
from willie.module import commands

@commands('fortune')
def fortune(bot, trigger, found_match=None):
	if trigger.sender == '#podricing':
		return False
	line_number = random.randint(1, 500)
	fortune = linecache.getline('/home/willie/fortunes.txt', line_number)
	fortune = ' '.join(fortune.split())
	bot.say(fortune)