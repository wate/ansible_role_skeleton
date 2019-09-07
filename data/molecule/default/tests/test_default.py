import os
import yaml
import pytest
# import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


property = {}
default_var_file = os.environ['MOLECULE_PROJECT_DIRECTORY'] + '/defaults/main.yml'
if os.path.exists(default_var_file):
    property.update(yaml.full_load(open(default_var_file, 'r')))

role_var_file = os.environ['MOLECULE_PROJECT_DIRECTORY'] + '/vars/main.yml'
if os.path.exists(role_var_file):
    property.update(yaml.full_load(open(role_var_file, 'r')))


@pytest.mark.parametrize('name', [
    'packages1',
    'packages2',
])
def test_package(host, name):
    assert host.package(pkg).is_installed

def test_config(host):
    f = host.file('/etc/hosts')
    assert f.exists
    assert f.is_file
    assert f.is_directory
    assert f.is_symlink
    assert f.linked_to == '/run/lock'
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o600
    assert f.contains('test string')
