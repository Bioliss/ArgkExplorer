#!/usr/bin/env python3
#
# ライブラリ等使用時にライセンス条項を記載する箇所

"""記念日をツイートする

新垣さんにまつわる記念日の節目の年(1年、2年、3年、5年、10年、20年、30年...)にツイートする
"""
#coding: UTF-8
import commands
import datetime
import os
import urllib2

import PostCommon
from dateutil.relativedelta import *


def get_anniversary_dict() -> dict:
    """記念日の日付と内容を取得

    json形式の定義データを読み込みdict型で返す

    Returns:
        dict -- 記念日の日付と内容
    """    

def main():

    #今日の日付
    today = datetime.datetime.today()
    anniversary_list = get_anniversary_dict()
    for anniversary_day, str_detail in anniversary_list.iteritems():
        # 日付の比較
        date = datetime.datetime.strptime(anniversary_day, '%Y-%m-%d')
        rdelta = relativedelta(today, date)
        years = rdelta.years
        months = rdelta.months
        days = 	rdelta.days

        # true = 1～3 or 5の倍数ではない。
        if (years % 5 and years != 1 and years != 2 and years != 3):
            continue
        
        # 同じ日の場合はTrue
        if (months == 0) and (days == 0):
            if PostCommon.post_tweet("【記念日ツイート】\n" + str_detail + "から今日で" + str(years) + "年になります！\n#新垣結衣") == False:
                print("ツイート失敗")

if __name__ == '__main__':
    main()
