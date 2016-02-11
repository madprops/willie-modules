# coding: utf-8

import giantbomb
from willie.module import commands

@commands('vidya')
def vidya(bot, trigger, found_match=None):

	global result_list

	try:
		result_list
	except NameError:
		result_list = []

	gb = giantbomb.Api('c3cd72f9e232132125e9458294f296f73f720c91')

	def get_game(id):

		try:

			game = gb.getGame(id)

			s = u'\x02' + game.name + u'\x02' + " ("

			for g in game.genres:
			    s += g['name'] + ", "

			s = s[:-2] + ")" 
			
			try:
				game.original_release_date[:-9]
				s += u'\x02' + " Released On: " + u'\x02' + game.original_release_date[:-9]
			except:
				pass

			s += u'\x02' + " Developed by: " + u'\x02'

			for d in game.developers:
			    s += d['name'] + ", "

			s = s[:-2]


			s += u'\x02' + " Published by: " + u'\x02'

			for p in game.publishers:
			    s += p['name'] + ", "

			s = s[:-2]

			print game.image

			s += u'\x02' + " URL: " + u'\x02' + game.site_detail_url

			bot.say(s)

		except:
			bot.say('game not found')

	arg = trigger[7:]

	if arg.isdigit():
		if len(result_list) == 0:
			return
		if int(arg) < 1 or int(arg) > len(result_list):
			return
		get_game(result_list[int(arg) - 1])

	else:

		bot.say('searching for ' + arg)

		try:
			results = gb.search(arg)[:8]
			if len(results) == 0:
				bot.say('game not found')
			elif len(results) == 1:
				get_game(results[0])
			else:
				result_list = []
				n = 1
				s = ''
				for g in results:
					result_list.append(g.id)
					s += u'\x02' + '(' + str(n) + ')' + u'\x02' + ' ' + g.name + ' '
					n += 1
				s = s[:-1]
				bot.say("pick a game with '.vidya number' " + s)
		except:
			bot.say('game not found')
