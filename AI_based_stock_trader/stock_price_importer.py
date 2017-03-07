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


class stock_price_data_collection_function():

    def __init__():

    def download_daily_data(stock_list):
        for stock in stock_list:
            locals()['%s' % stock] = yahoo_finance.Share('%s' % stock)
            locals()['%s_df' % stock] = pd.DataFrame(locals()['%s' %
                                                              stock].get_historical("1989-01-01", "2017-03-01"))
            locals()['%s_df' % stock] = locals()['%s_df' % stock].iloc[::-1]
            locals()['%s_df' % stock].to_csv(
                "%s_stock_data.csv" % stock, index=False)
if __name__ == '__main__':
    stock_list = ['IBM', 'AAPL', 'GOOG', 'MSFT']

    # print IBM.get_open()

    #IBM_df.to_csv("ibm_stock_data.csv", index=False)
