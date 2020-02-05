def create_track_objects(url, dir):
    """
    Create new Track instances.
    If the url points to a playlist, change the dir and create a new track for each item.
    """
    if 'list' not in url:
        return [Track(url, dir)]
    else:
        tracks = []
        ydl_opts = {'ignoreerrors': True, 'quiet': True}
        with YoutubeDL(ydl_opts) as ydl:
            ydl.add_default_info_extractors()
            info = ydl.extract_info(url, download=False)
            if not info:
                raise TrackNotFound(url)
            logger.info("Playlist: %s", info['title'])
            dir = os.path.join(dir, info['title'])
            for entry in info['entries']:
                if entry is not None:
                    tracks.append(Track('https://www.youtube.com/watch?v=' + entry['id'], dir))
        return tracks 
