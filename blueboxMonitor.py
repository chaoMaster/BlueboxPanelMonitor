# -*- coding: GBK -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

import sys
import getopt
import ConfigParser
import re
import subprocess
import threading
import platform



def NetCheck(ip):   # 网络监测函数
    try:
        if platform.system() == "Windows":  # 判断当前系统环境

            p = subprocess.Popen(["ping", "-n", "4", ip],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            outW = p.stdout.read()
            errW = p.stderr.read()
            regex1 = re.compile("100%")
            regex2 = re.compile("找不到主机")

            if (len(regex1.findall(outW))) or (len(regex2.findall(outW))):

                return False
            else:

                return True
        else:
            p = subprocess.Popen(["ping", "-c", "4", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out = p.stdout.read()
            err = p.stderr.read()
            regex1 = re.compile("100.0% packet loss")
            regex2 = re.compile("100% packet loss")

            if (len(regex1.findall(out)) == 0) and (len(regex2.findall(out)) == 0) and ((len(err)) == 0):

                return True
            else:

                return False
    except:
        print "NetCheck work error"
        return False

def threadOffline(threadName, delay): # 开启网络监测线程
    i = 1
    while True:
        time.sleep(180)
        flag1 = NetCheck("www.baidu.com")
        flag2 = NetCheck("chinabluemix.itsm.unisysedge.cn")

        if (flag1 == False) and (flag2 == False):
            print u"网络连接失败"
            offlineBrowser = webdriver.Chrome(executable_path=driverpath)
            offlineBrowser.get(audioPath)
            break


configPath = "config.ini"  # 配置文件名已在此写死，请添加配置文件时务必按照此文件名命名，否则出错

try:  # 读取配置文件
    config = ConfigParser.ConfigParser()
    with open(configPath, 'r+') as cfgfile:
        config.readfp(cfgfile)

    username = config.get("info", "username")
    password = config.get("info", "password")
    driverpath = config.get("info", "driverpath")
    audioPath = config.get("info", "audiopath")
except:
    print "ERR : no configuration \n"
    print "please create configuration file\n"
    print "configuration must be renamed config.ini\n"
    print "configuration need to fill username .password .driverPath .audioPath\n"
    print "driver download and version, CSDN link : http://blog.csdn.net/chaomaster/article/details/52963265\n"
    print "the script will be exit in 5 second\n"
    time.sleep(5)

if (not username) or (not password) or (not driverpath):
    print "Please send the user name, password, drive path to configuration file, such as config.ini "
    sys.exit()


# 由于是客户支持，需要严谨对待，未免出现一些脚本 bug 问题导致错误的回复 ticket ，因此本脚本只做出提醒功能

def threadMain(threadName, delay):  # 开启主线程

    browser = webdriver.Chrome(executable_path=driverpath)
    browser.get("https://support.cn01.bluebox.net/tickets")

    browser.find_element_by_xpath(".//*[@id='user_email']").send_keys(username)
    browser.find_element_by_xpath(".//*[@id='user_password']").send_keys(password)
    browser.find_element_by_xpath(".//*[@id='new_user']/input[4]").click()

    while True:

        timeLocator = (By.XPATH, ".//*[@id='bulk-ticket-form']/div[1]/div[1]/div[3]/div[2]/strong[1]/time")

        WebDriverWait(browser, 30, 0.5).until(EC.visibility_of_element_located(timeLocator))
        # timeString = browser.find_element_by_xpath(".//*[@id='bulk-ticket-form']/div[1]/div[1]/div[3]/div[2]/strong[1]/time").text
        # WebDriverWait(browser,30000,0.5).until("seconds" in timeString)
        if "seconds" in browser.find_element_by_xpath(
                ".//*[@id='bulk-ticket-form']/div[1]/div[1]/div[3]/div[2]/strong[1]/time").text:
            browser.find_element_by_xpath(".//*[@id='bulk-ticket-form']/div[1]/div[1]/div[2]/div[1]/a").click()
            time.sleep(3)


            browserWarning = webdriver.Chrome(executable_path=driverpath)
            browserWarning.get(audioPath)

            break  # 每次处理完一个问题需要重启脚本

threads = []
t1 = threading.Thread(target=threadMain, args=("thread", 0,))
threads.append(t1)
t2 = threading.Thread(target=threadOffline, args=("threadMain", 0,))
threads.append(t2)

if __name__ == "__main__":
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()