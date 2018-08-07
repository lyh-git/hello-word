from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import  pymongo
from selenium.webdriver.chrome.options import Options

path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=path)

def search():
    driver.get('https://www.taobao.com/')
    input=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q')))
    submi=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_TSearchForm > div.search-button > button')))
    input.send_keys('背包')
    submi.click()
    total=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="mainsrp-itemlist"]/div/div/div/div/div/div/div/img')))
    print(total.text)
    driver.close()
def main():
    search()

if __name__=='__main__':
    main()