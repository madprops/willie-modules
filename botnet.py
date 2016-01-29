# coding: utf-8

from willie.module import commands
from willie.formatting import color

pos = 0

def get_color():

	colors = ['02', '04', '08', '02', '03', '04']
	global pos
	if pos > len(colors) - 1:
		pos = 0
	c = colors[pos]
	pos += 1
	return c


@commands('botnet')
def botnet(bot, trigger, found_match=None):

	text = trigger[8:]

	result = ''

	for c in text:
		if c == ' ':
			result += c
		else:
			result += color(c, get_color())

	bot.say(result)

	global pos
	pos = 0