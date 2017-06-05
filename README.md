<p><img src="https://vignette2.wikia.nocookie.net/logopedia/images/6/6a/Java-logo.jpg" alt="java logo" title="java" align="right" height="60" /></p>

Ansible Role: java
==================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/java/master)](https://ci.devops.sosoftware.pl/blue/organizations/jenkins/SoInteractive%2Fjava/activity) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/18236.svg)](https://galaxy.ansible.com/SoInteractive/java/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

JVM installation

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.java
```

Role can be also run as unprivileged user without ability to use `yum` or `apt`
```yaml
- hosts: all
  roles:
    - SoInteractive.java
  vars:
    java_user_install: true
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.

TODO
----

- Tests, tests, tests
- CentOS7 support
- Tests for user-based install
