from willie.module import rule
 
@rule('^(\[.*\])$') 
def intesify(bot, trigger, found_match=None):
    if trigger.is_privmsg:
        return
    thing = trigger.group(1)[1:-1]
    if thing != "":
        msg = u'\x02' + '[' + thing.upper() + ' INTENSIFIES]'
        if bot.memory.contains('last_thing_said'):
            if bot.memory['last_thing_said'] == msg:
                return
        bot.say(msg)
        bot.memory['last_thing_said'] = msg