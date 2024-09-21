import yt_dlp


link = input("Link:\n")


ydl_opts = {
    'format': 'best',  
    'outtmpl': 'downloads/Mp4s%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',  
    'noplaylist': False  
}


with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print("Done Roasting Your Link.")
