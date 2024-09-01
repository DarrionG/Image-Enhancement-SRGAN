import glob, os
from PIL import Image


# Class to create the data set of lower quality images
class Compress:

    def __init__(self, src_path: str, dest_path: str, img_format: str, img_quality: int):
        
        self.src_path = src_path
        self.dest_path = dest_path
        self.img_format = img_format
        self.img_quality = img_quality

    # Compresses all images of defined type in source to destination
    def img_compress(self):

        paths = glob.glob(self.src_path + '*' + self.img_format)
        
        try:

            for path in paths:

                dest = self.dest_path + os.path.basename(path) + self.img_format

                with Image.open(path) as img:

                    if img.mode != "RGB":

                        img = img.convert("RGB")

                    img.save(dest, "JPEG", optimize=True, quality=self.img_quality)

        except OSError as err:

            print(err)
    