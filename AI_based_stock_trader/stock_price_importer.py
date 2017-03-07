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
            self.stock_price_dict['%s' % stock] = locals()['%s_df' % stock]
            if output_tocsv == True:
                locals()['%s_df' % stock].to_csv(
                    "%s_stock_data.csv" % stock, index=False)
                print '%s download completed' % stock
            else:
                pass
            # else

    def ShowDailyData(self, Startdate="1989-01-01", Enddate="2017-03-01"):
        pass


def ReadStockList(path_stock_list):
    with open(path_stock_list, 'r') as f:
        stocks = f.readlines()
        temp = []
        stock_list = (stock.split(',') for stock in stocks)
        for s in stock_list:

            if isinstance(s, list):
                for rank in xrange(len(s)):
                    if '\n' in s[rank]:
                        s[rank] = s[rank].split('\n')[0]

                temp.extend(s)
            elif isinstance(s, str):
                if '\n' in s:
                    s = s.split('\n')[0]
                temp.append(s)

    return temp


if __name__ == '__main__':
    #stock_list = ['IBM', 'AAPL', 'GOOG', 'MSFT']
    stock_list = ReadStockList('stocklist.txt')
    SPDCollectionFunction(stock_list).DownloadDailyData()

    # print IBM.get_open()

    #IBM_df.to_csv("ibm_stock_data.csv", index=False)
