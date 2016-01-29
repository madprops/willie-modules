import re
import random
import sqlite3
import datetime
from willie.module import commands, rule, event

# if it doesn't exist, create a sqlite database 
# and create this table CREATE TABLE laters(id integer primary key, sender text, receiver text, message text, date text);

@commands('later')
def create_later(bot, trigger, found_match=None):
    if trigger.is_privmsg:
        return
    try:
        conn = sqlite3.connect('/home/willie/willie.db')
        c = conn.cursor()
        cmd = trigger.group(2)
        regex = re.compile(r"^tell\s+(?P<receiver>\S+)\s+(?P<message>.*)$")
        match = regex.match(cmd)
        sender = trigger.nick
        receiver = match.group('receiver')
        message = match.group('message')
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        t = (sender, receiver, message, date)
        c.execute('INSERT INTO laters VALUES (NULL,?,?,?,?)', t)
        conn.commit()
        conn.close()
        #the lucky number thing is because i use it in a channel where it kicks you if you say the same thing 3 times
        bot.say('ok i will remind ' + receiver + '. your lucky number is ' + str(random.randint(1,1000)))
    except:
        bot.say('something went wrong, ' + str(random.randint(1,1000)) + ' children have been sacrificed')

@rule('.*')
def check_later(bot, trigger, found_match=None):
    if trigger.is_privmsg or trigger.nick == 'madbot':
        return
    conn = sqlite3.connect('/home/willie/willie.db')
    c = conn.cursor()
    t = (trigger.nick,)
    ids = []
    c.execute('SELECT * FROM laters WHERE receiver=? COLLATE NOCASE', t)
    for later in c:
        ids.append(later[0])
        sender = later[1]
        receiver = later[2]
        message = later[3]
        date = later[4]
        msg = receiver + ', ' + sender + ' sent you this ' + format_date(date) + ': ' + message
        if bot.memory.contains('last_thing_said'):
            if bot.memory['last_thing_said'] == msg:
                continue
        bot.say(msg)
        bot.memory['last_thing_said'] = msg
    for id in ids:
        t = (id,)
        c.execute('DELETE FROM laters WHERE id=?', t)
        conn.commit()
    conn.close()

@rule('.*')
@event("JOIN")
def check_join(bot, trigger):
    check_later(bot, trigger)

def format_date(datetime_string):
    date_time = datetime.datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')
    current_datetime = datetime.datetime.now()
    delta = str(current_datetime - date_time)
    if delta.find(',') > 0:
        days, hours = delta.split(',')
        days = int(days.split()[0].strip())
        hours, minutes = hours.split(':')[0:2]
    else:
        hours, minutes = delta.split(':')[0:2]
        days = 0
    days, hours, minutes = int(days), int(hours), int(minutes)
    datelets =[]
    years, months, xdays = None, None, None
    plural = lambda x: 's' if x!=1 else ''
    if days >= 365:
        years = int(days/365)
        if len(datelets) < 1:
            datelets.append('%d year%s' % (years, plural(years)))
        days = days%365
    if days >= 30 and days < 365:
        months = int(days/30)
        if len(datelets) < 1:
            datelets.append('%d month%s' % (months, plural(months)))        
        days = days%30
    if not years and days > 0 and days < 30:
        xdays =days
        if len(datelets) < 1:
            datelets.append('%d day%s' % (xdays, plural(xdays)))        
    if not (months or years) and hours != 0:
        if len(datelets) < 1:
            datelets.append('%d hour%s' % (hours, plural(hours)))        
    if not (xdays or months or years):
        if len(datelets) < 1:
            datelets.append('%d minute%s' % (minutes, plural(minutes)))        
    return ', '.join(datelets) + ' ago'