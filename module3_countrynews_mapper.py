import os

curr_dir = os.getcwd()
target_dir = os.path.join(curr_dir,'worldwide_country')

for txt_file in os.listdir(target_dir):
    print(txt_file)