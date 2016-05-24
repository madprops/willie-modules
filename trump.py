# coding: utf-8

from willie.module import rule
from willie.formatting import color
import datetime

@rule(r'.*\bgreat\b.*')
def trump(bot, trigger, found_match=None):

	global timer

	try:
		timer
	except NameError:
		timer = datetime.datetime.now()

	if datetime.datetime.now() - timer >= datetime.timedelta(minutes=30):

		msg = '  MAKE AMERICA GREAT AGAIN!  T R U M P   2 0 1 6  '
		msg = u'\x02' + color(msg, '04', '00') + u'\x02'
		bot.say(msg)
		timer = datetime.datetime.now()