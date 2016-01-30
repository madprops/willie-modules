import giantbomb
from willie.module import commands

@commands('vidya')
def vidya(bot, trigger, found_match=None):

	arg = trigger[7:]

	bot.say('searching for ' + arg)

	try:

		gb = giantbomb.Api('c3cd72f9e232132125e9458294f296f73f720c91')

		results = gb.search(arg)

		game = gb.getGame(results[0])

		s = u'\x02' + game.name + u'\x02' + " ("

		for g in game.genres:
		    s += g['name'] + ", "

		s = s[:-2]

		s += ") " + u'\x02' + "Released On: " + u'\x02' + game.original_release_date[:-9]

		s += u'\x02' + " Developed by: " + u'\x02'

		for d in game.developers:
		    s += d['name'] + ", "

		s = s[:-2]


		s += u'\x02' + " Published by: " + u'\x02'

		for p in game.publishers:
		    s += p['name'] + ", "

		s = s[:-2]

		print game.image

		s + " " + game.image.super

		bot.say(s)

	except:
		bot.say('game not foundn')
