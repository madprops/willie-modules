import sys
import string
from willie.module import commands

def string_to_num(txt):
	characters = string.ascii_letters
	numbers = '0123456789'
	txt = txt.lower().strip()
	txt = ' '.join(txt.split())
	word_sums = 0
	for word in txt.split():
		word_sum = 0
		for letter in word:
			try:
				n = characters.index(letter) + 1
			except:
				try:
					n = numbers.index(letter)
				except:
					pass
			word_sum += n
		word_sums += word_sum
	return word_sums

def deconstruct(num, s=""):
	sum = 0
	for n in str(num):
		sum += int(n)
	s += " -> " + str(sum)
	if len(str(sum)) > 1:
		return deconstruct(sum, s)
	else:
		if s 
		return s

@commands('numb')
def stringnum(bot, trigger, found_match=None):
	try:
		txt = trigger[6:]
		num1 = string_to_num(txt)
		deconstruction = deconstruct(num1)
		bot.say(txt + ' = ' + str(num1) + deconstruction)
	except:
		bot.say('format must be alphanumeric')




