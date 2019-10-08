#!/bin/env pythonraise Exception('Sample Exception')

import unittest


__author__ = 'omer.nawaz'


class TestSuite2(unittest.TestCase):
    execution_order = 2


    def test_b1(self):
        print('Executing Test1')


    def test_b2(self):
        print('Executing Test2')
        assert False


    def test_b3(self):
        print('Executing Test3')
        raise Exception('Sample Exception')


    def test_b4(self):
        print('Executing Test4')
        assert False


