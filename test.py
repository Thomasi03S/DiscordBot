import youtube_dl

ydl = youtube_dl.YoutubeDL()
info = ydl.extract_info("https://www.youtube.com/watch?v=W8x4m-qpmJ8", download=False)
print("info:",info)
url2 = info['formats'][0]['url']
print("url2:",url2)