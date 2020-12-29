from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.pipeline import Pipeline

CHANNAL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNAL_ID
    }

    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
