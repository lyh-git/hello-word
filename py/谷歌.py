#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import requests
from lxml import etree
import  pymongo
client=pymongo.MongoClient('localhost',27017)
mydb=client['mydb']
test=mydb['test']

#coding=utf-8
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import time
path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

url_path = "http://image.baidu.com/"
driver.get(url_path)
driver.find_element_by_id('kw').send_keys('美女')
driver.find_element_by_class_name('s_search').click()
path1=r'C:/Users/HUA/Desktop/新建文件夹1/'
list=[]

for i in range(1, 30):
        js = "var q=document.body.scrollTop=" + str(500 * i)  # PhantomJS
        js = "var q=document.documentElement.scrollTop=" + str(500 * i)  # 谷歌 和 火狐

        driver.execute_script(js)



        driver.implicitly_wait(10)

        html=driver.page_source


        items=etree.HTML(html)


        data={
        'imgs':items.xpath('// *[ @ id = "imgid"]/div / ul / li/@data-objurl')}



print(data)

test.insert_one(data)



