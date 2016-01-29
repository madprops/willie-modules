import random
from textblob import TextBlob
from willie.module import commands

@commands('tao')
def tao(bot, trigger, found_match=None):

	with open('/home/willie/tao', 'r') as f:
		tao = f.read()

	blob = TextBlob(tao)
	bot.say(' '.join(random.choice(blob.raw_sentences).split()))


