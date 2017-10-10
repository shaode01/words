# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 17:00:28 2017

@author: 
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def shanbayExport(wordlist):
    
    df = pd.DataFrame(columns=('word', 'pronunciation', 'definition'))#生成空的pandas表  
    elem=Chrome_login.find_element_by_class_name('jquery-bootstrap-pagination')
    pagenum=int(elem.text.split('\n')[-2])
    for j in range(pagenum):
        urli='https://www.shanbay.com/bdc/learnings/library/#master_tab_p'+str(j+1)
        Chrome_login.get(urli)
        word=Chrome_login.find_elements_by_xpath(".//span[@class='word']")   
        pronunciation=Chrome_login.find_elements_by_xpath(".//span[@class='pronunciation']")   
        definition=Chrome_login.find_elements_by_xpath(".//span[@class='definition']")   
        for i in range(len(word)):
            df.loc[j*10+i] = [word[i].text,pronunciation[i].text,definition[i].text]  
         
    df.to_csv(wordlist,index=False)


wordlist='shanbay.csv'
Chrome_login=webdriver.Chrome()  
url='https://www.shanbay.com/bdc/learnings/library/#master_tab_p1'
Chrome_login.get(url) 
#手动登录
