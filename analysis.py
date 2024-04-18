from matplotlib import pyplot as plt
import pandas as pd
from PIL import Image

# Чтение данных из CSV файла
df = pd.read_csv("markup.csv")

df = df[df['Mark'] != -1]

size = 6

data_first_column = df.loc[df['Mark'] == 7, 'Filename'].tolist()
fig, axs = plt.subplots(size, size, figsize=(10, 10))

for i in range(size):
    for j in range(size):
        print(data_first_column[i * size + j])
        image_data = Image.open(f"static/{data_first_column[i * size + j]}")
        
        axs[i, j].imshow(image_data, cmap='gray')
        axs[i, j].axis('off')

plt.tight_layout()
plt.show()