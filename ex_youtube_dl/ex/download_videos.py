from youtube_dl import YoutubeDL

list_url = ["https://www.youtube.com/watch?v=5RAYRa7e9ks", \
            #"https://www.youtube.com/watch?v=5RAYRa7e9ks"
            ]
if __name__ == '__main__':
    
    if len(list_url) >= 1:
        ydl_opts = {
            #"writeinfojson": False,
            #"skip_download": True,
            #"writesubtitles": False,
            #"writeautomaticsub": False,
            #"listsubtitles": True
            }
        ydl = YoutubeDL(ydl_opts)
        #ydl.download(list_url)
        list_sub = ydl.list_subtitles("zepiHyho0WM", "--all-subs")
        #print(list_sub)
        meta = ydl.extract_info("https://www.youtube.com/watch?v=5RAYRa7e9ks")
        for i in range(len(meta)):
            #print(meta[i])
            pass

        print("title: ", meta.get("title"))
    else:
        print("Enter list of urls to download")
        exit(0)
