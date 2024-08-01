from PIL import Image
import rawpy
import os


# path to folder
output_jpg_path = './toJPG'
directory_path = './190724_1507'


def convert_dng_to_jpg(filename):
            with rawpy.imread(f'{directory_path}/{filename}') as raw:
                rgb = raw.postprocess(
            use_camera_wb=True,
            output_color=rawpy.ColorSpace.sRGB,)
            image = Image.fromarray(rgb)
            newfilename = filename.split('.')[0]
            image.save(f'{output_jpg_path}/{newfilename}.jpg', format='JPEG', quality=100)




for filename in os.listdir(directory_path):
    if filename.endswith(".dng"):
        #print(filename)
        convert_dng_to_jpg(filename) 
