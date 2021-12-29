from pytube import YouTube #pip insatll pytube

link = "https://youtu.be/zbMHLJ0dY4w"

yt = YouTube(link)
stream = yt.streams.all()
stream = yt.streams.get_by_itag('22')
stream.download()

# https://www.worthwebscraping.com/how-to-download-youtube-videos-using-python/
