def get_youtube_url(self, youtube_url):
        # determine the media file name
        filetmpl = u'%(id)s_%(uploader_id)s_%(title)s.%(ext)s'
        ydl = youtube_dl.YoutubeDL({
            'outtmpl': join(self.media_folder, filetmpl),
            'quiet': True, 'restrictfilenames': True, 'noplaylist': True
        })
        ydl.add_default_info_extractors()
        try:
            result = ydl.extract_info(youtube_url, download=False)
            media_filename = sanitize_filename(filetmpl % result['entries'][0], restricted=True)
        except:
            return ''

        # check if a file with this name already exists
        if not os.path.isfile(media_filename):
            try:
                ydl.extract_info(youtube_url, download=True)
            except:
                return ''
        return u'%s/%s' % (self.media_url, split(media_filename)[1]) 
