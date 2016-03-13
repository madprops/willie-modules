# coding: utf-8

from willie.module import commands
from willie.formatting import color


@commands('stop')
def stopit(bot, trigger, found_match=None):

	text = u"Did you know that bullying people on IRC can cause serious problems? The victim may get depressed (which is an illness!) or even become suicidal! This is not a joke and has to be taken seriously! Notice that you have done something wrong, take action and stop this now. It is better for everyone. You would not like it if someone did the same to you, would you? Please be aware of your failure and don’t do this to anyone again."

	bot.say(color(text, '00', '04'))