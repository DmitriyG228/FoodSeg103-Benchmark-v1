# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/segment.ipynb (unless otherwise specified).

__all__ = ['url_to_image', 'checkpoints_path', 'model_path', 'get_segment_model', 'inference_segmentor']

# Cell
import sys
sys.path.insert(0,'..')

from mmseg.apis import init_segmentor, inference_segmentor, show_result_pyplot
from mmseg.core.evaluation import get_palette
import numpy as np
from mytools.tools import *
from urllib.request import urlopen
import cv2
from PIL import Image
from .paths import *
from pathlib import Path
import torch

def url_to_image(url):
	# download the image, convert it to a NumPy array, and then read
	# it into OpenCV format
	resp = urlopen(url)
	image = np.asarray(bytearray(resp.read()), dtype="uint8")
	image = cv2.imdecode(image, cv2.IMREAD_COLOR)
	# return the image
	return image

# Cell
checkpoints_path = Path('/home/dima/FoodSeg103-Benchmark-v1/checkpoints/')
model_path = checkpoints_path.ls()[7]

# config_file     = [p for p in model_path.ls() if '.py' in p.name][0]
# checkpoint_file = [p for p in model_path.ls() if 'pth' in p.name][0]

# print(model_path)


# Cell
def get_segment_model(model_path):
    config_file     = [p for p in model_path.ls() if '.py' in p.name][0]
    checkpoint_file = [p for p in model_path.ls() if 'pth' in p.name][0]
    return  init_segmentor(str(config_file), str(checkpoint_file), device='cuda:0')

inference_segmentor =inference_segmentor

