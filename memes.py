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

@commands('memes')
def memes(bot, trigger, found_match=None):

	with open('/home/willie/neritic.log', 'r') as f:
		log = f.read()

	p = re.compile(ur"^\w+ \d+ \d+:\d+:\d+ (<" + 'lemmy' + ur">\t.*" + 'imgur.com' + ur".*)", re.MULTILINE | re.IGNORECASE)

	try:

		results = re.findall(p, log)

		bot.say(' '.join(random.choice(results).split()))

	except:

		bot.say('no quote found' + dots())
		