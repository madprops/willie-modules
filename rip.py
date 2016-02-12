# coding: utf-8

from willie.module import rule
from willie.formatting import color

@rule(ur"^rip\s.*$")
def rip(bot, trigger, found_match=None):
	arg = ' '.join(trigger[4:20].split()).strip()
	if arg == '':
		return
	bot.say(color(u"✞" + ' ' + u"✞" + ' ' u"✞" + ' ' u"✞" + ' ' , '04', '00') + color(' ' + arg.upper() + ' ', '00', '04') + color(' ' + u"✞" + ' ' + u"✞" + ' ' u"✞" + ' ' u"✞", '04', '00'))