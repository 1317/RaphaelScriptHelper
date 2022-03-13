# 请将此脚本、img文件夹和ResourceDictionary.py文件复制到项目根目录下再运行！

import ADBHelper, RaphaelScriptHelper, ResourceDictionary

deviceList = ADBHelper.getDevicesList()
print(deviceList)
'''i = 0
for did in deviceList:
    print(str(i) + ": " + did)
    i = i + 1
input_i = input("请输入需要执行脚本的设备编号\n")

delayTime = input("请输入关卡所耗时间（单位：秒）\n")'''

RaphaelScriptHelper.deviceType = 1
# RaphaelScriptHelper.deviceID = deviceList[int(input_i)]
RaphaelScriptHelper.deviceID ="cda135e9"
delayTime = 85
retry_times = 3

for i in range(0,100):
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
