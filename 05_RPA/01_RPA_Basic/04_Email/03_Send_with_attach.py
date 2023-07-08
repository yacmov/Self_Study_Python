import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다" 
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS 
msg.set_content("다운로드 하세요") 

# msg.add_attachment()

# mime type
# https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
with open("테스트.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)

with open("테스트엑셀.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype="aplication", subtype="vnd.ms-excel", filename=f.name)

# octet-stream 으로도 보내는게 가능함 지원하지 않는 확장자일 경우
# with open("테스트엑셀.xlsx", "rb") as f:
#     msg.add_attachment(f.read(), maintype="aplication", subtype="octet-stream", filename=f.name)

with open("file_menu.png", "rb") as f:
    msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)



with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)