import unittest


class Loader(unittest.TestLoader):

    def __init__(self, *args, **kwargs):
        super(Loader, self).__init__(*args, **kwargs)