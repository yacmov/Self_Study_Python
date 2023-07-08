import requests
from bs4 import BeautifulSoup

url = "http://play.google.com/store/moves/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Safari/605.1.15",
    "Accept-Language":"ko-KR,ko" # 지정된 언어로 접속하기

}
 
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
# movies2 = soup.find_all("div", attrs={"class":["abcd", "ddef"]}) # 리스트로 감싸주면 abcd 또는 ddef 인 클라스에 대한 정보를 가져온다 
print(len(movies))

# with open("movie.html", "w", encoding="utf8") as f: 
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnk0zc"}).get_text()
    print(title)