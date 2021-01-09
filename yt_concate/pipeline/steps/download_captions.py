import time

from pytube import YouTube

from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for yt in data:
            print('Downloading video captions for', yt.url)
            if utils.caption_file_exists(yt):
                print('Found existing caption file')
                continue
            try:
                source = YouTube(yt.url)
                # print(source.captions)
                en_caption = source.captions['a.en']
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
                # print(en_caption_convert_to_srt)
            except KeyError:
                print('KeyError when downloading video captions for', yt.url)
                continue
            # save the caption to a file named Output.txt
            text_file = open(utils.get_caption_filepath(yt.url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()

        end = time.time()
        print('took', end - start, 's')
        return data
