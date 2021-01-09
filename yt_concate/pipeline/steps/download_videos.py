from pytube import YouTube

from yt_concate.pipeline.steps.step import Step
from yt_concate.setting import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        for yt in yt_set:
            url = yt.url
            if utils.video_file_exists(yt):
                print(f'found existing video {yt.url} file, skipping')
                continue
            print(f'downloading{yt.url}')
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)
        return data
