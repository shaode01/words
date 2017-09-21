# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 00:39:30 2017

@author: Administrator
"""


import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def hujiangAddWord(word):
    elem = Chrome_login.find_element_by_name("w")    
    elem.clear()
    elem.send_keys(word)
    elem.send_keys(Keys.ENTER)
    try:
        elem2 = Chrome_login.find_element_by_class_name("speaker")
        if(elem2.get_attribute('alt')<>u'已经加,点击访问生词本'):
            elem2.click()
    except:
        print word
        pass

    
wordlist='d:\My Documents\Desktop\youdao30.txt'
wordpd=pd.read_csv(wordlist,sep="\t",header=None)
wordpd.columns=['word']
Chrome_login=webdriver.Chrome()  
url='https://dict.hjenglish.com/'
Chrome_login.get(url) 
#手动登录
#wordpd['word'].apply(lambda x:hujiangAddWord(x))
