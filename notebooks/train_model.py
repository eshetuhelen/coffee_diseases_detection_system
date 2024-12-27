import os
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator


def train_model():
    # Define paths
    train_dir = "C:/Users/dell/Desktop/archive/ethiopian cofee leaf dataset/train aug"

    # Image parameters
    IMAGE_SIZE = 224
    BATCH_SIZE = 32
    EPOCHS = 10  

    # Data augmentation
    data_augmentation = models.Sequential([
        layers.RandomFlip('horizontal'),
        layers.RandomRotation(0.2),
        layers.RandomZoom(0.2),
        layers.RandomHeight(0.2),
        layers.RandomWidth(0.2)
    ])

    # Assuming 'train_dir' contains multiple fruit categories
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2
    )

    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(IMAGE_SIZE, IMAGE_SIZE),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='training'
    )

    validation_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(IMAGE_SIZE, IMAGE_SIZE),
        batch_size=BATCH_SIZE,
        class_mode='categorical',
        subset='validation'
    )

    # Model architecture
    model = models.Sequential([
        data_augmentation,
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(len(train_generator.class_indices), activation='softmax')  # Dynamic number of classes
    ])

    # Compile the model
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    # Train the model
    history = model.fit(
        train_generator,
        epochs=EPOCHS,
        validation_data=validation_generator
    )

    # Save the model
    model_save_path = "C:/Users/dell/Desktop/fruit_detection/fruit_detection/api/model.h5"
    model.save(model_save_path)
    print(f"Model saved to {model_save_path}")

if __name__ == "__main__":
    train_model()

import json

# After training and before saving the model
class_indices = train_generator.class_indices
class_names = list(class_indices.keys())

# Save class names to JSON
class_names_path = "C:/Users/dell/Desktop/fruit_detection/fruit_detection/api/class_names.json"
with open(class_names_path, "w") as f:
    json.dump(class_names, f, indent=4)

print(f"Class names saved to {class_names_path}")

# Save the model
model.save(model_save_path)
