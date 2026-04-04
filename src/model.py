from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


def build_model():

    model = Sequential([
        Dense(32, activation='relu', input_shape=(2,)),
        Dense(32, activation='relu'),
        Dense(2, activation='linear')
    ])

    model.compile(
        optimizer="adam",
        loss="mse"
    )

    return model