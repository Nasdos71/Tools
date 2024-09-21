import yt_dlp

link = input("Link:\n")

ydl_opts = {
    'format': 'bestaudio/best',  # Download the best audio quality
    'postprocessors': [{          # Use the FFmpeg postprocessor to convert to MP3
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',  # Specify the output format
        'preferredquality': '320',  # Set the desired quality (optional)
    }],
    'outtmpl': 'downloads/Mp3s/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s',  
    'noplaylist': False  
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print("Done Roasting Your Link.")
