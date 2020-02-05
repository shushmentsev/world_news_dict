def download_next():
    queue_list = list(YoutubeHelper.queue_instance.queue_storage)
    # print(queue_list)
    youtube_url = None
    if len(queue_list) > 0:
        youtube_url = queue_list[-1]['main_url']
    else:
        return
    if os.path.isfile(utils.get_temporary_img_dir() + f"{queue_list[-1]['img_id']}.jpg"):
        # print("Thumbnail exists...skipping")
        return
    try:
        with youtube_dl.YoutubeDL(YoutubeHelper.ydl_opts) as ydl:
            ydl.extract_info(youtube_url, download=True)
            #if video['duration'] >= YoutubeHelper.max_track_duration or video['duration'] <= 0.1:
            #    debug_print("Video length exceeds limit...skipping.")
            #    YoutubeHelper.queue_instance.pop()
    except youtube_dl.utils.DownloadError:
        return
    return 
