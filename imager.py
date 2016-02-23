import time
from willie.module import rule
from apiclient.discovery import build

@rule('^((?!http|https|www)\w+(\.png|\.jpg|\.gif))$')
def imager(bot, trigger, found_match=None):

    args = trigger.split('.')
    term = args[0].lower()
    ext = args[-1].lower()


    tries = 0

    while tries < 3:

        try:

            service = build("customsearch", "v1",
                           developerKey=bot.config.google.api_key)
            res = service.cse().list(
                cx=bot.config.google.cx_images,
                q=term,
                searchType='image',
                num=1,
                fileType=ext,
                safe= 'off'
            ).execute()

            if 'items' in res:
                link = res['items'][0]['link']
                bot.say(link)
                break

        except:

            time.sleep(2)
            tries += 1
            pass