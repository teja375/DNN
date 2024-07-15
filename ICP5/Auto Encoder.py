from keras.layers import Input, Dense
from keras.models import Model
from keras.datasets import fashion_mnist
import numpy as np
import matplotlib.pyplot as plt
from keras.optimizers import Adadelta

# Load Fashion MNIST data
(x_train, _), (x_test, _) = fashion_mnist.load_data()

# Normalize and reshape the data
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))

# Define hyperparameters
encoding_dim = 32
input_dim = x_train.shape[1]
noise_factor = 0.5
learning_rate = 1.0
batch_size = 128
epochs = 10

# Define the denoising autoencoder model
input_img = Input(shape=(input_dim,))
encoded = Dense(128, activation='relu')(input_img)
encoded = Dense(encoding_dim, activation='relu')(encoded)

decoded = Dense(128, activation='relu')(encoded)
decoded = Dense(input_dim, activation='sigmoid')(decoded)

denoising_autoencoder = Model(input_img, decoded)
optimizer = Adadelta(learning_rate=learning_rate)
denoising_autoencoder.compile(optimizer=optimizer, loss='binary_crossentropy')

# Introducing noise to the input data
x_train_noisy = x_train + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_train.shape)
x_test_noisy = x_test + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_test.shape)
x_train_noisy = np.clip(x_train_noisy, 0., 1.)
x_test_noisy = np.clip(x_test_noisy, 0., 1.)

# Train the denoising autoencoder
history = denoising_autoencoder.fit(x_train_noisy, x_train,
                                    epochs=epochs,
                                    batch_size=batch_size,
                                    shuffle=True,
                                    validation_data=(x_test_noisy, x_test_noisy))

# Predict on test data
decoded_imgs = denoising_autoencoder.predict(x_test_noisy)

# Visualize one original and reconstructed image
plt.figure(figsize=(10, 4))
# Original image
plt.subplot(1, 2, 1)
plt.imshow(x_test_noisy[0].reshape(28, 28), cmap='gray')
plt.title('Original Noisy Image')
plt.axis('off')
# Reconstructed image
plt.subplot(1, 2, 2)
plt.imshow(decoded_imgs[0].reshape(28, 28), cmap='gray')
plt.title('Reconstructed Image')
plt.axis('off')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper right')
plt.show()