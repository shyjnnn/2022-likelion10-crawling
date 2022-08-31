import csv
from bs4 import BeautifulSoup
import requests

#크롤링할 페이지 주소
url = "https://finance.naver.com/sise/sise_market_sum.naver?&page="

#CSV파일
filename="시가총액1-200_beautifulsoup.csv"
f = open(filename, "w", encoding = "utf-8-sig", newline="")
writer = csv.writer(f)

for page in range(1,5):
    res = requests.get(url +str(page))
    #부적절한 페이지일 경우 오류 발생 시키는 코드
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    data_rows = soup.find("table", attrs={"class" : "type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1 : #의미없는 데이터 skip
            continue
        data = [column.get_text().strip() for column in columns]
        writer.writerow(data)