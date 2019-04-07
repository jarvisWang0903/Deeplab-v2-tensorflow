import os
import numpy as np
from PIL import Image
import tensorflow as tf
def save_image(image, save_dir, name, mean=None):
    """
    Save image by unprocessing if mean given else just save
    :param mean:
    :param image:
    :param save_dir:
    :param name:
    :return:
    """
    if mean.any() != None:
        image = unprocess_image(image, mean)
    new_image = Image.fromarray(np.array(image,dtype = np.uint8))
    new_image.save(os.path.join(save_dir, name + ".png"))
    new_image.show()

def unprocess_image(image, mean_pixel):
    return image + mean_pixel