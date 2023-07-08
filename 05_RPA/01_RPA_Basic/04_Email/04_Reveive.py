# pip install imap-tools

from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

# limit = 1 최대 메일 갯수
# reverse=True 이면 메일을 꺼꾸로 받아온다. 즉 마지막 수신한것부터 가져온다.
for msg in mailbox.fetch(limit=1, reverse=True):
    print("제목 : ", msg.subject)
    print("발신자 : ", msg.from_)
    print("수신자 : ", msg.to)
    # print("참조자", msg.cc)
    # print("비밀참조자", msg.bcc)
    print("날짜 : ", msg.date)
    # 시간은 세계 기준시간을 표시해준다. 각 나라별로 + - 해서 해당 지역에 현재 시간을 구해야 한다.

    print("본문 : ", msg.text)
    print("HTML 메시지 : ", msg.html)
    print("=" * 100)

    # 첨부 파일 받기
    for att in msg.attachments:
        print("첨부파일 이름 : ", att.filename)
        print("타입 : ", att.content_type)
        print("크기", att.size)

        # 파일 다운로드
        with open("download_" + att.filename, "wb") as f:
            f.write(att.payload)
            print("첨부 파일 {} 다운로드 완료".format(att.filename))


mailbox.logout()
