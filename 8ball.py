# coding: utf-8

import random
import string
from willie.module import commands
from willie.formatting import color

def to_int(question):

	characters = string.ascii_letters
	numbers = '0123456789'

	sum = 0
	for c in question:
		n = 0
		try:
			n = characters.index(c) + 1
		except:
			try:
				n = numbers.index(c)
			except:
				pass
		sum += n

	return sum

@commands('8ball')
def speakthetruth(bot, trigger, found_match=None):

	question = trigger.group(2)

	if not question:
		sum = random.randint(0, 100)

	else:
		sum = to_int(question)

	if sum % 2 == 0:

		s = []
		s.append("it's pretty obvious the answer is no")
		s.append("negative")
		s.append("NO")
		s.append("obviously not")
		s.append("shake my head to be honest fam")
		s.append("my sources say no")
		msg = color(random.choice(s), '04')

	else:

		s = []
		s.append("that's certainly so")
		s.append("i have no doubt in my mind")
		s.append("YES")
		s.append("of course")
		s.append("it is certain")
		s.append("one would be wise to think so")
		msg = color(random.choice(s), '03')

	bot.action('shakes the magic 8 ball... ' + msg)