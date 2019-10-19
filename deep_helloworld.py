import tensorflow as tf
import matplotlib.pyplot as plt
import keras

mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
plt.imshow(x_train[0], cmap=plt.cm.binary)
plt.show()
print(y_train[0])
