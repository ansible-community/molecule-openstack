import os
import pathlib

from molecule.test.conftest import change_dir_to
from molecule.util import run_command

from molecule import logger

LOG = logger.get_logger(__name__)


def test_command_init_role(temp_dir):
    os.path.join(temp_dir.strpath, "test-init")
    cmd = ["molecule", "init", "role", "acme.test_init"]
    assert run_command(cmd).returncode == 0


def test_command_init_scenario(tmp_path: pathlib.Path):
    """Verify that init scenario works."""
    scenario_name = "default"

    with change_dir_to(tmp_path):
        scenario_directory = tmp_path / "molecule" / scenario_name
        cmd = [
            "molecule",
            "init",
            "scenario",
            scenario_name,
            "--driver-name",
            "openstack",
        ]
        result = run_command(cmd)
        assert result.returncode == 0

        assert scenario_directory.exists()

        # run molecule reset as this may clean some leftovers from other
        # test runs and also ensure that reset works.
        result = run_command(["molecule", "reset"])  # default sceanario
        assert result.returncode == 0

        result = run_command(["molecule", "reset", "-s", scenario_name])
        assert result.returncode == 0
