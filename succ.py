from willie.module import commands
from willie.tools import Identifier
import random

@commands('succ')
def succ(bot, trigger, found_match=None):

	nicks = bot.privileges[Identifier(trigger.sender)].keys()

	bot.say(random.choice(nicks) + ' will never get the succ https://www.youtube.com/watch?v=XJhrw-m7Kzs')

