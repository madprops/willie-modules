from willie.module import rule, event

@rule('.*')
@event("JOIN")
def kys(bot, trigger):
    bot.say('kill yourself ' + trigger.user)
    