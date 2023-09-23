from ..domain_models import image


def passthrough(raw_images):
    return image_set.ChannelSeparated(raw_images.basedir)