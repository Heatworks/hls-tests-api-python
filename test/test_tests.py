# coding: utf-8

"""
    HLS - Tests

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2017-03-02T13:53:08Z
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import hls_tests
from hls_tests.rest import ApiException
from hls_tests.models.tests import Tests


class TestTests(unittest.TestCase):
    """ Tests unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTests(self):
        """
        Test Tests
        """
        model = hls_tests.models.tests.Tests()


if __name__ == '__main__':
    unittest.main()