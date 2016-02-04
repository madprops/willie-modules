# coding: utf-8

import re
import random
import linecache
from willie.module import commands

def dots():
	s = ''
	n = random.randint(2, 5)
	for x in range(1, n):
		s += '.'
	return s

@commands('q')
def quote(bot, trigger, found_match=None):

	global last_date

	try:
		last_date
	except NameError:
		last_date = ''

	arguments = trigger[3:].strip()


	fname = '/home/willie/' + trigger.sender + '.log'


	if arguments[0:7] == 'search ':
		string = arguments[7:]

		with open(fname, 'r') as f:
			log = f.read()

		p = re.compile(ur"^(\w+ \d+ \d+:\d+:\d+ <(?!madbot|flanfly|SuikaIbuki|Wobbuffet|Internets|kindbot|ChanStat)[^>]+>\t(?![.!~,]).*\b" + string + ur"\b.*)", re.MULTILINE | re.IGNORECASE)

		try:

			results = re.findall(p, log)

			result = random.choice(results)

			last_date = result[0:15]

			bot.say(' '.join(result.split())[16:])

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

	elif arguments[0:7] == 'context':

		if last_date != '':

			with open(fname, 'r') as f:
				log = f.read()

			lines = log.split('\n')

			for i, line in enumerate(lines, 0):
				if last_date in line:
					n = i
					break

			for x in range(0, 5):
				d = -2 + x
				try:
					s = lines[n + d]
					s = ' '.join(s.split()).strip()[16:]
					if s.startswith('<'):
						bot.say(s)
				except:
					pass

			last_date = ''

	else:
		with open(fname, 'r') as f:
			log = f.read()

		if arguments != '':
			p = re.compile(ur"^(\w+ \d+ \d+:\d+:\d+ <" + arguments + ur">\t[^.!~,].*)", re.MULTILINE | re.IGNORECASE)
		else:
			p = re.compile(ur'^(\w+ \d+ \d+:\d+:\d+ <(?!madbot|flanfly|SuikaIbuki|Wobbuffet|Internets|kindbot|ChanStat)[^>]+>\t[^.!~,].*)', re.MULTILINE)

		try:

			results = re.findall(p, log)

			result = random.choice(results)

			last_date = result[0:15]

			bot.say(' '.join(result.split())[16:])

		except:

			bot.say("no quote found" + dots())
		


