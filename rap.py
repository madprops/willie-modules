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

@commands('rap')
def rap(bot, trigger, found_match=None):

	global rap_status
	global rap_time
	global rap_last_word
	global rap_said_words
	global rap_time_limit
	global rap_level

	try:
		rap_status
	except NameError:
		rap_status = 'stopped'

	try:
		rap_time
	except NameError:
		rap_time = 0

	try:
		rap_last_word
	except NameError:
		rap_last_word = 'joker'

	try:
		rap_said_words
	except NameError:
		rap_said_words = []

	try:
		rap_time_limit
	except NameError:
		rap_time_limit = 5

	try:
		rap_level
	except NameError:
		rap_level = 0

	if rap_status == 'stopped':

		arg = trigger[5:]

		if arg != '':
			if arg == 'easy':
				rap_time_limit = 12
			elif arg == 'normal':
				rap_time_limit = 8
			elif arg == 'hard':
				rap_time_limit = 4
			else:
				return
		else:
			rap_time_limit = 8

		rap_said_words = []
		bot.say('you have ' + str(rap_time_limit) + ' seconds to write a word that ends with the last letter of the following word.')
		while True:
			line_number = random.randint(1, 354984)
			w = linecache.getline('/home/willie/words', line_number)
			w = w.replace("'s\n", "").strip()
			if w[-1] == 's':
				continue
			break
		bot.say('the first word is: ' + w)
		rap_time = time.time()
		rap_last_word = w
		rap_said_words.append(w)
		rap_level = 0
		rap_status = 'started'

	else:
		diff = time.time() - rap_time
		if diff > (rap_time_limit + 1):
			bot.say(str(int(diff)) + ' seconds have passed, the game has ended. you reached level ' + str(rap_level))
			rap_status = 'stopped'
			return
		else:
			word = trigger[5:].strip().lower()
			if word == '':
				return
			if word in rap_said_words:
				bot.say('repeated word. the game is over. you reached level ' + str(rap_level))
				rap_status = 'stopped'
				return
			if word[-1] != rap_last_word[-1]:
				bot.say("you didn't rhyme. the game is over. you reached level " + str(rap_level))
				rap_status = 'stopped'
				return
			process = subprocess.Popen(['grep', word, '/usr/share/dict/words'], stdout=subprocess.PIPE)
			stdout, stderr = process.communicate()
			words = stdout.split()
			if word in [x.lower() for x in words]:
				bot.say('go on, you have ' + str(rap_time_limit) + ' seconds' + fill())
				rap_last_word = word
				rap_said_words.append(word)
				rap_time = time.time()
				rap_level += 1
			else:
				bot.say(word + " is not a word. the game is over. you reached level " + str(rap_level))
				rap_status = 'stopped'
			




