from youtube_dl import YoutubeDL


def delete_symbols(s):
    symbols_for_deleting = [',', '&', '?', '[', ']', '{', '}', '/', '.',
                            '*', ':', ';', "'", '"', "#", "@", '!', "=", '+', '—', '-', '№']
    new_s = ''
    for i in range(len(s)):
        if s[i] not in symbols_for_deleting:
            new_s += s[i]
    return new_s.replace(' ', '_',).replace(' ', '_').replace('__', '_')   # title for bd writing


def get_yt_video_title(url):  # title for yt video
    with YoutubeDL({'quiet': True}) as ydl:
        info_dict = ydl.extract_info(url, download=False)
    title = delete_symbols(info_dict.get('title', None))
    return title


def get_video_title(filename):  # title for local video
    return delete_symbols(filename[:-3])
