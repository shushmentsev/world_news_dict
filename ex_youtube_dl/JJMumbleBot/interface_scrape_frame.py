def _get_capture_url(video_url, resolution):
    # Youtube options
    ydl_opts = {}
    # Create youtube-dl object
    ydl = youtube_dl.YoutubeDL(ydl_opts)
    # Set video url, extract video information
    info_dict = ydl.extract_info(video_url, download=False)
    # Get video formats available
    formats_lst = info_dict.get('formats',None)

    for format in formats_lst:
        # Getting the desired resolution
        if format.get('format_note',None) == resolution:
            # Get the video url
            url = format.get('url',None)
            return url
    return None 
