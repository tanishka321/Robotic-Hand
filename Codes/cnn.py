import numpy as np
import pandas as pd
import cv2
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Lists to hold image data and labels
X = [] # Image data
y = [] # Labels

# Loop through image paths to load images and labels into arrays
for path in imagepaths:
    # Read the image
    img = cv2.imread(path)
    # Convert the image to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Resize the image to a fixed size
    img = cv2.resize(img, (320, 120))
    # Append the processed image to the list
    X.append(img)
    
    # Process the label from the image path
    category = path.split("/")[3]
    label = int(category.split("_")[0][1]) # Assumes label format as described
    y.append(label)

# Convert lists to numpy arrays to speed up train_test_split
X = np.array(X, dtype="uint8")
X = X.reshape(len(imagepaths), 120, 320, 1) # Reshape for CNN input
y = np.array(y)

# Print the number of images and labels loaded
print("Images loaded: ", len(X))
print("Labels loaded: ", len(y))

# Split the data into training and testing sets
test_size = 0.3
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

# Define the CNN model
model = Sequential([
    Conv2D(32, (5, 5), activation='relu', input_shape=(120, 320, 1)), # First convolutional layer
    MaxPooling2D((2, 2)), # First max pooling layer
    Conv2D(64, (3, 3), activation='relu'), # Second convolutional layer
    MaxPooling2D((2, 2)), # Second max pooling layer
    Conv2D(64, (3, 3), activation='relu'), # Third convolutional layer
    MaxPooling2D((2, 2)), # Third max pooling layer
    Flatten(), # Flatten layer to reshape data for the dense layers
    Dense(128, activation='relu'), # Fully connected dense layer
    Dense(10, activation='softmax') # Output layer with softmax activation for 10 classes
])

# Compile the model
model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy', 
              metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=5, batch_size=64, verbose=2, validation_data=(X_test, y_test))

# Evaluate the model on the test set
test_loss, test_acc = model.evaluate(X_test, y_test)
print('Test accuracy: {:2.2f}%'.format(test_acc * 100))

# Make predictions on the test set
predictions = model.predict(X_test)
# Convert predictions to class labels
y_pred = np.argmax(predictions, axis=1)

# Generate and display the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
conf_df = pd.DataFrame(conf_matrix, 
                       columns=["Predicted Thumb Down", "Predicted Palm (H)", "Predicted L", "Predicted Fist (H)", "Predicted Fist (V)", "Predicted Thumbs up", "Predicted Index", "Predicted OK", "Predicted Palm (V)", "Predicted C"],
                       index=["Actual Thumb Down", "Actual Palm (H)", "Actual L", "Actual Fist (H)", "Actual Fist (V)", "Actual Thumbs up", "Actual Index", "Actual OK", "Actual Palm (V)", "Actual C"])

print(conf_df)
