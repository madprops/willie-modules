from willie.module import commands, rule, event

@commands('london')
def london(bot, trigger, found_match=None):

    thing = trigger[8:].upper()

    if thing == 'lemmy':
        thing = 'memes'

    elif thing == 'memes':
        thing = 'lemmy'

    if len(thing) > 11: 
        return

    s = ''

    for c in thing:
        s += c + ' ' 
    s = s.strip()

    if bot.memory.contains('last_london_said'):
        if bot.memory['last_london_said'] == s:
            return

    bot.memory['last_london_said'] = s

    bot.say(s)

    said = []

    for x in range(0, len(thing) - 1):
        if x == 0:
            continue
        s = thing[x]
        for z in range(0, ((len(thing) - 2) * 2) + 1):
            s += ' '
        s += thing[-1 - x]
        said.append(s)
        if len(said) > 2:
            if said[-1] == said[-2] and said[-1] == said[-3]:
                continue
        bot.say(s)

    rthing = thing[::-1]

    s = ''

    for c in rthing:
        s += c + ' '

    s = s.strip()

    bot.say(s)