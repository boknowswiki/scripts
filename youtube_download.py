from pytube import YouTube
from pytube import Playlist
import os, sys

url = 'https://www.youtube.com/watch?v=L0MK7qz13bU'

def downloadYouTube(videourl, path):
    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)



'''
downloadYouTube(url, '/home/botao/share/youtube_videos/yangyi_lee/')

'''
pl = Playlist(url)
pl.populate_video_urls()
l = pl.video_urls
print 'len %d' % len(l)
#pl.download_all('/home/botao/share/youtube_videos/yangyi_lee')
i = 0

while i < len(l):
    print "downloading %d/154, u %s" % (i, l[i])
    try:
        downloadYouTube(l[i], '/home/botao/share/youtube_videos/yangyi_lee/')
    except:
        print 'failed at %d, retry' % i
        #sys.exit(1)
        continue

    i = i + 1


'''
from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=I7qNBJBe-DQ")
yt = yt.get('mp4', '720p')
yt.download('/home/botao/youtube/')
'''
