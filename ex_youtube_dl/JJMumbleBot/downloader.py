def create_source(cls, ctx, search: str, *, loop, volume, download=True):
        loop = loop or asyncio.get_event_loop()

        ytdlopts['outtmpl'] = f'downloads/{ctx.guild.id}/%(extractor)s-%(id)s-%(title)s.%(ext)s'
        ytdl = youtube_dl.YoutubeDL(ytdlopts)

        to_run = partial(ytdl.extract_info, url=search, download=download)
        data = await utils.evieecutor(func=to_run, executor=None, loop=loop)

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        data['duration'] = data.get('duration', get_duration(data['url']))
        data['channel'] = ctx.channel
        data['volume'] = volume

        if download:
            source = ytdl.prepare_filename(data)
        else:
            source = data['url']

        return cls(discord.FFmpegPCMAudio(source), data=data, requester=ctx.author, filename=source) 
