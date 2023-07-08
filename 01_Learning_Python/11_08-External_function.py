# # https://docs.python.org/3/py-modindex.html

# # glob : Query the list of folders/files within a path
# import glob
# print(glob.glob("*.py"))


# # os : Basic functions provided by the operating system
# import os
# print(os.getcwd())

# folder = "sample_dir"
# if os.path.exists(folder):
#     print("This folder already exists.")
#     os.rmdir(folder)
#     print("The folder was deleted.")
# else:
#     os.makedirs(folder)
#     print("Created a folder.")


# print(os.listdir())

# import time # time-related functions
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print (datetime.date.today())

today = datetime.date.today()
td = datetime.timedelta(days=100)
print("100 days since we met", today + td)
