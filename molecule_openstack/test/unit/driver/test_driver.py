import os

import pytest

from molecule import api, config
from molecule_openstack import driver


@pytest.fixture
def openstack_instance(patched_config_validate, config_instance):
    return driver.Openstack(config_instance)


def test_openstack_config_gives_config_object(openstack_instance):
    assert isinstance(openstack_instance._config, config.Config)


def test_openstack_name_property(openstack_instance):
    assert "openstack" == openstack_instance.name


def test_openstack_options_property(openstack_instance):
    assert {"managed": True} == openstack_instance.options


def test_openstack_login_cmd_template_property(openstack_instance):
    template = "ssh {address} -l {user} -p {port}"
    assert template in openstack_instance.login_cmd_template


def test_openstack_safe_files_property(openstack_instance):
    expected_safe_files = [
        os.path.join(
            openstack_instance._config.scenario.ephemeral_directory,
            "instance_config.yml",
        )
    ]

    assert expected_safe_files == openstack_instance.safe_files


def test_openstack_delegated_property(openstack_instance):
    assert not openstack_instance.delegated


def test_openstack_managed_property(openstack_instance):
    assert openstack_instance.managed


def test_created(openstack_instance):
    assert "false" == openstack_instance._created()


def test_converged(openstack_instance):
    assert "false" == openstack_instance._converged()


def test_openstack_status(mocker, openstack_instance):
    openstack_status = openstack_instance.status()

    assert 2 == len(openstack_status)

    assert openstack_status[0].instance_name == "instance-1"
    assert openstack_status[0].driver_name == "openstack"
    assert openstack_status[0].provisioner_name == "ansible"
    assert openstack_status[0].scenario_name == "default"
    assert openstack_status[0].created == "false"
    assert openstack_status[0].converged == "false"

    assert openstack_status[1].instance_name == "instance-2"
    assert openstack_status[1].driver_name == "openstack"
    assert openstack_status[1].provisioner_name == "ansible"
    assert openstack_status[1].scenario_name == "default"
    assert openstack_status[1].created == "false"
    assert openstack_status[1].converged == "false"


def test_driver_is_detected():
    driver_name = __name__.split(".")[0].split("_")[-1]
    assert driver_name in [str(d) for d in api.drivers()]
