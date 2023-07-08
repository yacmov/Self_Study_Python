import requests
res = requests.get("http://google.com")

# print(f"Response Code : {res.status_code}") # 200 이면 정상 응답

# if res.status_code == requests.codes.ok:
#     print("normal")
# else:
#     print(f"Error {res.status_code}")

res.raise_for_status() # will use often than above

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)   