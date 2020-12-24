import contextlib
import os
import random
import string

import pytest


@pytest.fixture
def random_string(length=5):
    return "".join((random.choice(string.ascii_uppercase) for _ in range(length)))


@contextlib.contextmanager
def change_dir_to(dir_name):
    cwd = os.getcwd()
    os.chdir(dir_name)
    yield
    os.chdir(cwd)


@pytest.fixture
def temp_dir(tmpdir, random_string, request):
    directory = tmpdir.mkdir(random_string)

    with change_dir_to(directory.strpath):
        yield directory
