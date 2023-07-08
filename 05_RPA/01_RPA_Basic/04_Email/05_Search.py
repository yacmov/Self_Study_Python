from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
# mailbox.logout() < 이부분이 들어가야함 

# with 문을 쓰게 되면 로그아웃을 안써줘도 됨
with MailBox("imap.gmail.com", 993). login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    # for msg in mailbox.fetch(limit=5, reverse=True): # 전체 메일 다 가져오기
    #     print(f"[{msg.from_}] {msg.subject}")
    
    # for msg in mailbox.fetch('(UNSEEN)'): # 읽지 않음 메일 가져오기
    #     print(f"[{msg.from_}] {msg.subject}")

    # for msg in mailbox.fetch('(FROM yacmov@gmail.com)', limit=5, reverse=True): # 특정인이 보낸 메일 가져오기
    #     print(f"[{msg.from_}] {msg.subject}")
    
    # 항상 작은 따옴표로 시작하고 큰 따옴표로 안을 써준다 예시를 아래로
    # for msg in mailbox.fetch('(TEXT "test mail")'): # 어떤 글자를 포함하는 메일 (제목, 본문)
    #     print(f"[{msg.from_}] {msg.subject}")

    # for msg in mailbox.fetch('(SUBJECT "test mail")'): # 어떤 글자를 포함하는 메일 (제목만)
    #     print(f"[{msg.from_}] {msg.subject}")

    # for msg in mailbox.fetch(limit=30, reverse=True): # 어떤 글자(한글)을 포함하는 메일 필터링 
    #     if "테스트" in msg.subject: # 제목에
    #         print(f"[{msg.from_}] {msg.subject}")

    # for msg in mailbox.fetch('SENTSINCE 07-Jun-2023', reverse=True, limit=50): # 특정 날짜 이후로 온 메일
    #     if "테스트" in msg.subject: # 제목에
    #         print(f"[{msg.from_}] {msg.subject}")
    
    # for msg in mailbox.fetch('ON 07-Jun-2023', reverse=True, limit=50): # 특정 날짜에 온 메일
    #     if "테스트" in msg.subject: # 제목에
    #         print(f"[{msg.from_}] {msg.subject}")

    # # 2가지 이상의 조건을 모두 만족하는 메일
    # for msg in mailbox.fetch('(SENTSINCE 07-Jun-2023 SUBJECT "test mail")'): # 특정 날짜에 온 메일
    #     print(f"[{msg.from_}] {msg.subject}")

    # 2가지 중 하나라도 만족하는 메일 (또는 조건)
    for msg in mailbox.fetch('(OR SENTSINCE 07-Jun-2023 SUBJECT "test mail")'): # 특정 날짜에 온 메일
        print(f"[{msg.from_}] {msg.subject}")


# https://pypi.org/project/imap-tools/