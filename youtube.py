from pytube import YouTube
#https://www.youtube.com/watch?v=pBKGqdsDfos
yt = YouTube('https://www.youtube.com/watch?v=6D-BW8dSb3w')
yt.set_filename(yt.filename)
print(yt.get_videos())
video = yt.filter(resolution='360p')
video[0].download("H://guest//Videos")
