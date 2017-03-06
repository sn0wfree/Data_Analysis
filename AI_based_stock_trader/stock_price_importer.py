# coding=UTF8
#-------------------------
__title__ = "AI trader: Stock Price importer"
__author__ = "sn0wfree"
__version__ = '0.0.1'

"""
This function is a test for a simply ai trader
"""
#-------------------------
import pandas as pd
import os
import tushare  # for china market
import yahoo_finance  # for global market


if __name__ == '__main__':
    yahoo = yahoo_finance.Share('IBM')
    print yahoo.get_open()
