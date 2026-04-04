from src.model import build_model


def train_model(X_train_scaled, y_train_scaled):

    model = build_model()

    history = model.fit(
        X_train_scaled,
        y_train_scaled,
        epochs=200,
        batch_size=32,
        validation_split=0.1,
        verbose=0
    )

    return model, history