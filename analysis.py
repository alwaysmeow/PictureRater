from matplotlib import pyplot as plt
import pandas as pd
from PIL import Image

# Чтение данных из CSV файла
df = pd.read_csv("markup.csv")

df = df[df['Mark'] != -1]

data_first_column = df.loc[df['Mark'] == 0, 'Filename'].tolist()
fig, axs = plt.subplots(3, 3, figsize=(10, 10))

for i in range(3):
    for j in range(3):
        print(data_first_column[i * 3 + j])
        image_data = Image.open(f"static/{data_first_column[i * 3 + j]}")
        
        axs[i, j].imshow(image_data, cmap='gray')
        axs[i, j].axis('off')

plt.tight_layout()
plt.show()