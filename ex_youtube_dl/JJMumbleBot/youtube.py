def get_playlist_info(self):
        del self.ydl_opts['noplaylist']
        self.ydl_opts['extract_flat'] = True

        # in case of a radio playist, restrict the number of songs that are downloaded
        # if we received just the id, it is an id starting with 'RD'
        # if its a url, the id is behind a '&list='
        if song_utils.is_radio(self.target):
            self.ydl_opts['playlistend'] = self.musiq.base.settings.max_playlist_items

        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            self.info_dict = ydl.extract_info(self.target, download=False)

        if self.info_dict['_type'] != 'playlist' or 'entries' not in self.info_dict:
            raise NoPlaylistException('Not a Playlist')

        playlist_info = {}
        playlist_info['id'] = self.info_dict['id']
        playlist_info['urls'] = []
        if 'title' in self.info_dict:
            playlist_info['title'] = self.info_dict['title']
        for entry in self.info_dict['entries']:
            playlist_info['urls'].append('https://www.youtube.com/watch?v=' + entry['id'])
        return playlist_info 
