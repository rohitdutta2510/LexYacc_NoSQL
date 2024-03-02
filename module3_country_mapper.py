import os
import sys

file_path = os.path.join(os.getcwd(),'worldwide_country')
# print(file_path)

dir_contents = os.listdir(file_path)
for txt_file in dir_contents:
    print(txt_file)

