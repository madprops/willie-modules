# coding: utf-8

import random
from willie.module import commands

@commands('decide')
def decide(bot, trigger, found_match=None):

	args = ' '.join(trigger.strip().split())

	if args == '.decide':
		bot.say('you must include things separated by commas')

	arg_list = args[8:].split(',')

	bot.say(random.choice(arg_list).strip())
