# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_paths.ipynb (unless otherwise specified).

__all__ = ['mapbox_access_token', 'main_path', 'data_path', 'reference_images_path', 'fragment_reference_images_path',
           'glovo_dataset_path', 'branch']

# Cell

# export
from pathlib import Path
import os
#export
Path.ls = lambda x: list(x.iterdir())
#export
mapbox_access_token = 'pk.eyJ1IjoiZGltYWRnbyIsImEiOiJjanYydDF2dTkwdnFzNDNwOXFuNzY4OGxnIn0.wnBvykpkR0RtWOp7bj74Yw'

# export
main_path                       = Path(os.getenv("HOME"))
data_path                       = Path(main_path/'data/food')
reference_images_path           = Path(data_path/'reference_images')
fragment_reference_images_path  = Path(data_path/'fragment_reference_images')


glovo_dataset_path  = Path('/home/dima/datasets/glovo_dataset')

branch = 'dev'