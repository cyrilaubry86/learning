import doctest
# Import some standard libraries
import doctest
import copy

# Import external libraries
import numpy
import cv2
from skimage import io


def remove_red(pixel_data):
  """ Sets all red channels to 0 in a list of pixels.
  >>> remove_red([[[0, 0, 0], [255, 0, 0]], [[0, 255, 0], [0, 0, 255]]])
  [[[0, 0, 0], [0, 0, 0]], [[0, 255, 0], [0, 0, 255]]]
  >>> remove_red([[[0, 0, 0], [100, 0, 0]], [[150, 255, 0], [255, 0, 255]]])
  [[[0, 0, 0], [0, 0, 0]], [[0, 255, 0], [0, 0, 255]]]
  """
  new_pixel_data = copy.deepcopy(pixel_data)
  for rows in pixel_data:
    for row in rows:
      row[0] = 0
  return new_pixel_data

# Run the doctests
doctest.run_docstring_examples(remove_red, globals(), verbose=True, name='remove_red')