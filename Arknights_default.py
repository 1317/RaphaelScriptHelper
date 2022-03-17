# 请将此脚本、img文件夹和ResourceDictionary.py文件复制到项目根目录下再运行！

import ADBHelper
import RaphaelScriptHelper
import ResourceDictionary

deviceList = ADBHelper.getDevicesList()
# print(deviceList)
'''i = 0
for did in deviceList:
    print(str(i) + ": " + did)
    i = i + 1
input_i = input("请输入需要执行脚本的设备编号\n")

delayTime = input("请输入关卡所耗时间（单位：秒）\n")'''

RaphaelScriptHelper.deviceType = 1
# RaphaelScriptHelper.deviceID = deviceList[int(input_i)]
RaphaelScriptHelper.deviceID = "cda135e9"


class Operation(object):
    def __init__(self, id, duration, description=''):
        self.id = id
        self.duration = duration
        self.description = description


operation_info = {'1-7': Operation('1-7', 85, '刷固源岩'), 'GA-8': Operation('GA-8', 160)}

delayTime = operation_info['GA-8'].duration
retry_times = 3

for i in range(0, 100):
    j = 0
    while j < retry_times:
        RaphaelScriptHelper.find_pic_touch(ResourceDictionary.start_QHD)
        RaphaelScriptHelper.random_delay()
        if RaphaelScriptHelper.find_pic_touch(ResourceDictionary.start1_QHD):
            break
        j = j + 1
        RaphaelScriptHelper.random_delay()

    RaphaelScriptHelper.delay(int(delayTime))

    j = 0
    while j < retry_times:
        if RaphaelScriptHelper.find_pic_touch(ResourceDictionary.finish_QHD):
            break
        j = j + 1
        RaphaelScriptHelper.delay(3)

    RaphaelScriptHelper.delay(3)
    RaphaelScriptHelper.random_delay()
