from youtube_dl import YoutubeDL


def get_yt_video_title(url):
    with YoutubeDL({'quiet': True}) as ydl:
        info_dict = ydl.extract_info(url, download=False)
    title = info_dict.get('title', None).replace(' - ', '_')\
        .replace(' ', '_').replace('.', '').replace('—', '').replace('__', '_').replace('?', '')
    return title


def get_video_title(filename):
    return filename[:-3].replace(' - ', '').replace(' ', '_').replace('.', '').replace('—', '').replace('__', '_')