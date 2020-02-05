def videoDownload(_url, pathToDownload, _format): #the url should be a list of string urls
    
    #the options that we want when downloading a video
    ydlOpts = {
        'format': ('bestvideo[ext='+_format+']+bestaudio[ext=m4a]/'+_format), #the format that it can be
        'logger': myLogger(), #this is used to log errors and such
        'progress_hooks': [myHook], #says when it's done dont know how useful
        'noplaylist': 'true', #makes it so that if the link is in a youtube playlist it wont download the whole playlist
        'outtmpl': (pathToDownload), #output location and name
        'ignoreerrors': 'true', #if error move one
        'restrictfilenames': 'true' #gets rid of spaces in output name
    }
    with youtube_dl.YoutubeDL(ydlOpts) as ydl:
        ydl.download(_url) 
