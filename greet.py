import re
import random
import sqlite3
import datetime
from willie.module import commands, rule, event

# if it doesn't exist, create a sqlite database
# and create this table CREATE TABLE greets(id integer primary key, user text, message text);

@commands('greet')
def set_greet(bot, trigger, found_match=None):
    if trigger.is_privmsg:
        return
    conn = sqlite3.connect('/home/willie/willie.db')
    c = conn.cursor()
    message = trigger.group(2)
    user = trigger.nick
    if message == '' or not message:
        return
    t = (user,)
    c.execute('DELETE FROM greets WHERE user=? COLLATE NOCASE', t)
    conn.commit()
    if message != 'delete':
        t = (user, message)
        c.execute('INSERT INTO greets VALUES (NULL,?,?)', t)
        conn.commit()
    conn.close()
    #the lucky number thing is because i use it in a channel where it kicks you if you say the same thing 3 times
    bot.say('ok greet set, your lucky number is ' + str(random.randint(1,1000)))

@rule('.*')
@event("JOIN")
def greet(bot, trigger):
    if trigger.is_privmsg or trigger.nick == 'madbot':
        return
    t = (trigger.nick,)
    conn = sqlite3.connect('/home/willie/willie.db')
    c = conn.cursor()
    c.execute('SELECT * FROM greets WHERE user=? COLLATE NOCASE LIMIT 1', t)
    data = c.fetchone()
    if data:
        msg = data[2]
        if bot.memory.contains('last_thing_said'):
            if bot.memory['last_thing_said'] == msg:
                return
        bot.say(msg)
        bot.memory['last_thing_said'] = msg
    conn.close()
