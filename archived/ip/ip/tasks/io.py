import pathlib
from ..domain_models import image

def read_uncalibrated(path: pathlib.Path | str):
    if type(path) is str:
        path = pathlib.Path(path)
    set = image_set.UncalibratedImageSet(path)
    return set
