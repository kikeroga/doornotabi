#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import requests
import serial
import random

SERIAL_NAME = '/dev/ttyXXXXX'
SERIAL_PORT = 9600
SERVER_URL = 'http://xxx.xxx.xxx.xxx/send.html'

angle = -1

ser = serial.Serial(SERIAL_NAME, SERIAL_PORT)
time.sleep(2)

ser.write('g')

while True:
    value = int(ser.readline())
    if value != -1:
        tch = value / 1000
        deg = value % 1000
        r = random.randint(1,1000)
        url = SERVER_URL + '?' + 'tch=' + str(tch) + '&' + 'deg=' + str(deg) + '&' + 'r=' + str(r)
        print 'request: ' + url
        res = requests.get(url)
        print res.status_code
        if res.status_code == requests.codes.ok:
            status = res.text
            print 'status: ' + status
            if status == 2:
                ser.write('g')
                # arduino叩く
                print 'CLEAR'
        value = -1 # 受付状態に戻る

ser.close()
