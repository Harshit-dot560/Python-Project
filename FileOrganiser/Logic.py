import os
import shutil
Images=[".jpg",".png",".jpeg",".gif",".webp",".avif"]
Document=[".pdf",".txt",".pptx",".docx",".odt",".html",".htm"]
Video=[".mp4",".webm",".mov"]
Folder_type=input("Enter Folder type (Images/ Document/ Video): ").strip().capitalize()
if Folder_type=="Images":
 extensions=Images
elif Folder_type=="Document":
 extensions=Document
elif Folder_type=="Video":
 extensions=Video
else:
 print("Invalid Folder type")
 exit()
os.makedirs(Folder_type,exist_ok=True)
for file in os.listdir():
 if file==Folder_type:
  continue
 if os.path.isfile(file) and file.lower().endswith(tuple(extensions)):
  dest = os.path.join(Folder_type,file)
  name, ext = os.path.splitext(file)
  counter = 1
  while os.path.exists(dest): 
    dest = os.path.join(Folder_type, f"{name}_{counter}{ext}")
    counter += 1
    shutil.move(file, dest)
  #if not os.path.exists(dest): skip the same name file
    #print(f"Moving{file} → {Folder_type}/")
    #shutil.move(file, dest)
print("Files moved successfully!")