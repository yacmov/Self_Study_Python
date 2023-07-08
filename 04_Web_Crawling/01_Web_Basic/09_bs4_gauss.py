import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# 만화 가져오기
# cartoons = soup.find_all("td", attrs = {"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a['href']
# for cartoon in cartoons:
#     print(cartoon.get_text())
#     link = cartoon["href"] 
#     print(f"https://comic.naver.com/{link})")

# 평점 구하기
total_rates = 0
cartoons = soup.find_all('div', attrs={'class':'rating_type'})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates += float(rate)
print('Total Score :', total_rates)
print('Average Score : ', total_rates / len(cartoons))
