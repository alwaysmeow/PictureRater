from matplotlib import pyplot as plt
import pandas as pd
from PIL import Image

# Чтение данных из CSV файла
df = pd.read_csv("markup.csv")

# Удаление всех строк, где второй столбец равен -1
df = df[df['Mark'] != -1]

data_first_column = df.loc[df['Mark'] == 9, 'Filename'].tolist()
# Создание фигуры и осей для 4x4 сетки графиков
fig, axs = plt.subplots(4, 4, figsize=(10, 10))

# Загрузка и отображение ваших изображений в каждом из подграфиков
for i in range(4):
    for j in range(4):
        # Замените эту строку на код загрузки вашего изображения для каждого подграфика
        print(data_first_column[i * 4 + j])
        image_data = Image.open(f"static/{data_first_column[i * 4 + j]}")
        
        axs[i, j].imshow(image_data, cmap='gray')  # Отображение изображения
        axs[i, j].axis('off')  # Убрать оси координат

plt.tight_layout()  # Автоматическое распределение между графиками
plt.show()