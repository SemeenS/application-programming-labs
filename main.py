import argparse
import cv2 as cv

from histogram import compute_histogram, reflection, display_histogram
from parser import parsers

def main() -> None:
    path_to_img, path_to_save, reflection_axis = parsers()

    try:
        img = cv.imread(path_to_img)
        print(f"{path_to_img} sizes: {img.shape}")
        display_histogram(compute_histogram(img))

        ref_img = reflection(img, int(reflection_axis))
        cv.imshow("Original image", img)
        cv.waitKey(0)
        cv.imshow("Reflected image", ref_img)
        cv.waitKey(0)

        cv.imwrite(path_to_save, ref_img)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()