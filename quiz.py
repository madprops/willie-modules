import json
import random
import urllib
import htmlentitydefs, re
from willie.module import interval
# from willie.module import commands


def escape(html):
	s = html.replace('&amp;','&').replace('&lt;','<').replace('&gt;','>').replace('&quot;','"').replace('&#39;',"'").replace('&#039;',"'")
	d = re.sub('&([^;]+);', lambda m: unichr(htmlentitydefs.name2codepoint[m.group(1)]), s)
	d.encode('utf-8')
	return d
	
@commands('quiz')
# @interval(86400)
def quiz(bot, trigger=None, found_match=None):

	global last_answer

	try:
		last_answer
	except NameError:
		last_answer = ''

	arg = trigger[6:].strip().lower()

	if arg != '':

		if arg == last_answer:
			bot.say('that is correct, it is ' + arg)
		else:
			bot.say(arg + ' is a wrong answer')

		return

	url = "http://www.opentdb.com/api.php?amount=1&category=15&type=multiple"
	response = urllib.urlopen(url)
	content = response.read()
	json_data = json.loads(content.decode('utf8'))
	result = json_data['results'][0]
	msg = 'Question: ' + escape(result['question'])
	answers = [result['correct_answer']]
	answers += result['incorrect_answers']
	indexes = range(0, 4)
	random.shuffle(indexes)

	a = answers[indexes[0]]
	if a == result['correct_answer']:
		last_answer = 'a'
	msg += ' a) ' + escape(a)

	a = answers[indexes[1]]
	if a == result['correct_answer']:
		last_answer = 'b'
	msg += ' b) ' + escape(a)

	a = answers[indexes[2]]
	if a == result['correct_answer']:
		last_answer = 'c'
	msg += ' c) ' + escape(a)

	a = answers[indexes[3]]
	if a == result['correct_answer']:
		last_answer = 'd'
	msg += ' d) ' + escape(a)

	bot.say(msg)
