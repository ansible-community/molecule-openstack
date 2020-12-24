import copy
import functools
import os
import shutil
from pathlib import Path
from uuid import uuid4

import pytest

from molecule import config, util


@pytest.helpers.register
def write_molecule_file(filename, data):
    util.write_file(filename, util.safe_dump(data))


@pytest.fixture
def _molecule_dependency_galaxy_section_data():
    return {"dependency": {"name": "galaxy"}}


@pytest.fixture
def _molecule_driver_section_data():
    return {"driver": {"name": "openstack"}}


@pytest.fixture
def _molecule_platforms_section_data():
    return {
        "platforms": [
            {"name": "instance-1", "groups": ["foo", "bar"], "children": ["child1"]},
            {"name": "instance-2", "groups": ["baz", "foo"], "children": ["child2"]},
        ]
    }


@pytest.fixture
def _molecule_provisioner_section_data():
    return {
        "provisioner": {
            "name": "ansible",
            "options": {"become": True},
            "config_options": {},
        }
    }


@pytest.fixture
def _molecule_scenario_section_data():
    return {"scenario": {"name": "default"}}


@pytest.fixture
def _molecule_verifier_section_data():
    return {"verifier": {"name": "ansible"}}


@pytest.fixture
def molecule_data(
    _molecule_dependency_galaxy_section_data,
    _molecule_driver_section_data,
    _molecule_platforms_section_data,
    _molecule_provisioner_section_data,
    _molecule_scenario_section_data,
    _molecule_verifier_section_data,
):

    fixtures = [
        _molecule_dependency_galaxy_section_data,
        _molecule_driver_section_data,
        _molecule_platforms_section_data,
        _molecule_provisioner_section_data,
        _molecule_scenario_section_data,
        _molecule_verifier_section_data,
    ]

    return functools.reduce(lambda x, y: util.merge_dicts(x, y), fixtures)


@pytest.fixture
def molecule_directory_fixture(temp_dir):
    return pytest.helpers.molecule_directory()


@pytest.fixture
def molecule_scenario_directory_fixture(molecule_directory_fixture):
    path = pytest.helpers.molecule_scenario_directory()
    if not os.path.isdir(path):
        os.makedirs(path)

    return path


@pytest.fixture
def molecule_ephemeral_directory_fixture(molecule_scenario_directory_fixture):
    path = pytest.helpers.molecule_ephemeral_directory(str(uuid4()))
    if not os.path.isdir(path):
        os.makedirs(path)
    yield
    shutil.rmtree(str(Path(path).parent))


@pytest.fixture
def molecule_file_fixture(
    molecule_scenario_directory_fixture, molecule_ephemeral_directory_fixture
):
    return pytest.helpers.molecule_file()


@pytest.fixture
def config_instance(molecule_file_fixture, molecule_data, request):
    mdc = copy.deepcopy(molecule_data)
    if hasattr(request, "param"):
        util.merge_dicts(mdc, request.getfixturevalue(request.param))
    pytest.helpers.write_molecule_file(molecule_file_fixture, mdc)
    c = config.Config(molecule_file_fixture)
    c.command_args = {"subcommand": "test"}

    return c
