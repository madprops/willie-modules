# coding: utf-8

import random

from willie.module import commands

def fill():
	s = ''
	n = random.randint(2, 7)
	for x in range(1, n):
		s += '.'
	return s

@commands('tunnel')
def tunnel(bot, trigger, found_match=None):

	msg = u'\x02' + '[an alien message appears]' + u'\x02' + ' ' + trigger[8:] + ' (answer with .tunnel)'

	if trigger.sender == '#podricing':
		bot.msg('#neritic-net', msg, 1)
		bot.say('sending message' + fill())

	elif trigger.sender == '#neritic-net':
		bot.msg('#podricing', msg, 1)
		bot.say('sending message' + fill())
