# coding: utf-8

import random
from willie.module import commands
from willie.formatting import color


@commands('nini')
def niniit(bot, trigger, found_match=None):

	gn = "Good night everyone! "

	msgs = []
	msgs.append("May you dream of lolis!")
	msgs.append("Let tomorrow be a great day!")
	msgs.append("Good luck!")
	msgs.append("Sleep tight puppers!")
	msgs.append("Please don't die!")
	msgs.append("I'll be back!")
	msgs.append("It's being fun!")

	msg = gn + random.choice(msgs)

	bot.say(color(u"🌙 ", '06', '00') + color(msg, '06', '00') + color(u" 🌙", '06', '00'))	