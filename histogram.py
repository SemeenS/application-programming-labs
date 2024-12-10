import cv2 as cv
import numpy as np

from matplotlib import pyplot as plt

def compute_histogram(image: np.ndarray) -> tuple:
    """
    create the histogram for each color channel (B, G, R) of the input image.
    :return tuple: A tuple containing three histograms (B, G, R) as numpy arrays.
    """
    histograms = [cv.calcHist([image], [i], None, [256], [0, 256]) for i in range(3)]
    return tuple(histograms)

def display_histogram(histograms: tuple) -> None:
    """
    show the histograms of the RGB channels.
    :return: None:
    """
    colors = ['b', 'g', 'r']
    plt.figure(figsize=(10, 5))
    plt.title('Histogram of RGB Channels')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    for hist, color in zip(histograms, colors):
        plt.plot(hist, color=color)
    plt.show()

def reflection(img: np.ndarray, axis: int) -> np.ndarray:
    """
    Reflect the input image along the specified axis.
    :return: np.ndarray: The reflected image.
    """
    return cv.flip(img, axis)