import argparse

def parsers() -> tuple:
    """
    Parsing the arguments of command line
    :return: tuple of name od directory, request, name of annotation file
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_img', type=str, help='Path to the input image')
    parser.add_argument('path_to_save', type=str, help='Path to save the reflected image')
    parser.add_argument('reflection_axis', type=str, help='Axis for reflection: 0 for horizontal, 1 for vertical')
    args = parser.parse_args()
    path_to_img, path_to_save, reflection_axis = args.path_to_img, args.path_to_save, args.reflection_axis
    return path_to_img, path_to_save, reflection_axis