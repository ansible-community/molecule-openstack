*************************
Molecule OpenStack Plugin
*************************

.. image:: https://badge.fury.io/py/molecule-openstack.svg
   :target: https://badge.fury.io/py/molecule-openstack
   :alt: PyPI Package

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/python/black
   :alt: Python Black Code Style

.. image:: https://img.shields.io/badge/Code%20of%20Conduct-Ansible-silver.svg
   :target: https://docs.ansible.com/ansible/latest/community/code_of_conduct.html
   :alt: Ansible Code of Conduct

.. image:: https://img.shields.io/badge/Mailing%20lists-Ansible-orange.svg
   :target: https://docs.ansible.com/ansible/latest/community/communication.html#mailing-list-information
   :alt: Ansible mailing lists

.. image:: https://img.shields.io/badge/license-MIT-brightgreen.svg
   :target: LICENSE
   :alt: Repository License

Molecule OpenStack is designed to allow use of OpenStack Clouds for
provisioning test resources.

Please note that this driver is currently in its early stage of development.

.. _installation-and-usage:

Installation and Usage
======================

Install molecule-openstack and pre-requisites:

.. code-block::

   pip install molecule-openstack ansible openstacksdk

Create a new role with molecule using the openstack driver:

.. code-block::

   molecule init role <role_name> -d openstack

Configure ``<role_name>/molecule/default/molecule.yaml`` with required
parameters based on your openstack cloud. A simple config is:

.. code-block:: yaml

   dependency:
      name: galaxy
   driver:
      name: openstack
   platforms:
   - name: molecule-foo
      image: "ubuntu"
      flavor: "m1.medium"
      network: "private"
      fip_pool: "public"
      ssh_user: "ubuntu"
   provisioner:
      name: ansible
   verifier:
      name: ansible

Argument ``fip_pool`` in only required when network is not an external
network. Instead of configuring
``<role_name>/molecule/default/molecule.yaml`` the following environment
variables can be exported:

.. code-block::

   export MOLECULE_OPENSTACK_IMAGE=ubuntu
   export MOLECULE_OPENSTACK_FLAVOR=m1.medium
   export MOLECULE_OPENSTACK_NETWORK=private
   export MOLECULE_OPENSTACK_FIP_POOL=public
   export MOLECULE_OPENSTACK_SSH_USER=ubuntu

After this molecule can be run from the base-dir of the role:

.. code-block::

   source ~/.openrc
   molecule test



.. _get-involved:

Get Involved
============

* Join us in the ``#ansible-molecule`` channel on `Freenode`_.
* Join the discussion in `molecule-users Forum`_.
* Join the community working group by checking the `wiki`_.
* Want to know about releases, subscribe to `ansible-announce list`_.
* For the full list of Ansible email Lists, IRC channels see the
  `communication page`_.

.. _`Freenode`: https://freenode.net
.. _`molecule-users Forum`: https://groups.google.com/forum/#!forum/molecule-users
.. _`wiki`: https://github.com/ansible/community/wiki/Molecule
.. _`ansible-announce list`: https://groups.google.com/group/ansible-announce
.. _`communication page`: https://docs.ansible.com/ansible/latest/community/communication.html

.. _license:

License
=======

The `MIT`_ License.

.. _`MIT`: https://github.com/ansible/molecule/blob/master/LICENSE

The logo is licensed under the `Creative Commons NoDerivatives 4.0 License`_.

If you have some other use in mind, contact us.

.. _`Creative Commons NoDerivatives 4.0 License`: https://creativecommons.org/licenses/by-nd/4.0/
