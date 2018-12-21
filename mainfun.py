#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import datetime
import shutil


path = "C:/Users/dongf/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"
path_target = "C:/MyData/Data/图片/LockScreenAutoGetSave"


def get_pics():
    index = 1
    path_day = ''
    path_month = ''
    date_now = datetime.datetime.now()
    if date_now.month < 10:
        path_month = '0' + str(date_now.month)
    else:
        path_month = str(date_now.month)
    if date_now.day < 10:
        path_day = '0' + str(date_now.day)
    else:
        path_day = str(date_now.day)
    new_name_pre = 'img' + str(date_now.year) + path_month + path_day
    for item in os.listdir(path=path):
        print(item)
        old_name = os.path.join(path, item)
        item_size = os.path.getsize(old_name)
        item_size_kb = item_size / 1024
        if item_size_kb > 100:
            print('old name : {}'.format(old_name))
            new_name_pre = item + '.jpg'
            new_name = os.path.join(path_target, new_name_pre)
            shutil.copy(old_name, new_name)
            index = index + 1
            print('No.{}'.format(index))
    print('Done')


if __name__ == '__main__':
    get_pics()
