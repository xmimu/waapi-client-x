#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File:        test_ui_methods.py
@Author:      lgx
@Contact:     1101588023@qq.com
@Time:        2024/03/14 20:21
@Description:
"""
import time
import unittest
from waapix.client import UIClient
from waapix.constants import command


class TestUiMethods(unittest.TestCase):

    def setUp(self):
        self.client = UIClient()

    def tearDown(self):
        self.client.disconnect()

    def test_get_commands(self):
        result = self.client.ui_get_commands()
        self.assertIsInstance(result, list)
        self.assertTrue(result)
        print('Test get commands:', len(result), result)

    def test_get_selected(self):
        result = self.client.ui_get_selected_objects()
        self.assertIsInstance(result, list)
        print('Test get selected:', len(result), result)

    def test_show_explorer(self):
        self.client.ui_execute_command(command.ShowLogs)
        time.sleep(3)
        self.client.ui_execute_command(command.CloseView)


if __name__ == '__main__':
    unittest.main()
