import os
import csv
import pandas as pd
from PIL import Image

i = len(os.listdir('static'))
sourcedir = 'kinopoisk'
filenames = os.listdir(sourcedir)
df = pd.read_csv("markup.csv")

for filename in filenames:
    if filename[-5:] == ".jpeg":
        img = Image.open(f"{sourcedir}/{filename}")
        img.save(f"static/{i}.jpeg")
        df = df._append({"Filename": f"{i}.jpeg", "Mark": "-1"}, ignore_index=True)
        i += 1

df.to_csv("markup2.csv", index=False)