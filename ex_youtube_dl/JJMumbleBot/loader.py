def _load_from_url(self, url: str, *, noplaylist=False):
        '''Retrieves one or more songs for a url. If its a playlist, returns multiple

        The results are (title, source) pairs
        '''

        ydl = youtube_dl.YoutubeDL({
            'format': 'bestaudio/best',
            'noplaylist': noplaylist,
            'ignoreerrors': True,
            'nocheckcertificate': True,
            'logtostderr': False,
            'quiet': True
        })

        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, self._extract_songs, ydl, url) 
