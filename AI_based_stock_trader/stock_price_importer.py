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


class SPDCollectionFunction():

    def __init__(self, stock_list):
        self.stock_list = stock_list
        self.stock_price_dict = {}

    def DownloadDailyData(self, Startdate="1989-01-01", Enddate="2017-03-01", output_tocsv=False):
        for stock in self.stock_list:

            locals()['%s_df' % stock] = pd.DataFrame(yahoo_finance.Share(
                '%s' % stock).get_historical(Startdate, Enddate))
            locals()['%s_df' % stock] = locals()['%s_df' % stock].iloc[::-1]
            if output_tocsv == True:
                locals()['%s_df' % stock].to_csv(
                    "%s_stock_data.csv" % stock, index=False)
            self.stock_price_dict['%s' % stock] = locals()['%s_df' % stock]


def ReadStockList():


if __name__ == '__main__':
    stock_list = ['IBM', 'AAPL', 'GOOG', 'MSFT']
    SPDCollectionFunction(stock_list).DownloadDailyData()

    # print IBM.get_open()

    #IBM_df.to_csv("ibm_stock_data.csv", index=False)
