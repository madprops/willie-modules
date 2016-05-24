import random
from willie.tools import Identifier
from willie.module import commands

@commands('cards')
def cards(bot, trigger, found_match=None):

	global czar
	global status
	global players
	global used_questions
	global answer_lines

	try:
		czar
	except NameError:
		czar = ''

	try:
		status
	except NameError:
		status = 'stopped'

	try:
		players
	except NameError:
		players = []

	try:
		used_questions
	except NameError:
		used_questions = []

	try:
		answer_lines
	except NameError:
		f = open('/home/willie/white')
		answer_lines = f.readlines()

	num_questions = 406
	num_answers = 688

	args = ' ' + trigger[6:].strip()

	def get_nicks():
		return bot.privileges[Identifier(trigger.sender)].keys()

	def random_question():
		global used_questions
		afile = open('/home/willie/black')
		line = next(afile)
		status = 'ended'
		for num, aline in enumerate(afile):
			if random.randrange(num + 2): continue
			if num in used_questions:
				continue
			else:
				used_questions.append(num)
				line = aline
				status = 'ok'
		if status == 'ended':
			return 'ended'
		else:
			return line

	def draw_cards():
		global czar
		global players
		for p in players:
			if p != czar:
				nums = random.sample(range(0, num_answers - 1), 10)
				bot.msg(p, '-------- here are your cards. use ".cards id" to choose your answer --------', 1)
				for n in nums:
					bot.msg(p, str(n) + ' - ' + answer_lines[n], 1)

	def end_game():
		global czar
		global status
		global players
		global used_questions
		bot.say('the game has ended!')
		players = []
		used_questions = []
		czar = ''
		status = 'stopped'

	def next_round():
		global czar
		global players
		czar = random.choice(players)
		bot.say(czar + ' is now the czar. pick a winner with ".cards pick nickname"')
		q = random_question()
		if q == 'ended':
			end_game()
			return
		bot.say(u'\x02' + q + u'\x02')
		draw_cards()

	if args == ' ':
		if status != 'started':
			bot.say('game has not started. use ".cards start" to begin')
		else:
			bot.say('game is ongoing. use ".cards start" to start a new game')
		return

	if args == ' reset deck':
		f = open('/home/willie/white')
		answer_lines = f.readlines()
		bot.say('done!!')
		return

	if args == ' start':
		czar = ''
		players = []
		used_questions = []
		status = 'starting'
		bot.say('starting a new game. add players with ".cards add nickname". remove players with ".cards remove nickname". when you\'re ready type ".cards ready"')
		return

	if args == ' list':
		if len(players) == 0:
			bot.say('nobody is playing')
			return
		s = ''
		for p in players:
			s += p + ' '
		bot.say('this the list of players: ' + s)

	if args == ' next':
		if status != 'started':
			bot.say('game has not started. use ".cards start" to begin')
			return
		else:
			next_round()
			return

	if args == 'end':
		end_game()
		return

	if ' add ' in args:
		if status == 'ended':
			bot.say('game has not started. use ".cards start" to begin')
			return
		p = args.split()[-1].strip()
		if p not in get_nicks():
			bot.say('that person is not in this channel')
			return
		else:
			pp = p.lower()
			if pp not in players:
				players.append(pp)
				bot.say(p + ' was added to the game!')
				return
			else:
				bot.say('player already added')
				return

	if ' remove ' in args:
		if status == 'ended':
			bot.say('game has not started. use ".cards start" to begin')
			return
		p = args.split()[-1].strip()
		if p.lower() in players:
			players.remove(p.lower())
			bot.say(p + ' was removed from the game')
			return
		else:
			bot.say(p + ' is not playing')
			return

	if status == 'starting':

		if args == ' ready':
			# if len(players) < 2:
			# 	bot.say('not enough people to play :(')
			# 		return
			bot.say('starting game!')
			status = 'started'
			next_round()
			return

	if status == 'started':
		if ' pick ' in args:
			p = args.split()[-1]
			if p.lower() not in players:
				bot.say('that person is not playing!')
				return
			else:
				if trigger.nick != czar:
					bot.say('you are not the czar!')
					return
				else:
					bot.say(p + ' won!')
					next_round()
					return

		if args.split()[0].isdigit():
			id = int(args.split()[0])
			if id + 1 > num_answers:
				return
			else:
				bot.say(trigger.nick + ' chose "' + answer_lines[id].strip() + '"')
				return
