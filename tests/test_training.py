from src.data_processing import load_data
from src.train import train_model
from src.evaluate import evaluate_model


def test_training():

    X_train, X_test, y_train, y_test = load_data()

    model = train_model(X_train, y_train)

    assert model is not None


def test_model_quality():

    X_train, X_test, y_train, y_test = load_data()

    model = train_model(X_train, y_train)

    metrics = evaluate_model(model, X_test, y_test)

    assert metrics["r2"] > 0.95