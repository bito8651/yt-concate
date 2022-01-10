import os
from pprint import pprint

from .step import Step
from yt_concate.settings import CAPTIONS_DIR


class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            captions = {}
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                time_line = False
                time = None
                caption = None
                for line in f:
                    line = line.strip()
                    if '-->' in line:
                        time_line = True
                        time = line
                        continue
                    if time_line:  # 讓python自動檢查是不是True
                        caption = line
                        captions[caption] = time
                        time_line = False  # reset 成 False 才能繼續用 '-->' 取得 time
            data[caption_file] = captions

        pprint(data)
        return data
