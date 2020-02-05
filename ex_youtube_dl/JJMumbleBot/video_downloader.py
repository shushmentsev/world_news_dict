def download_video(url, output='video', quiet=True):
    """
    Download a video from youtube with a given url and destination filepath.
    
    url and output must be utf-8 encoded.
    
    If quiet is true, stdout will be suppressed.
    """
    
    ydl_opts = {}
    ydl_opts['outtmpl'] = output
    ydl_opts['quiet'] = quiet
    ydl_opts['merge_output_format'] = 'mkv'
    ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio'
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        result = ydl.extract_info(url, download=False)
        outfile = ydl.prepare_filename(result) + '.' + result['ext']
    
    return outfile 
