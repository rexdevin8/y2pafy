from fastapi import FastAPI
from fastapi.responses import FileResponse
import pafy
import uvicorn
import os
import shutil
import tempfile

app = FastAPI()

@app.get("/audio/")
async def ytsearch(youtube_url: str):
    print(youtube_url)


    tmp = tempfile.mkdtemp()
    print(tmp)
    video = pafy.new(youtube_url)

    print(video.title)
    bestaudio = video.getbestaudio()
    ext = bestaudio.extension
    print(ext)

    bestaudio.download(filepath=tmp)
    download_path = os.path.join(tmp, video.title + "." + ext)
    base, ext = os.path.splitext(download_path)
    new_file = base + '.mp3'
    os.rename(download_path, new_file)


    audio_name = new_file.split("\\")[-1]
    print(download_path)
    print(audio_name)

    return FileResponse(new_file, media_type="audio/mpeg",filename=audio_name)
    shutil.rmtree(tempdir)
