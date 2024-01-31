#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@File:        __init__.py
@Author:      lgx
@Contact:     1101588023@qq.com
@Time:        2024/01/30 13:26
@Description:
"""

from waapix.client import SoundEngineClient, WwiseCoreClient, UIClient


class WaapiClientX(SoundEngineClient, WwiseCoreClient, UIClient):

    def __init__(self, url=None, allow_exception=False):
        super().__init__(url, allow_exception)


if __name__ == '__main__':
    with WaapiClientX() as client:
        print(client.get_info())