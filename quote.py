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

@commands('q')
def quote(bot, trigger, found_match=None):

	arguments = trigger[3:].strip()


	fname = '/home/willie/' + trigger.sender + '.log'


	if arguments[0:7] == 'search ':
		string = arguments[7:]

		with open(fname, 'r') as f:
			log = f.read()

		p = re.compile(ur"^\w+ \d+ \d+:\d+:\d+ (<(?!madbot|flanfly|SuikaIbuki|Wobbuffet|Internets|kindbot|ChanStat)[^>]+>\t(?![.!~,]).*\b" + string + ur"\b.*)", re.MULTILINE | re.IGNORECASE)

		try:

			results = re.findall(p, log)

			bot.say(' '.join(random.choice(results).split()))

		except:

			bot.say('no quote found' + dots() + ' you searched for ' + string)

	elif arguments[0:6] == 'count ':
		string = arguments[6:]

		with open(fname, 'r') as f:
			log = f.read()

		p = re.compile(ur"^\w+ \d+ \d+:\d+:\d+ (<(?!madbot|flanfly|SuikaIbuki|Wobbuffet|Internets|kindbot|ChanStat)[^>]+>\t(?![.!~,]).*\b" + string + ur"\b.*)", re.MULTILINE | re.IGNORECASE)

		try:

			results = re.findall(p, log)

			bot.say("'" + string + "' has been said " + str(len(results)) + " times")

		except:

			bot.say('no quote found' + dots() + ' you searched for ' + string)

	else:
		with open(fname, 'r') as f:
			log = f.read()

		if arguments != '':
			p = re.compile(ur"^\w+ \d+ \d+:\d+:\d+ (<" + arguments + ur">\t[^.!~,].*)", re.MULTILINE | re.IGNORECASE)
		else:
			p = re.compile(ur'^\w+ \d+ \d+:\d+:\d+ (<(?!madbot|flanfly|SuikaIbuki|Wobbuffet|Internets|kindbot|ChanStat)[^>]+>\t[^.!~,].*)', re.MULTILINE)

		try:

			results = re.findall(p, log)

			bot.say(' '.join(random.choice(results).split()))

		except:

			bot.say("no quote found" + dots())
		


