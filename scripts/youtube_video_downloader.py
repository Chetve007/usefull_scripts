from pytubefix import YouTube
from pytubefix.cli import on_progress


yt = YouTube(
    "https://youtu.be/N0wIgeAqLiA?si=fDagVRP5H-VeZELt&t=5005",
    on_progress_callback=on_progress,
    proxies={"http": "121.188.216.74:995"},
).streams.first().download()
