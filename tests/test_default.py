from testinfra.utils.ansible_runner import AnsibleRunner
import yaml

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')
defaults = yaml.load(open('defaults/main.yml', 'r'))


def test_linux(SystemInfo):
    assert SystemInfo.type == 'linux'


def test_packages(Package):
    present = [
        "oracle-java8-installer"
    ]
    if present and not defaults['java_user_install']:
        for package in present:
            p = Package(package)
            assert p.is_installed
