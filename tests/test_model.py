from src.model import build_model


def test_model():

    model = build_model(1)

    assert model is not None