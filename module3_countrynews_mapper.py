import os
import sys

curr_dir = os.getcwd()  # Current working directory
target_dir = os.path.join(curr_dir,'worldwide_country')  # Target director where given countries news is present

countries = ['Australia','India','England','Malaysia','Singapore']
file_name = sys.argv[1]

# Getting the filepath
file_path = os.path.join(target_dir,file_name)  

print(file_path)  #Sends the file path to combiner