import os
from PIL import Image

filenames = os.listdir('static')

for i in range(len(filenames)):
    filename = filenames[i]
    img = Image.open(f"static/{filename}")
    img = img.convert('RGB')
    img.save(f"static/{i}.jpeg")
    print(f"File {i}.jpeg")