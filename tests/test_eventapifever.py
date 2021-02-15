from main import app


def test_version():
    assert app.version == '0.1.0'
