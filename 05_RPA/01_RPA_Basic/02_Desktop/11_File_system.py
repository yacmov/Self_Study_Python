# 파일 기본
import os
# print(os.getcwd()) # current working directory 현재 작업 공간
# os.chdir("05_RPA_Basic") # rpa_basic 으로 작업 공간 이동
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로 이동
# print(os.getcwd())
# os.chdir("C:/") # 주어진 경로로 이동
# print(os.getcwd())


# # 파일 경로 만들기
# # file_path= os.path.join(os.getcwd(), "my_file.txt")
# # print (file_path)


# # 파일 경로에서 폴더 정보 가져오기
# # r이 들어가면 탈출문자를 사용하지 않고 있는 그대로 받아들인다.
# # print(os.path.dirname(r"C:\Users\yacmo\Desktop\Programing_Language\Python\my_file.txt"))

# # 파일 정보 가져오기
# import time
# import datetime

# file_path = "05_RPA_Basic/02_Desktop/11_File_system.py"
# # 파일의 생성 날짜
# ctime = os.path.getctime(file_path)
# print(ctime)

# # 날짜 정보를 strftime 을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime(file_path)
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime(file_path)
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# # 파일 
# size = os.path.getsize(file_path)
# print(size)


# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir("05_RPA_Basic")) # 주어진 폴더 밑에서 모든 폴더 파일 가져오기

# 파일 목록 가져오기 (하위 폴더 모두 포함)
# result = os.walk(".") # 현재 작업공간이 있는 모든 폴더, 파일 목록 가져오기
# result = os.walk("05_RPA_Basic") # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기

# print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)

# # 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_File_system.py"
# result = []
# for root, dirs, files in os.walk("."):
#     # [a.txt, b.txt .....]
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)

# # 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx, #.txt, 자동화*.png
# import fnmatch
# pattern = "*icon.png" # .py 로 끝나는 모든 파일
# result = []

# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): # 이름이 패턴과 일치
#             result.append(os.path.join(root, name))
# print(result)


# # 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir("05_RPA_Basic"))
# print(os.path.isfile("05_RPA_Basic"))

# print(os.path.isdir("run_icon.png"))
# print(os.path.isfile("run_icon.png"))

# # 만약에 지정된 경로에 해당 하는 파일 / 폴더가 없다면?
# print(os.path.isfile("run_btnnnnn.png"))


# 주어진 경로가 존재하는지?
# if os.path.exists("05_RPA_Basic"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재 하지 않습니다.")


# open("new_file.txt", "a").close()
# os.rename("new_file.txt", "new_file_rename.txt") # 이름 변경 앞에껄 뒤에껄로 변경함


# 파일 삭제하기
# os.remove("new_file_rename.txt")

# 폴더 만들기
# os.mkdir("new_folder") # 현재 경로 기준으로 폴더 생성
# os.mkdir("C:/users/nadocoding/test") # 절대 경로 기준으로 폴더을 생성

# os.remove

# os.mkdir("new_folders/a/b/c") # 경로로 찾아가 폴더를 만든다.

#os.makedirs("new_folders/a/b/c") # 경로로 가기위해 폴더가 없으면 폴더를 생성한다.


# 폴더명 변경하기
# os.rename("new_folder", "new_folder_rename")

# 폴더 지우기
# os.rmdir("rew_folder_rename") # 폴더 안이 비었을때만 삭제 가능

import shutil # shell uilities
# shutil.rmtree("new_filders") # 폴더 안이 비어 있지 않아도 완전 삭제 가능
# 모든 파일이 삭제될 수 있으므로 주의!!!!

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("run_icon.png", "test_folder") # 원본 파일 경로, 대상 폴더 경로
# shutil.copy("run_icon.png", "test_folder/copied_run_btn.png") # 원본 파일 경로, 대상 폴더 경로에 변경된 이름으로 저장

# shutil.copyfile("run_icon.png", "test_folder/copied_run_icon2.png") # 원본 파일 경로, 대상 파일을  변경된 이름으로 저장

# shutil.copy2("run_icon.png", "test_folder/copy2.png") # 원본 파일, 대상 폴더(파일) 경로

# copy, copyfile : 메타 정보 복사 X
# copy2 : 메타정보 복사 O


# 폴더 복사 (폴더 복사기때문에 폴더만 적어야 한다.)
# shutil.copytree("test_folder", "test_folder2") # 원본 폴더 경로, 대상 폴더 경로
# shutil.copytree("test_folder", "test_folder3")

# 폴더 이동
# shutil.move("test_folder", "test_folder3")
# shutil.move("test_folder2", "test_fodler3")
# shutil.move("test_folder3", "test_folder") # 폴더명이 변경되는 효과를 낼수도 있다. 



