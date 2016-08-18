import time
import random
import subprocess
import linecache
from willie.module import commands

def fill():
	s = ''
	n = random.randint(2, 7)
	for x in range(1, n):
		s += '!'
	return s

@commands('par')
def par(bot, trigger, found_match=None):

	global par_status
	global par_time
	global par_last_word
	global par_said_words
	global par_time_limit
	global par_level

	try:
		par_status
	except NameError:
		par_status = 'stopped'

	try:
		par_time
	except NameError:
		par_time = 0

	try:
		par_last_word
	except NameError:
		par_last_word = 'joker'

	try:
		par_said_words
	except NameError:
		par_said_words = []

	try:
		par_time_limit
	except NameError:
		par_time_limit = 5

	try:
		par_level
	except NameError:
		par_level = 0

	if par_status == 'stopped':

		arg = trigger[5:]

		if arg != '':
			if arg == 'easy':
				par_time_limit = 12
			elif arg == 'normal':
				par_time_limit = 8
			elif arg == 'hard':
				par_time_limit = 4
			else:
				return
		else:
			par_time_limit = 8

		par_said_words = []
		bot.say('you have ' + str(par_time_limit) + ' seconds to write a word that starts with the last letter of the following word.')
		line_number = random.randint(1, 354984)
		w = linecache.getline('/home/willie/words', line_number)
		w = w.replace("'s\n", "").strip()
		bot.say('the first word is: ' + w)
		par_time = time.time()
		par_last_word = w
		par_said_words.append(w)
		par_level = 0
		par_status = 'started'

	else:
		diff = time.time() - par_time
		if diff > (par_time_limit + 1):
			bot.say(str(int(diff)) + ' seconds have passed, the game has ended. you reached level ' + str(par_level))
			par_status = 'stopped'
			return
		else:
			word = trigger[5:].strip().lower()
			if word == '':
				return
			if word in par_said_words:
				bot.say('repeated word. the game is over. you reached level ' + str(par_level))
				par_status = 'stopped'
				return
			if word[0] != par_last_word[-1]:
				bot.say("you messed up. the game is over. you reached level " + str(par_level))
				par_status = 'stopped'
				return
			process = subprocess.Popen(['grep', word, '/usr/share/dict/words'], stdout=subprocess.PIPE)
			stdout, stderr = process.communicate()
			words = stdout.split()
			if word in [x.lower() for x in words]:
				bot.say('go on, you have ' + str(par_time_limit) + ' seconds' + fill())
				par_last_word = word
				par_said_words.append(word)
				par_time = time.time()
				par_level += 1
			else:
				bot.say(word + " is not a word. the game is over. you reached level " + str(par_level))
				par_status = 'stopped'
			




