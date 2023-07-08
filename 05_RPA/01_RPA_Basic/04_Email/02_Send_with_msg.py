import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = EMAIL_ADDRESS # 받는 사람

# 여러명에게 메일을 보낼 떄
# msg["To"] = EMAIL_ADDRESS, EMAIL_ADDRESS
# to_list = [EMAIL_ADDRESS, EMAIL_ADDRESS]
# msg["To"] = ", ".join(to_list)

# # 참조
# msg["Cc"] = EMAIL_ADDRESS

# # 비밀참조
# msg["Bcc"] = EMAIL_ADDRESS

# # 그렇다면 숨은 참조는 무엇일까요? 
# # 이메일을 보내면서 참조인으로 누구를 집어넣고 싶은데, 
# # 받는 사람은 모르게 하고 싶을 때 사용하는 기능입니다. 
# # 또는, 이메일을 누군가에게 보내야 하는데 
# # 수신자끼리 서로를 확인할 수 없게 하고 싶을 때 
# # 사용하기도 합니다. 
# # 받는 사람을 자기 자신으로 하고 숨은 참조에
# # 수신자들을 입력하면, 
# # 이메일은 가는데 서로가 누구인지는 모르겠죠. 
# # 예를 들어 이벤트 당첨 단체공지를 날리거나 할 때에는 
# # 대상자들을 받는 사람에 입력을 하기보다는 
# # 숨은 참조에 입력을 하고, 받는 사람을 자기 자신으로 하는 것이 효과적입니다.

msg.set_content("테스트 본문입니다") # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)