# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 21:55:24 2018

@author: NISARG
"""

import utils
import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

#from collection import deafultdict
from io import StringIO
import matplotlib.pyplot as plt
from PIL import Image 
import cv2
import collections

#cap=cv2.VideoCapture(0)

sys.path.append(". .")

from utils import visualization_utils as vis_util
from utils import label_map_util
