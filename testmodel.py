import tensorflow as tf
from PIL import Image
from matplotlib import pyplot as plt
from random import randint
import numpy as np

img_size = 299
size = 3
model = tf.keras.models.load_model('models/model1.h5')

def get_image(path):
    image = tf.image.decode_jpeg(tf.io.read_file(path), channels=3)
    image = tf.cast(tf.image.resize_with_pad(image, img_size, img_size), dtype = tf.float32)
    return tf.keras.applications.inception_v3.preprocess_input(image)

def test(path):
    img = get_image(path)
    return model.predict(np.expand_dims(img, axis=0))[0][0]

fig, axs = plt.subplots(size, size, figsize=(10, 10))

for i in range(size):
    for j in range(size):
        path = f"static/{randint(0, 2577)}.jpeg"
        image_data = Image.open(path)

        axs[i, j].imshow(image_data, cmap='gray')
        axs[i, j].axis('off')
        axs[i, j].set_title(test(path))

plt.show()