from __future__ import unicode_literals

from subprocess import Popen, PIPE
from willie.module import commands, rule, rate, event, unblockable
from willie.tools import Identifier
import time
import sys

current_milli_time = lambda: int(round(time.time() * 1000))

@commands('ping')
def ping(bot, trigger, found_match=None):
    target = trigger.nick
    if trigger.group(2) and trigger.group(3):
        target = trigger.group(3)
    if '#' in target:
        return
    target = Identifier(target)
    bot.msg(target, '\x01PING {0} {1:016d}\x01'.format(trigger.sender, current_milli_time()))


@rate(5)
@rule('(\S*) (\d{16})')
@event('NOTICE')
@unblockable
def read_ping_reply(bot, trigger):
    if 'intent' not in trigger.tags:
        return

    if trigger.tags['intent'].upper() != 'PING':
        return

    target = trigger.group(1)
    try:
        initialtime = int(trigger.group(2))
    except ValueError:
        return # Not our problem

    diff = int(current_milli_time() - initialtime)

    bot.msg(target, '[PING] ' + trigger.nick + ': ' + str(diff) + ' ms')