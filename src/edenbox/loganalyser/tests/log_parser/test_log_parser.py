#!/usr/bin/env python3.7

import unittest
from log_analyser.log_parser import LogParser
from tests.log_parser.tests_config import Config


class TestLogParserSetup(unittest.TestCase):

    def setUp(self):
        self.parser = LogParser(Config.DUMMY_FILE)

    def test_1(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
