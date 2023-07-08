import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/index"
res = requests.get(url)
res.raise_for_status()
with open("navercomics.html", "w", encoding="utf8") as f:
    f.write(res.text)
soup = BeautifulSoup(res.text, "lxml")


# print(soup.title) # 타이틀 스크립트 정보를 가져온다
# print(soup.title.get_text()) # 타이틀 스크립트에서 텍스만 출력 한다
# print(soup.a) # 모든 객체중 처음으로 보이는 a 를 보여줘
# print(soup.a.attrs) # 속성을 보여줘
# print(soup.a["href"]) # "a" element's href
# print(soup.a["id"]) # "a" 엘레멘트에 있는 클래스 혹은 아이디 등중에 지정한 값을 보여줘


# s1 = soup.find(attrs={"class":"GlobalNavigationBar__link--WMOzG"})
# print(soup.find("span", attrs={"class":"itemName"})) # 클래스 값이 span 인 엘레멘트를 찾아줘
# print(soup.find(attrs={"class":"itemName"})) # 클래스 엘레멘트가 엘레멘트인것을 찾아줘


# s1 = soup.find("strong", attrs={"class":"AsideList__ranking--sNPZy"})
# s1 = soup.find("a", attrs={"id":"headerUpgradePremiumBtn"})
# print(s1)

# rank1 = soup.find("img", attrs={"class":"Poster__image--d9XTI"})
# print(rank1.img.get_text())


# rank2 = rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
# print(rank1.parent)
# rank2 = rank1.find_next_sibling("li")
# rank3 = rank2.find_next_sibling("li")
# print(rank2.a.get_text())
# print(rank3.a.get_text())

# rank1.find_next_siblings("li")
# print(soup)
# webtoon = soup.find("a", text="윈드브레이커")
# print(webtoon)