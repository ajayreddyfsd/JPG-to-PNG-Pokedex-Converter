import sys
import os
from PIL import Image

#to get the args from the command line
x = sys.argv[1]
y = sys.argv[2]

#making relative folder paths using the args
folder1_path = f'./{x}'
folder2_path = f'./{y}'

#creating the folder2 if it doesnt exist
if not (os.path.exists(folder2_path)):
   os.makedirs(folder2_path, exist_ok=True)

#loop through all the files in folder1
for file in os.listdir(folder1_path):
   file_path = os.path.join(folder1_path, file)
   if(file_path):
      img = Image.open(file_path) #open the file, change the path and extension and then save it 
      file_path = os.path.join(folder2_path, file)
      file_path = file_path.replace('jpg', 'png')
      img.save(file_path, 'png')
