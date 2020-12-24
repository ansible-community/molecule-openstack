import pytest


@pytest.fixture
def patched_config_validate(mocker):
    return mocker.patch("molecule.config.Config._validate")
