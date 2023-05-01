#importing  required modules
import os
from shutil import move

#create directories
root_direct="C:\\users\\[Username]\\Downloads"
image_direct="C:\\users\\[Username]\\Downloads\\images"
doc_direct="C:\\users\\[Username]\\Downloads\\documents"
videos_direct="C:\\users\\[Username]\\Downloads\\videos"

#type of files
doc= ('.docx','.doc','.txt', '.pdf')
img=('.jpg', '.jpeg', '.png')
video= ('.mp4')

#run over files
files=[]
for i in os.listdir(root_direct):
    if os.path.isfile(i) and not i.startwith('.') and not i._eq_(_file_):
        files.append(i)

# file moved and overwritten if already exists
def move_files(files):
  for file in files:
    if file.endswith(doc):
      move(file, '{}/{}'.format(documents_dir, file))
      print('file {} moved to {}'.format(file, doc_direct))
    elif file.endswith(doc):
      move(file, '{}/{}'.format(image_dir, file))
      print('file {} moved to {}'.format(file, image_direct))
    elif file.endswith(video):
      move(file, '{}/{}'.format(software_dir, file))
      print('file {} moved to {}'.format(file, videos_direct))
    else:
      move(file, '{}/{}'.format(root_direct, file))
      print('file {} moved to {}'.format(file, root_direct))

if os.path.isfile(new):
    print ("already exists")
