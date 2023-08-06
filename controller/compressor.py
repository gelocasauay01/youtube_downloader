import ffmpeg
import os

class Compressor:
    def __init__(self, input: str, outname: str):
        self.input = ffmpeg.input(input)
        self.outname = outname
        
    def compress(self) -> bool:
        is_success = True
        try:
            ffmpeg.output(self.input, self.outname, **{'b:v': 200000, 'b:a': 192000, 'vcodec': 'mpeg4', 'vtag': 'xvid', 'vf':'scale=720:480'}).run()
            os.remove(self.input)
        except:
            is_success = False
        return is_success