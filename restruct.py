import os
from PIL import Image

filenames = os.listdir('Faces')

def convert_to_jpeg(file_path):
    try:
        img = Image.open(file_path)
        if img.format == 'PNG':
            jpeg_path = os.path.splitext(file_path)[0] + '.jpeg'
            img = img.convert('RGB')
            img.save(jpeg_path)
            os.remove(file_path)
            print(f"Converted '{file_path}' to '{jpeg_path}'")
        else:
            print(f"'{file_path}' is not a PNG file. Skipping conversion.")
    except Exception as e:
        print(f"Error converting '{file_path}': {e}")

def rename_files(folder_path):
    files = os.listdir(folder_path)
    num_files = len(files)
    num_digits = len(str(num_files))
    
    for i, file_name in enumerate(files, start=1):
        file_path = os.path.join(folder_path, file_name)
        new_file_name = f"{i:0{num_digits}}_{file_name}"
        new_file_path = os.path.join(folder_path, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed '{file_path}' to '{new_file_path}'")

for i in range(len(filenames)):
    filename = filenames[i]
    img = Image.open(f"Faces/{filename}")
    img = img.convert('RGB')
    img.save(f"NewFaces/{i}.jpeg")
    print(f"File {i}.jpeg")
