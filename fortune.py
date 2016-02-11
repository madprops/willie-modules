# coding: utf-8

import random
import linecache
from willie.module import commands

@commands('fortune')
def fortune(bot, trigger, found_match=None):
	line_number = random.randint(1, 500)
	fortune = linecache.getline('/home/willie/fortunes.txt', line_number)
	bot.say(fortune)