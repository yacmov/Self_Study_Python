import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?component=&q=노트북&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Safari/605.1.15"}
# res = requests.get(url)
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# print(res.text)

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:
    
    # 광고 제품 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print(" <광고 상품 제외합니다.>")
        continue
    
    name = item.find("div", attrs={"class":"name"}).get_text()
    
    # 애플 제풒 제외
    if "Apple" in name:
        print(" <Apple 상품 제외합니다.>")
        continue
    
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    
    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class":"rating"}) # 평점
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점 없음"
        print(" <평점 없는 상품 제외합니다.>")
        continue
    rate_cnt = item.find("span", attrs={"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1] # 1번째 인덱스 부터 뒤에서 -1 번째 까지 출력
    else:
        rate_cnt = "평점 수 없음"
        print(" <평점 수 없는 상품 제외합니다.>")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)