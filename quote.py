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

	arguments = ' '.join(trigger[3:].strip().split())

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

		lenargs = arguments[8:].strip().split()

		lbefore = 2
		lafter = 2

		if len(lenargs) > 0:
			if len(lenargs) == 1:
				if lenargs[0].isdigit():
					lbefore = min(int(lenargs[0]), 10)
					lafter = lbefore
			if len(lenargs) == 2:
				if lenargs[0].isdigit():
					lbefore = min(int(lenargs[0]), 10)
				if lenargs[1].isdigit():
					lafter = min(int(lenargs[1]), 10)

		if last_date != '':

			with open(fname, 'r') as f:
				log = f.read()

			lines = log.split('\n')

			for i, line in enumerate(lines, 0):
				if last_date in line:
					n = i
					break

			for x in range(0, (1 + lbefore + lafter)):
				d = -(lbefore) + x
				try:
					s = lines[n + d]
					s = ' '.join(s.split()).strip()[16:]
					if s.startswith('<'):
						bot.say(s)
				except:
					pass

	else:
		with open(fname, 'r') as f:
			log = f.read()

		term = ''
		username = ''

		if arguments != '':

			ls = arguments.split()
			username = ls[0]
			if len(ls) > 1:
				term = ' '.join(ls[1:])

		if username != '':

			if term != '':

				p = re.compile(ur"^(\w+ \d+ \d+:\d+:\d+ <" + username + ur">\t[^.!~,].*\b" + term + ur"\b.*)", re.MULTILINE | re.IGNORECASE)
			else:

				p = re.compile(ur"^(\w+ \d+ \d+:\d+:\d+ <" + username + ur">\t[^.!~,].*)", re.MULTILINE | re.IGNORECASE)

		else:

			p = re.compile(ur'^(\w+ \d+ \d+:\d+:\d+ <(?!madbot|flanfly|SuikaIbuki|Wobbuffet|Internets|kindbot|ChanStat)[^>]+>\t[^.!~,].*)', re.MULTILINE)

		try:

			results = re.findall(p, log)

			result = random.choice(results)

			last_date = result[0:15]

			bot.say(' '.join(result.split())[16:])

		except:

			bot.say("no quote found" + dots())
		


