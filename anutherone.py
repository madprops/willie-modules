# coding: utf-8

from willie.module import commands

@commands('anutherone')
def anutherone(bot, trigger, found_match=None):
	if bot.memory.contains('last_thing_said'):
		bot.say(bot.memory['last_thing_said'])