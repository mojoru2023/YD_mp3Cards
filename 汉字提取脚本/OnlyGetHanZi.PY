#! -*- coding:utf-8 -*-


import datetime
import re
import os
import time

import xlrd
from xlrd import xldate_as_tuple
import datetime
import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None




#app选择好(完成)
# 单个下载脚本测试好（完成）
# 需要读取本地excel文件的程序（完成）
# 整理专门的excel文件（完成（完成））
# 在服务器上进行适配# 整理专门的excel文件（完成（完成））
# 放到服务器上去跑



import xlrd

def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

       # # if 去掉表头
       # if rowNum > 0:


    return dataFile


def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功")

if __name__ == '__main__':
    # lpath = '/root/YD_mp3Cards/日语mp3单词库'
    f_list =[]

    # 剔除所有假名的正则

    lpath =  os.getcwd()
    excelFile = '{0}\\m.xlsx'.format(lpath)
    full_items = read_xlrd(excelFile=excelFile)
    for single_name in full_items:
        f_item =re.sub(r"[あいうえおかきくけこさしすせそたちつてとなにねねのはひふへほまみむめもやゆよらりるれろわをんがぎぐげごっざじずぜぞだちづでどばびぶべぼぱぴぷぺぽ]", "", single_name[0])
        f_list.append(f_item)
    for single_pic in set(f_list):
        try:

            with open('M.txt','a') as file_handle:
                  # .txt可以不自己新建,代码会自动新建

                file_handle.write(single_pic+",")     # 写入
                # file_handle.write('\n')         # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
        except:
            pass