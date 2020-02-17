from youtube_dl import YoutubeDL

list_url = ["https://www.youtube.com/watch?v=5RAYRa7e9ks", \
            "https://www.youtube.com/watch?v=umMUSzMR-HQ"
            ]

def meta(list_url):

    ydl_opts = {
            #"writeinfojson": False,
            #"skip_download": True,
            "writesubtitles": False,
            "writeautomaticsub": False,
            #"listsubtitles": True
            }
    
    for url in (list_url):
        
        if len(list_url) >= 1:
            
            ydl = YoutubeDL(ydl_opts)
            #ydl.download(list_url)
            #list_sub = ydl.list_subtitles("zepiHyho0WM", "all")
            #print(list_sub)
            meta = ydl.extract_info(url)
            print(meta)
            print("title: ", meta.get("title"))
            print("subtitles: ", meta.get("subtitles"))
        else:
            print("Enter list of urls to download")
            exit(0)

if __name__ == '__main__':
    
    meta(list_url)
