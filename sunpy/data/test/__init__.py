"""SunPy test data files"""
from __future__ import absolute_import

import os
import glob

from astropy.utils.data import get_pkg_data_filename
from astropy.utils.data import get_pkg_data_filenames

import sunpy

__all__ = ['rootdir', 'file_list', 'get_test_filepath', 'get_available_test_data']

rootdir = os.path.join(os.path.dirname(sunpy.__file__), "data", "test")


def get_test_filepath(filename, **kwargs):
    """
    Return the full path to a test file in the ``data/test`` directory.

    Parameters
    ----------
    filename : `str`
        The name of the file inside the ``data/test`` directory.

    Return
    ------
    filepath : `str`
        The full path to the file.

    See Also
    --------

    astropy.utils.data.get_pkg_data_filename : Get package data filename

    Notes
    -----

    This is a wrapper around `astropy.utils.data.get_pkg_data_filename` which
    sets the ``package`` kwarg to be 'sunpy.data.test`.

    """
    return get_pkg_data_filename(filename, package="sunpy.data.test", **kwargs)


def get_available_test_data():
    """
    Prints all available test data

    """
    for fn in get_pkg_data_filenames('test', 'sunpy.data', '*'):
        # checking if the file path yields a directory
        if(os.path.isdir(fn)):
            for dir_contents in os.listdir(fn):
                if "__init__" not in dir_contents:
                    # printing contents of the directory
                    print(dir_contents)
        else:
            # extracting the filename from the directory
            if "__init__" not in fn:
                file_name = os.path.split(fn)[-1]
                print(file_name)


file_list = glob.glob(os.path.join(rootdir, '*.[!p]*'))
