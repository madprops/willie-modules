# coding: utf-8

import re
import random
from willie.module import commands

def dots():
	s = ''
	n = random.randint(2, 5)
	for x in range(1, n):
		s += '.'
	return s

def fill():
	s = ''
	n = random.randint(2, 7)
	for x in range(1, n):
		s += '.'
	return s

@commands('memes')
def memes(bot, trigger, found_match=None):

	with open('/home/willie/#neritic-net.log', 'r') as f:
		log = f.read()

	p = re.compile(ur"^\w+ \d+ \d+:\d+:\d+ (<" + 'lemmy' + ur">\t.*" + 'imgur.com' + ur".*)", re.MULTILINE | re.IGNORECASE)	

	try:

		results = re.findall(p, log)

		msg = ' '.join(random.choice(results).split())

		if trigger.group(2):

			if trigger.group(2).strip() == '| tunnel':

				msg2 = u'\x02' + '[an alien message appears]' + u'\x02' + ' ' + msg

				if trigger.sender == '#podricing':
					bot.msg('#neritic-net', msg2, 1)
					bot.say('sending message (' + msg + ')')
					return

				elif trigger.sender == '#neritic-net':
					bot.msg('#podricing', msg2, 1)
					bot.say('sending message (' + msg + ')')
					return

		bot.say(msg)

	except:

		bot.say('no quote found' + dots())
		