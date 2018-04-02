#-*- code:utf-8 -*-
import time
import requests
from openpyxl import Workbook

class AccpointsTop(object):

    url = "http://accpoints.api.zw.dev.singulato.com/users"

    def get_json(this):
        params = {'per_page': 1000, 'page': 1}
        data = requests.get(AccpointsTop.url, params = params).json()
        info_list = []
        for item in data:

            info = []
            info.append(item['guid'])
            # info.append(item['name'])
            # info.append(item['nick_name'])
            # info.append(item['phone'])
            # info.append(item['email'])
            info.append(item['accumulate_points'])
            info.append(time.strftime("%Y-%m-%d %H:%M:%S", item['accpoints_first_time']))
            print (item['accpoints_first_time'])
            exit()
            info_list.append(info)
        # return info_list


AccpointsTop = AccpointsTop()
AccpointsTop.get_json()