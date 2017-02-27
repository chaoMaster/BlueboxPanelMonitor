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



def NetCheck(ip):   # �����⺯��
    try:
        if platform.system() == "Windows":  # �жϵ�ǰϵͳ����

            p = subprocess.Popen(["ping", "-n", "4", ip],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            outW = p.stdout.read()
            errW = p.stderr.read()
            regex1 = re.compile("100%")
            regex2 = re.compile("�Ҳ�������")

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

def threadOffline(threadName, delay): # �����������߳�
    i = 1
    while True:
        time.sleep(180)
        flag1 = NetCheck("www.baidu.com")
        flag2 = NetCheck("chinabluemix.itsm.unisysedge.cn")

        if (flag1 == False) and (flag2 == False):
            print u"��������ʧ��"
            offlineBrowser = webdriver.Chrome(executable_path=driverpath)
            offlineBrowser.get(audioPath)
            break


configPath = "config.ini"  # �����ļ������ڴ�д��������������ļ�ʱ��ذ��մ��ļ����������������

try:  # ��ȡ�����ļ�
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


# �����ǿͻ�֧�֣���Ҫ�Ͻ��Դ���δ�����һЩ�ű� bug ���⵼�´���Ļظ� ticket ����˱��ű�ֻ�������ѹ���

def threadMain(threadName, delay):  # �������߳�

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

            break  # ÿ�δ�����һ��������Ҫ�����ű�

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