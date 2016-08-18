import subprocess
from willie.module import commands

@commands('golpe')
def golpe(bot, trigger, found_match=None):

	url = "https://www.reddit.com/r/brasil/comments/4e36ye/"

	command = "golpe"
	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	stdout, stderr = process.communicate()
	percentage = stdout.split()[-1]
	bot.say('Probabilidade de golpe: ' + percentage)
O