from matplotlib import pyplot as plt
import pandas as pd

# Чтение данных из CSV файла
df = pd.read_csv("markup.csv")

plt.figure(figsize=(10, 6))
plt.hist(df['Mark'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Mark')
plt.ylabel('Count')
plt.grid(True)
plt.show()