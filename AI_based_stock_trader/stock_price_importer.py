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
import datetime
import tushare  # for china market
import yahoo_finance  # for global market


class SPDCollectionFunction():

    def __init__(self, stock_list, Startdate, Enddate):
        self.stock_list = stock_list
        self.stock_price_dict = {}
        self.Startdate = Startdate
        self.Enddate = Enddate

    def DownloadDailyData(self, output_tocsv=False):
        if self.DateFind(self.Startdate) != 'default':
            Startdate = self.DateFind(self.Startdate)
        else:
            Startdate = '2000-01-01'
        if self.DateFind(self.Enddate) != 'deafult':

            Enddate = self.DateFind(self.Enddate)
        else:
            Enddate = datetime.date.today().strftime('%y-%m-%d')
        # print Startdate, Enddate

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

        return self.stock_price_dict

        # else

    def ShowDailyData(self):
        if self.DateFind(self.Startdate) != 'default':
            Startdate = self.DateFind(self.Startdate)
        else:
            Startdate = '2000-01-01'
        if self.DateFind(self.Enddate) != 'deafult':

            Enddate = self.DateFind(self.Enddate)
        else:
            Enddate = datetime.date.today().strftime('%y-%m-%d')
        pass

    def DateFind(self, date):
        if isinstance(date, str):
            if '-' in date:

                date_output = date

            else:
                date_output = 'default'

        elif isinstance(date, int):
            date = str(date)
            if len(date) >= 8 and ' ' not in date:
                date_output = datetime.datetime.strptime(date, '%y-%m-%d')
            else:
                date_output = 'default'
        return date_output


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
    # for stock in stock_list[0]:
    if stock_list != []:
        #stock = stock_list[1]
        print stock
        history_Date_list = SPDCollectionFunction(stock, '2003-01-01',
                                                  '2017-03-06').DownloadDailyData()

    # print IBM.get_open()

    #IBM_df.to_csv("ibm_stock_data.csv", index=False)
