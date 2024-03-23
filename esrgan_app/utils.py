import os

def get_uploaded_image_path(filename):
    """
    Generates the file path where the uploaded image will be stored.
    """
    return os.path.join('uploads', filename)

def get_result_image_path(filename):
    """
    Generates the file path where the result image will be stored.
    """
    return os.path.join('results', filename)
