#coding=UTF8
#-------------------------
__title__="importer"
__author__="sn0wfree"
__version__=0.1

"""
This function is a component which is part of Data Mining Plan
"""
#-------------------------
import pandas as pd
import os,magic




if __name__ == '__main__':
    #target_file=raw_input("please enter the full path of data file:")
    #os.path.splitext('a/b/c.txt')
    target_file="/Users/sn0wfree/Dropbox/PhD_1st/sn0wfree.github.io/BST215_Quantitative_Research_Methods_Term_1/QRM_assignment/all.csv"

    #recognise the file
    #step 1 recognise headfile
class file_type():
    def __init__(self):
        self.__filetype__='unknown'


    with open(target_file,'rb') as f:
        print file_type_from_magic=magic.from_file(target_file)
#def filetype_headfile():




    #
