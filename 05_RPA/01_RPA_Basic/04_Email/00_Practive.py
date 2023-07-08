from account import *
to_list = [EMAIL_ADDRESS, EMAIL_ADDRESS, EMAIL_ADDRESS]
# ", " < 이걸로 구분해서 리스트로 넣는다.
msg = ", ".join(to_list)
print(msg)


import time
# %d 날짜
# %a 요일
# %b 달 - 짧게 표시
# %Y 연도
print(time.strftime('%d-%b-%Y')) # 현재 날짜를 일-월-연도

import datetime
dt = datetime.datetime.strptime("2020-12-30", "%Y-%m-%d")
print(type(dt))
print(dt.strftime('%d-%b-%Y'))