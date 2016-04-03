# coding: utf-8

from willie.module import commands

@commands('tunnel')
def tunnel(bot, trigger, found_match=None):

	msg = u'\x02' + '[an alien message appears]' + u'\x02' + ' ' + trigger[8:] + ' (answer with .tunnel msg)'

	if trigger.sender == '#podricing':
		bot.msg('#neritic-net', msg, 1)

	elif trigger.sender == '#neritic-net':
		bot.msg('#podricing', msg, 1)

	bot.say('message sent.')
