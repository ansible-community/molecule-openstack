from molecule import api


def test_driver_is_detected():
    driver_name = __name__.split(".", maxsplit=1).split("_")[-1]
    assert driver_name in [str(d) for d in api.drivers()]
