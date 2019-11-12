'''Module to read different file types and assign them a python data structure'''

import numpy as np
import pandas as pd
from PIL import Image
import pyabf


def read_image(image_file):
    """
    image_file: image file (jpg, png, jpeg)
    return: a pandas dataframe of the RGB representation
    of the image file
    """
    colourImg = Image.open(image_file)
    colourPixels = colourImg.convert("RGB")
    colourArray = np.array(colourPixels.getdata()).reshape(
        colourImg.size + (3,))
    indicesArray = np.moveaxis(np.indices(colourImg.size), 0, 2)
    allArray = np.dstack((indicesArray, colourArray)).reshape((-1, 5))

    return pd.DataFrame(allArray, columns=["y", "x", "red", "green", "blue"])


def read_csv(csv_file):
    """
    csv_file: a csv file
    return: a pandas dataframe containing data
    from the csv file
    """
    return pd.read_csv(csv_file)


def read_xlsx(xslx_file):
    """
    xslx_file: an excel file
    return: a pandas dataframe containing data
    from the xslx file
    """
    return pd.read_excel(xslx_file, sheet_name='data')


def read_abf_binary(binary_file):
    """
    binary_file: .abf binary file
    return: array containing data
    from the abf file 
    """
    file = pyabf.ABF(binary_file)
    return file.data


if __name__ == "__main__":
    # Main functions to Run

    print("Image file \n", read_image("image.jpeg"))
    print("\n csv file \n", read_csv("Nuclei.csv"))
    print("\n xlsx file \n", read_xlsx("Financial Sample.xlsx"))
    print("\n binary file \n", read_abf_binary("16o03002.abf"))
