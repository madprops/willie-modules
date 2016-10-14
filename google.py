import time
from willie.module import commands
from apiclient.discovery import build

@commands('g')
def google(bot, trigger, found_match=None):

	term = trigger.group(2)

	tries = 0

	while tries < 3:

		try:

			service = build("customsearch", "v1",
						   developerKey=bot.config.google.api_key)
			res = service.cse().list(
				cx=bot.config.google.cx_all,
				q=term,
				num=1,
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