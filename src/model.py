from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization, Input

def create_model(input_shape=(100,100,3), num_classes=6):
    """
    CNN tabanlı model oluşturur.
    input_shape: Görüntü boyutu (100x100x3)
    num_classes: Sınıf sayısı
    """
    model = Sequential([
        Input(shape=input_shape),  # input_shape uyarısını önler
        Conv2D(32, (3,3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D(2,2),

        Conv2D(64, (3,3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D(2,2),

        Conv2D(128, (3,3), activation='relu'),
        BatchNormalization(),
        MaxPooling2D(2,2),

        Flatten(),
        Dense(256, activation='relu'),
        Dropout(0.5),
        Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

# Notebook'ta kullanmak için:
# from src.model import create_model
# model = create_model(input_shape=(100,100,3))
# model.summary()

