# coding: utf-8

from willie.module import rule
from willie.formatting import color

@rule(r'.*\bgreat\b.*')
def trump(bot, trigger, found_match=None):
	msg = '  MAKE AMERICA GREAT AGAIN!  T R U M P   2 0 1 6  '
	msg = u'\x02' + color(msg, '04', '00') + u'\x02'
	bot.say(msg)