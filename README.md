# Spotify-DJ-Requests
Simple pyhton script that allows the crowd to send in songs through the use of a public spotify playlist of your choice. My program will then poll that playlist regulary, grab any new songs added and autmatically download them onto your laptop. This way you can fulfill any song request (assuming you are DJing with a laptop) while still keep the dancefloor active!


Requirements:

    - Python 3.9+

    - spotipy (pip install spotipy)
    
    - python-dotenv (pip install python-dotenv)

    - FFmpeg (required by SpotDL)
        macOS: brew install ffmpeg
        Linux: sudo apt-get install ffmpeg
        Windows: download FFmpeg, add bin to PATH.

    - SpotDL (pip install spotdl) 
            For issues: https://github.com/spotDL/spotify-downloader

    - A Spotify Developer app (Client ID + Client Secret)
        Make sure you register your program on https://developer.spotify.com and aquire your own CLIENT_ID and CLIENT_SECRET
        Once you have both just create a .env file in your directory (cp .env) and use this template:
        SPOTIPY_CLIENT_ID=your-client-id-here
        SPOTIPY_CLIENT_SECRET=your-client-secret-here

Troubleshooting:

    - 429 / “rate/request limit”: You’re hitting Spotify’s rate limits. Increase POLL_SECONDS, reduce MAX_WORKERS, and make sure only one instance of the script is running. SpotDL may briefly show “Retry after: N seconds”; that’s normal.

    - SpotDL not found: Ensure your virtualenv is activated or that spotdl is on PATH.

    - FFmpeg missing: Install FFmpeg and restart your shell.

    - Auth errors: Regenerate your Client Secret and update .env. Never commit real secrets.

Security:

    - NEVER commit .env with real credentials. (people could use your IDs and potentially block your API access)

    - If you accidentally pushed secrets: rotate your Client Secret immediately, remove the file from git history (e.g., git filter-repo), force-push, and have collaborators re-clone.

