from youtube_dl import YoutubeDL

list_url = ["https://www.youtube.com/watch?v=5RAYRa7e9ks", \
            "https://www.youtube.com/watch?v=umMUSzMR-HQ"
            ]

def meta(list_url):

    for i in (list_url)
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
        #list_sub = ydl.list_subtitles("zepiHyho0WM", "all")
        #print(list_sub)
        meta = ydl.extract_info("https://www.youtube.com/watch?v=5RAYRa7e9ks")
        for i in range(len(meta)):
            #print(meta[i])
            pass

        #print(meta)
        print("title: ", meta.get("title"))
        print("subtitles: ", meta.get("subtitles"))
    else:
        print("Enter list of urls to download")
        exit(0)

if __name__ == '__main__':
    
    
