import pytesseract
import numpy as np
import imutils
import cv2
from skimage.segmentation import clear_border

class plateDetection:
	def __init__(self,max_ratio,min_ratio):
		self.max_ratio=max_ratio
		self.min_ratio=min_ratio
