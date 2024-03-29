import tensorflow
import keras

mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# plt.imshow(x_train[0], cmap=plt.cm.binary)
# plt.show()
# print(y_train[0])

x_train = keras.utils.normalize(x_train, axis=1)
x_test = keras.utils.normalize(x_test, axis=1)

model = keras.models.Sequential()
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(128, activation=tensorflow.nn.relu))
model.add(keras.layers.Dense(128, activation=tensorflow.nn.relu))
model.add(keras.layers.Dense(10, activation=tensorflow.nn.softmax))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)
val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss)
print(val_acc)
