
# coding: utf-8

from willie.module import commands
from willie.formatting import color

@commands('help')
def help(bot, trigger, found_match=None):
	msg = "Here you can see all the modules I have installed: https://github.com/madprops/willie-modules"
	bot.say(msg)