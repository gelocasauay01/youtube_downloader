import ffmpeg
import os

class Compressor:
    def __init__(self, input_path: str, outname: str):
        self.input_path = input_path
        self.input_file = ffmpeg.input(input_path)
        self.outname = outname
        
    def compress(self):
        ffmpeg.output(self.input_file, self.outname, **{'b:v': 200000, 'b:a': 192000, 'vcodec': 'mpeg4', 'vtag': 'xvid', 'vf':'scale=720:480'}).run()
        os.remove(self.input_path)
