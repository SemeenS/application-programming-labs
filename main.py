from parser import create_parser
from downloader_img import download_images
from iterator import Iterator
from create_annotation import create_annotation

def main():
   args = create_parser()
   try:

      #download_images(args.keyword, args.number, args.img_dir)
      create_annotation(args.img_dir, args.annotation_file)
      iterator = Iterator(args.annotation_file)
      for i in iterator:
         print(i)
   except Exception as e:
      print(e)

if __name__ == '__main__':
   main()