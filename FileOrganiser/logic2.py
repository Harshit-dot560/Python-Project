import os

Images = [".jpg", ".png", ".jpeg", ".gif", ".webp", ".avif"]

files = [f for f in os.listdir() 
         if os.path.isfile(f) and f.lower().endswith(tuple(Images))]

# Sort files by modified time
files.sort(key=lambda x: os.path.getmtime(x))

for i, file in enumerate(files, start=1):
    name, ext = os.path.splitext(file)
    new_name = f"{i:03d}{ext}"   # 001.jpg, 002.jpg

    os.rename(file, new_name)

    print(f"{file} → {new_name}")