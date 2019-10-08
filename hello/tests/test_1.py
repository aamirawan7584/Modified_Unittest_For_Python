#!/bin/env python

import unittest

__author__ = 'omer.nawaz'


class TestSuite(unittest.TestCase):

    def test_a1(self):
        print('Executing Test1')


    def test_a2(self):
        print('Executing Test2')


    def test_a3(self):
        print('Executing Test3')
        assert False

    def test_a4(self):
        print('Executing Test4')
        assert False


class Alpha(unittest.TestCase):

    def test_alpha1(self):
        print('Executing Test1')


    def test_alpha2(self):
        print('Executing Test2')


    def test_alpha3(self):
        print('Executing Test3')
        assert False

    def test_alpha4(self):
        print('Executing Test4')
        assert False
