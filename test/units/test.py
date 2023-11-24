# coding: utf8
""" 
@File: test.py
@Editor: PyCharm
@Author: Austin (From Chengdu.China) https://fairy.host
@HomePage: https://github.com/AustinFairyland
@OperatingSystem: Windows 11 Professional Workstation 23H2 Canary Channel
@CreatedTime: 2023-10-11
"""
from __future__ import annotations

import sys
import warnings
import platform
import asyncio

sys.dont_write_bytecode = True
warnings.filterwarnings("ignore")
if platform.system() == "Windows":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import time

from tools.publics import PublicToolsBaseClass
from conf import ConfigClass
from modules.journals import JournalModulesClass

Journal = JournalModulesClass()
Config = ConfigClass()


class TestClass(PublicToolsBaseClass):
    def __init__(self):
        super().__init__()

    def test_task_01(self):
        Journal.info("test_task_01 开始测试")
        Journal.debug("开始输出配置信息")
        Journal.debug(Config.config)

        Journal.success("test_task_01 测试完成")


if __name__ == "__main__":
    start_run_time = time.time()

    ts = TestClass()
    ts.test_task_01()

    Journal.success("Run Times: {}s".format(time.time() - start_run_time))
