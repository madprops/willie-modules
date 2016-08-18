# coding: utf-8

from willie.module import commands
from willie.formatting import color

@commands('great')
def trump(bot, trigger, found_match=None):
	arg = trigger.group(2)
	if arg:
		thing = arg.upper()
	else:
		thing = 'AMERICA'
	msg = '  MAKE ' + thing + ' GREAT AGAIN!  T R U M P   2 0 1 6  '
	msg = u'\x02' + color(msg, '04', '00') + u'\x02'
	bot.say(msg)