import os

import pytest
from molecule.test.conftest import change_dir_to
from molecule.test.functional.conftest import metadata_lint_update
from molecule.util import run_command

from molecule import logger

LOG = logger.get_logger(__name__)


def test_command_init_scenario(temp_dir):
    role_directory = os.path.join(temp_dir.strpath, "test-init")
    cmd = ["molecule", "init", "role", "test-init"]
    assert run_command(cmd).returncode == 0
    metadata_lint_update(role_directory)

    with change_dir_to(role_directory):
        molecule_directory = pytest.helpers.molecule_directory()
        scenario_directory = os.path.join(molecule_directory, "test-scenario")
        cmd = [
            "molecule",
            "init",
            "scenario",
            "test-scenario",
            "--role-name",
            "test-init",
            "--driver-name",
            "openstack",
        ]
        assert run_command(cmd).returncode == 0

        assert os.path.isdir(scenario_directory)

        cmd = ["molecule", "test", "-s", "test-scenario"]
        assert run_command(cmd).returncode == 0
