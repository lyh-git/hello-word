#coding=utf-8
import io
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=path)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')

from bs4 import BeautifulSoup


driver.get('https://wenku.baidu.com/view/7af9e62d9a6648d7c1c708a1284ac850ad020422.html')

# 获取总页数

html = driver.page_source
driver.close()
path1 = r'C:/Users/HUA\Desktop/s1.txt'
fp = open(path1, 'a+')
p
soup = BeautifulSoup(html, 'lxml')  # 载入html

soups = soup.find_all(class_='reader-word-layer')  # 找到所有id为x的元素

for each in soups:
    text = each.get_text()  # 获取元素里的文字
    print(text)

    try:
      fp.write(text+'\n')
    except UnicodeError as u:
        continue

