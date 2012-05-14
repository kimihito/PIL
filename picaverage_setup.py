from numpy.distutils.core import setup
from numpy.distutils.misc_util import Configuration

config = Configuration()
config.add_extension("picaverage_cython", sources=["picaverage_cython.c"])
setup(**config.todict())

