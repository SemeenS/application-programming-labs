from parser import create_parser
from downloader_img import download_images
from iterator import Iterator
from create_annotation import create_annotation

def main():
   keyword, number, img_dir, annotation_file = create_parser()
   try:
      download_images(keyword, number, img_dir)
      create_annotation(img_dir, annotation_file)
      iterator = Iterator(annotation_file)
      for i in iterator:
         print(i)
   except Exception as e:
      print(f"Something went wrong: {e} ")

if __name__ == '__main__':
   main()