import os
import datetime
from willie.module import interval
# from willie.module import commands

def sorted_ls(path):
	mtime = lambda f: os.stat(os.path.join(path, f)).st_mtime
	return list(sorted(os.listdir(path), key=mtime))

# @commands('check')
@interval(3600)
def check_for_new_videos(bot):

	# bot.msg('madprops', 'running the handbeezy thing at ' + str(datetime.datetime.now()))

	files = sorted_ls('/var/www/handbeezy/media/videos')

	last_file = files[-1]

	fnum = last_file.split('.')[0]
	
	f = open('/home/willie/last_video.txt', 'r+')

	fnum_current = f.read()

	if fnum_current == '':
		f.seek(0)
		f.write(fnum)
		f.truncate()
		f.close()
	else:
		if fnum > fnum_current:
			for x in range(int(fnum_current) + 1, int(fnum) + 1):
				bot.msg('#podricing', 'new video! http://handbeezy.com/' + str(x) + '/ (possibly nsfw)')
			f.seek(0)
			f.write(fnum)
			f.truncate()
			f.close()

