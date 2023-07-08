# import logging

# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

# # debug < info < warning < error < critical
# logging.debug("아 이거 누가 짠거야~~")
# logging.info("자동화 수행 준비")
# logging.warning("이 슼릡트는 조금 오래 되었습니다. 실행상에 문제가 있을수 있습니다.")
# logging.error("에러가 발생하였습니다.")
# logging.critical("복구가 불가능한 심각한 문제가 발생하였습니다....")

# 터미널과 파일에 함께 로그 남기기

import logging
from datetime import datetime
logformatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s") # 시간 [로그레벨] 메시지 형태로 로그를 작성
logger = logging.getLogger()
# 로그 레벨 설정
logger.setLevel(logging.DEBUG)

# 스트림
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logformatter)
logger.addHandler(streamHandler)

# 파일
filename = datetime.now().strftime("mylogFile_%Y%m%d%H%M%S.log ")
fileHandler = logging.FileHandler(filename, encoding="utf=8")
fileHandler.setFormatter(logformatter)
logger.addHandler(fileHandler)

logger.debug("로그를 남겨보는 테스트를 진행합니다.")