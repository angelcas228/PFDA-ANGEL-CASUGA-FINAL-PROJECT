import glob
import os
import sys


from PIL import Image

def main():
    src_img_paths = glob.glob(sys.argv[1])
    logo_img = Image.open('NL_logo.png')
    for src_img_path in src_img_paths:
      name, ext = os.path.splitext(src_img_path)
      with (Image.open(src_img_path) as img,
            ):
          print(f"Watermarking {src_img_path}...")
          padding = 50
          x = padding
          y = img.height - logo_img.height - padding
          img.paste(logo_img, (x, y), mask=logo_img.getchannel('A'))
          # img.paste(logo_img, (x, y))
          img.save(f"{name}_wm{ext}")
    logo_img.close()

if __name__ == "__main__":
    main()