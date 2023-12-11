import pathlib
import abc

import dataclasses


def fits_in_dir(path: pathlib.Path):
    if not path.exists():
        raise FileNotFoundError(path)
    return [file.resolve() for file in path.glob('*.fit')]

@dataclasses.dataclass
class MultiFile(abc.ABC):
    basedir: pathlib.Path

class ChannelSeparated(MultiFile):
    @property
    def luminosity(self):
        return fits_in_dir(self.basedir / 'L')

    @property
    def red(self):
        return fits_in_dir(self.basedir / 'R')

    @property
    def green(self):
        return fits_in_dir(self.basedir / 'G')

    @property
    def blue(self):
        return fits_in_dir(self.basedir / 'B')


class Calibration(MultiFile):
    @property
    def darks(self):
        return fits_in_dir(self.basedir / 'darks')

    @property
    def flats(self):
        return fits_in_dir(self.basedir / 'flats')
