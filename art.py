from PIL import Image
import numpy as np
import math
import statistics



def rgb_image_to_brightness(img):
    print("Image size: ", img.width , "x", img.height)

    image_array = np.array(img)

    pixel_means = np.mean(image_array, axis=2)
    image_mean = pixel_means.flatten()

    return image_mean



def convert_brightness_to_ascii(img):
    ascii_chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    new_image = [ascii_chars[round((brightness / 255) * 20)] for brightness in img]
    return new_image

def display_ascii_art(ascii_art, width, height):
    scaled_ascii_art = [ascii_art[i:i+width] for i in range(0, len(ascii_art), width)]
    scaled_ascii_art = scaled_ascii_art[::height] 

    for row in scaled_ascii_art:
        print(''.join(row))


def main():
    file = "luffy.jpeg"
    img = Image.open(file)

    img_width = 100
    img_height = 50

    image_brightness = rgb_image_to_brightness(img)
    image_ascii = convert_brightness_to_ascii(image_brightness)
    display_ascii_art(image_ascii, img_width, img_height)


main()
