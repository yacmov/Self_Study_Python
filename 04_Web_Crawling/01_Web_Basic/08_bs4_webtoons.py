import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
with open("navercomicsweek.html", "w", encoding="utf8") as f:
    f.write(res.text)

# 네이버 웹툰 전ㅔ 목록 가오
cartoons = soup.find_all("li", attrs={"class":"DailyListItem__item--LP6_T"})
# 클라스 속성이 타이틀 인 모든 'li' 엘레멘트를 반환함
for cartoon in cartoons:
    print(cartoon.get_text())

