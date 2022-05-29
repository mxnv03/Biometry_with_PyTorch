from youtube_dl import YoutubeDL


def get_video_title(url):
    with YoutubeDL({'quiet': True}) as ydl:
        info_dict = ydl.extract_info(url, download=False)
    title = info_dict.get('title', None).split()[0].replace(',', '')
    return title