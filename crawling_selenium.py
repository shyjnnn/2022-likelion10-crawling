import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

#Chromedriver를 통한 웹사이트 접속 (네이버)
url = "https://www.naver.com/"
driver = webdriver.Chrome("C:/Users/shiny/WorkSpace/멋사 10기/크롤링 연습/chromedriver.exe")
driver.get(url = url)

#증권 클릭
stock = driver.find_element(By.XPATH, r"//*[@id='NM_FAVORITE']/div[1]/ul[2]/li[3]/a")
stock.click()

#국내 증시 클릭
domestic = driver.find_element(By.XPATH, r"//*[@id='menu']/ul/li[2]/a/span")
domestic.click()

#시가 총액 클릭
market_cap =driver.find_element(By.XPATH, r'//*[@id="newarea"]/div[1]/ul/li[1]/ul/li[6]/a')
market_cap.click()

filename="시가총액1-200_selenium.csv"
f = open(filename, "w", encoding = "utf-8-sig", newline="")
writer = csv.writer(f)


#정보 수집
for i in range(1,5):
    if(i >= 3):
        page = driver.find_element(By.XPATH, r'//*[@id="contentarea"]/div[3]/table[2]/tbody/tr/td[' + str(i+1) + "]/a")
        page.click()
    else :
        page = driver.find_element(By.XPATH, r'//*[@id="contentarea"]/div[3]/table[2]/tbody/tr/td[' + str(i) + "]/a")
        page.click()
    table = driver.find_element(By.CLASS_NAME, "type_2")
    tbody = table.find_element(By.TAG_NAME, "tbody")
    rows = tbody.find_elements(By.TAG_NAME, "tr")
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")
        if len(columns) < 1:
            continue
        data = [column.text.strip() for column in columns]
        writer.writerow(data)